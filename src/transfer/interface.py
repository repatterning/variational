"""Module interface.py"""
import json
import logging
import os

import boto3
import pandas as pd

import config
import src.elements.s3_parameters as s3p
import src.elements.service as sr
import src.s3.ingress
import src.transfer.dictionary
import src.transfer.metadata
import src.transfer.cloud


class Interface:
    """
    Class Interface
    """

    def __init__(self, connector: boto3.session.Session, service: sr.Service,  s3_parameters: s3p):
        """

        :param connector:
        :param service: A suite of services for interacting with Amazon Web Services.
        :param s3_parameters: The overarching S3 parameters settings of this
                              project, e.g., region code name, buckets, etc.
        """

        self.__service: sr.Service = service
        self.__s3_parameters: s3p.S3Parameters = s3_parameters

        self.__configurations = config.Config()

        # Metadata dictionary
        self.__metadata = src.transfer.metadata.Metadata(connector=connector).exc(architecture='variational')

    def __set_metadata(self, frame: pd.DataFrame) -> pd.DataFrame:
        """

        :param frame:
        :return:
        """

        # Assign metadata dict strings via section values
        frame['metadata'] = frame['section'].map(lambda x: self.__metadata[x])

        return frame


    def exc(self):
        """

        :return:
        """

        # Prepare
        src.transfer.cloud.Cloud(service=self.__service, s3_parameters=self.__s3_parameters).exc()

        # The strings for transferring data to Amazon S3 (Simple Storage Service)
        strings: pd.DataFrame = src.transfer.dictionary.Dictionary().exc(
            path=self.__configurations.warehouse, extension='*', prefix='')

        # Transfer
        if strings.empty:
            logging.info('Empty')
        else:
            strings = self.__set_metadata(frame=strings.copy())
            logging.info(strings)
            messages = src.s3.ingress.Ingress(
                service=self.__service, bucket_name=self.__s3_parameters.internal).exc(
                strings=strings, tags={'project': 'hydrography'})
            logging.info(messages)
