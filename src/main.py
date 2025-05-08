"""Module main.py"""
import datetime
import logging
import os
import sys

import boto3
import tensorflow as tf


def main():

    """
    Entry Point

    :return:
    """

    logger: logging.Logger = logging.getLogger(__name__)
    logger.info('Starting: %s', datetime.datetime.now().isoformat(timespec='microseconds'))
    logger.info('CPU: %s', tf.config.list_physical_devices('CPU'))
    logger.info('GPU: %s', tf.config.list_physical_devices('GPU'))

    # partitions: catchment & time series codes, listings: list of files and supplementary data
    partitions, listings = src.assets.interface.Interface(
        service=service, s3_parameters=s3_parameters, arguments=arguments).exc()
    logger.info(partitions)

    # Modelling
    src.modelling.interface.Interface(
        listings=listings, arguments=arguments).exc(partitions=partitions)

    # Deleting __pycache__
    src.functions.cache.Cache().exc()


if __name__ == '__main__':

    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    # Logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d\n',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Modules
    import src.assets.interface
    import src.elements.s3_parameters as s3p
    import src.elements.service as sr
    import src.functions.cache
    import src.modelling.interface
    import src.preface.interface

    connector: boto3.session.Session
    s3_parameters: s3p.S3Parameters
    service: sr.Service
    arguments: dict
    connector, s3_parameters, service, arguments = src.preface.interface.Interface().exc()

    # Devices
    gpu = tf.config.list_physical_devices('GPU')

    if arguments.get('cpu') | (not gpu):
        os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
        tf.config.set_visible_devices([], 'GPU')

    main()
