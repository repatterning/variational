"""
Module setup.py
"""
import sys

import config
import src.elements.s3_parameters as s3p
import src.elements.service as sr
import src.functions.directories
import src.s3.bucket
import src.s3.prefix


class Setup:
    """

    Notes
    -----

    This class prepares the Amazon S3 (Simple Storage Service) and local data environments.
    """

    def __init__(self, service: sr.Service, s3_parameters: s3p.S3Parameters):
        """
        
        :param service: A suite of services for interacting with Amazon Web Services.
        :param s3_parameters: The overarching S3 parameters settings of this project, e.g., region code
                              name, buckets, etc.
        """

        self.__service: sr.Service = service
        self.__s3_parameters: s3p.S3Parameters = s3_parameters

        # Configurations
        self.__configurations = config.Config()

        # An instance for interacting with objects within an Amazon S3 prefix
        self.__pre = src.s3.prefix.Prefix(service=self.__service, bucket_name=self.__s3_parameters.internal)

        self.__prefixes = ['', '']

    def __clear_prefix(self) -> bool:
        """

        :return:
        """

        # Get the keys therein
        states = []
        for prefix in self.__prefixes:
            keys: list[str] = self.__pre.objects(prefix=prefix)
            if len(keys) > 0:
                objects = [{'Key' : key} for key in keys]
                state = self.__pre.delete(objects=objects)
                states.append(bool(state))
            else:
                states.append(True)

        return all(states)

    def __s3(self) -> bool:
        """
        Prepares an Amazon S3 (Simple Storage Service) bucket.

        :return:
        """

        # An instance for interacting with Amazon S3 buckets.
        bucket = src.s3.bucket.Bucket(service=self.__service, location_constraint=self.__s3_parameters.location_constraint,
                                      bucket_name=self.__s3_parameters.internal)

        if bucket.exists():
            return self.__clear_prefix()

        return bucket.create()

    def __local(self) -> bool:
        """

        :return:
        """

        # An instance for interacting with local directories
        directories = src.functions.directories.Directories()
        directories.cleanup(path=self.__configurations.warehouse)

        # The warehouse
        return directories.create(path=self.__configurations.warehouse)

    def exc(self) -> bool:
        """

        :return:
        """

        return self.__s3() & self.__local()
