"""Module partitions.py"""
import typing


class Partitions(typing.NamedTuple):
    """
    The data type class ⇾ Partitions<br><br>

    Attributes<br>
    ----------<br>
    <b>ts_id</b>: int<br>
        The identification code of a time series.<br><br>
    <b>catchment_id</b>: int<br>
        The identification code of a catchment area.<br><br>
    <b>datestr</b>: str<br>
        The <b>date string of the start date of a period</b>, format %Y-%m-%d,  i.e., YYYY-mm-dd.<br><br>
    <b>uri</b>: str<br>
        A uniform resource locator
    """

    ts_id: int
    catchment_id: int
    datestr: str
    uri: str
