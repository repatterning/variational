"""
Module config
"""
import datetime
import logging
import os


class Config:
    """
    Class Config

    For project settings
    """

    def __init__(self):
        """
        Constructor
        """

        '''
        Date Stamp
        '''
        now = datetime.datetime.now()
        self.stamp: str = now.strftime('%Y-%m-%d')
        logging.info(self.stamp)

        '''
        Keys
        '''
        self.s3_parameters_key = 's3_parameters.yaml'
        self.arguments_key = 'artefacts' + '/' + 'architecture' + '/' + 'variational' + '/' + 'arguments.json'

        '''
        Local Paths
        '''
        self.warehouse: str = os.path.join(os.getcwd(), 'warehouse')
        self.assets_ = os.path.join(self.warehouse, 'assets', 'variational', self.stamp)
