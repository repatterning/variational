"""Module partitions.py"""
import datetime
import typing

import pandas as pd


class Partitions:
    """
    Partitions for parallel computation.
    """

    def __init__(self, data: pd.DataFrame, arguments: dict):
        """

        :param data:
        :param arguments:
        """

        self.__data = data
        self.__arguments = arguments

    def __boundaries(self) -> typing.Tuple[datetime.datetime, datetime.datetime]:
        """
        The boundaries of the dates; datetime format

        :return:
        """

        # The boundaries of the dates; datetime format
        spanning = self.__arguments.get('spanning')
        as_from = datetime.date.today() - datetime.timedelta(days=round(spanning*365))
        starting = datetime.datetime.strptime(f'{as_from.year}-01-01', '%Y-%m-%d')

        _end = datetime.datetime.now().year
        ending = datetime.datetime.strptime(f'{_end}-01-01', '%Y-%m-%d')

        return starting, ending

    def __dates(self, starting: datetime.datetime, ending: datetime.datetime) -> pd.DataFrame:
        """

        :param starting:
        :param ending:
        :return:
        """

        # Create series
        frame = pd.date_range(start=starting, end=ending, freq=self.__arguments.get('catchments').get('frequency')
                              ).to_frame(index=False, name='datestr')

        return frame['datestr'].apply(lambda x: x.strftime('%Y-%m-%d')).to_frame()

    def exc(self) -> pd.DataFrame:
        """

        :return:
        """

        starting, ending = self.__boundaries()
        dates = self.__dates(starting=starting, ending=ending)
        frame = dates.merge(self.__data, how='left', on='datestr')
        
        return frame
