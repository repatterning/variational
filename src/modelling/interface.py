import logging
import dask

import pandas as pd

import src.elements.partitions as pr
import src.modelling.data
import src.modelling.splittings


class Interface:
    """
    <b>Notes</b><br>
    ------<br>
    The interface to drift score programs.<br>
    """

    def __init__(self, listings: pd.DataFrame, arguments: dict):
        """

        :param listings: List of files
        :param arguments: The arguments.
        """

        self.__listings = listings
        self.__arguments = arguments

    @dask.delayed
    def __get_listing(self, ts_id: int) -> list[str]:
        """

        :param ts_id:
        :return:
        """

        return self.__listings.loc[
            self.__listings['ts_id'] == ts_id, 'uri'].to_list()

    def exc(self, partitions: list[pr.Partitions]):
        """

        :param partitions:
        :return:
        """

        # Delayed Functions
        __data = dask.delayed(src.modelling.data.Data(arguments=self.__arguments).exc)
        __splittings = dask.delayed(src.modelling.splittings.Splittings(arguments=self.__arguments).exc)

        # Compute
        computations = []
        for partition in partitions:
            listing = self.__get_listing(ts_id=partition.ts_id)
            data = __data(listing=listing)
            splittings = __splittings(data=data)
            computations.append(splittings)
        latest = dask.compute(computations, scheduler='threads')[0]

        logging.info(latest)
