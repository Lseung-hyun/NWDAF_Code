# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.scheduled_communication_time import ScheduledCommunicationTime
from openapi_server.models.traffic_characterization import TrafficCharacterization
from openapi_server import util

from openapi_server.models.scheduled_communication_time import ScheduledCommunicationTime  # noqa: E501
from openapi_server.models.traffic_characterization import TrafficCharacterization  # noqa: E501

class UeCommunication(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, comm_dur=None, comm_dur_variance=None, perio_time=None, perio_time_variance=None, ts=None, ts_variance=None, recurring_time=None, traf_char=None, ratio=None, confidence=None):  # noqa: E501
        """UeCommunication - a model defined in OpenAPI

        :param comm_dur: The comm_dur of this UeCommunication.  # noqa: E501
        :type comm_dur: int
        :param comm_dur_variance: The comm_dur_variance of this UeCommunication.  # noqa: E501
        :type comm_dur_variance: float
        :param perio_time: The perio_time of this UeCommunication.  # noqa: E501
        :type perio_time: int
        :param perio_time_variance: The perio_time_variance of this UeCommunication.  # noqa: E501
        :type perio_time_variance: float
        :param ts: The ts of this UeCommunication.  # noqa: E501
        :type ts: datetime
        :param ts_variance: The ts_variance of this UeCommunication.  # noqa: E501
        :type ts_variance: float
        :param recurring_time: The recurring_time of this UeCommunication.  # noqa: E501
        :type recurring_time: ScheduledCommunicationTime
        :param traf_char: The traf_char of this UeCommunication.  # noqa: E501
        :type traf_char: TrafficCharacterization
        :param ratio: The ratio of this UeCommunication.  # noqa: E501
        :type ratio: int
        :param confidence: The confidence of this UeCommunication.  # noqa: E501
        :type confidence: int
        """
        self.openapi_types = {
            'comm_dur': int,
            'comm_dur_variance': float,
            'perio_time': int,
            'perio_time_variance': float,
            'ts': datetime,
            'ts_variance': float,
            'recurring_time': ScheduledCommunicationTime,
            'traf_char': TrafficCharacterization,
            'ratio': int,
            'confidence': int
        }

        self.attribute_map = {
            'comm_dur': 'commDur',
            'comm_dur_variance': 'commDurVariance',
            'perio_time': 'perioTime',
            'perio_time_variance': 'perioTimeVariance',
            'ts': 'ts',
            'ts_variance': 'tsVariance',
            'recurring_time': 'recurringTime',
            'traf_char': 'trafChar',
            'ratio': 'ratio',
            'confidence': 'confidence'
        }

        self._comm_dur = comm_dur
        self._comm_dur_variance = comm_dur_variance
        self._perio_time = perio_time
        self._perio_time_variance = perio_time_variance
        self._ts = ts
        self._ts_variance = ts_variance
        self._recurring_time = recurring_time
        self._traf_char = traf_char
        self._ratio = ratio
        self._confidence = confidence

    @classmethod
    def from_dict(cls, dikt) -> 'UeCommunication':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UeCommunication of this UeCommunication.  # noqa: E501
        :rtype: UeCommunication
        """
        return util.deserialize_model(dikt, cls)

    @property
    def comm_dur(self):
        """Gets the comm_dur of this UeCommunication.

        indicating a time in seconds.  # noqa: E501

        :return: The comm_dur of this UeCommunication.
        :rtype: int
        """
        return self._comm_dur

    @comm_dur.setter
    def comm_dur(self, comm_dur):
        """Sets the comm_dur of this UeCommunication.

        indicating a time in seconds.  # noqa: E501

        :param comm_dur: The comm_dur of this UeCommunication.
        :type comm_dur: int
        """
        if comm_dur is None:
            raise ValueError("Invalid value for `comm_dur`, must not be `None`")  # noqa: E501

        self._comm_dur = comm_dur

    @property
    def comm_dur_variance(self):
        """Gets the comm_dur_variance of this UeCommunication.

        string with format \"float\" as defined in OpenAPI.  # noqa: E501

        :return: The comm_dur_variance of this UeCommunication.
        :rtype: float
        """
        return self._comm_dur_variance

    @comm_dur_variance.setter
    def comm_dur_variance(self, comm_dur_variance):
        """Sets the comm_dur_variance of this UeCommunication.

        string with format \"float\" as defined in OpenAPI.  # noqa: E501

        :param comm_dur_variance: The comm_dur_variance of this UeCommunication.
        :type comm_dur_variance: float
        """

        self._comm_dur_variance = comm_dur_variance

    @property
    def perio_time(self):
        """Gets the perio_time of this UeCommunication.

        indicating a time in seconds.  # noqa: E501

        :return: The perio_time of this UeCommunication.
        :rtype: int
        """
        return self._perio_time

    @perio_time.setter
    def perio_time(self, perio_time):
        """Sets the perio_time of this UeCommunication.

        indicating a time in seconds.  # noqa: E501

        :param perio_time: The perio_time of this UeCommunication.
        :type perio_time: int
        """

        self._perio_time = perio_time

    @property
    def perio_time_variance(self):
        """Gets the perio_time_variance of this UeCommunication.

        string with format \"float\" as defined in OpenAPI.  # noqa: E501

        :return: The perio_time_variance of this UeCommunication.
        :rtype: float
        """
        return self._perio_time_variance

    @perio_time_variance.setter
    def perio_time_variance(self, perio_time_variance):
        """Sets the perio_time_variance of this UeCommunication.

        string with format \"float\" as defined in OpenAPI.  # noqa: E501

        :param perio_time_variance: The perio_time_variance of this UeCommunication.
        :type perio_time_variance: float
        """

        self._perio_time_variance = perio_time_variance

    @property
    def ts(self):
        """Gets the ts of this UeCommunication.

        string with format \"date-time\" as defined in OpenAPI.  # noqa: E501

        :return: The ts of this UeCommunication.
        :rtype: datetime
        """
        return self._ts

    @ts.setter
    def ts(self, ts):
        """Sets the ts of this UeCommunication.

        string with format \"date-time\" as defined in OpenAPI.  # noqa: E501

        :param ts: The ts of this UeCommunication.
        :type ts: datetime
        """

        self._ts = ts

    @property
    def ts_variance(self):
        """Gets the ts_variance of this UeCommunication.

        string with format \"float\" as defined in OpenAPI.  # noqa: E501

        :return: The ts_variance of this UeCommunication.
        :rtype: float
        """
        return self._ts_variance

    @ts_variance.setter
    def ts_variance(self, ts_variance):
        """Sets the ts_variance of this UeCommunication.

        string with format \"float\" as defined in OpenAPI.  # noqa: E501

        :param ts_variance: The ts_variance of this UeCommunication.
        :type ts_variance: float
        """

        self._ts_variance = ts_variance

    @property
    def recurring_time(self):
        """Gets the recurring_time of this UeCommunication.


        :return: The recurring_time of this UeCommunication.
        :rtype: ScheduledCommunicationTime
        """
        return self._recurring_time

    @recurring_time.setter
    def recurring_time(self, recurring_time):
        """Sets the recurring_time of this UeCommunication.


        :param recurring_time: The recurring_time of this UeCommunication.
        :type recurring_time: ScheduledCommunicationTime
        """

        self._recurring_time = recurring_time

    @property
    def traf_char(self):
        """Gets the traf_char of this UeCommunication.


        :return: The traf_char of this UeCommunication.
        :rtype: TrafficCharacterization
        """
        return self._traf_char

    @traf_char.setter
    def traf_char(self, traf_char):
        """Sets the traf_char of this UeCommunication.


        :param traf_char: The traf_char of this UeCommunication.
        :type traf_char: TrafficCharacterization
        """
        if traf_char is None:
            raise ValueError("Invalid value for `traf_char`, must not be `None`")  # noqa: E501

        self._traf_char = traf_char

    @property
    def ratio(self):
        """Gets the ratio of this UeCommunication.

        Unsigned integer indicating Sampling Ratio (see clauses 4.15.1 of 3GPP TS 23.502), expressed in percent.  # noqa: E501

        :return: The ratio of this UeCommunication.
        :rtype: int
        """
        return self._ratio

    @ratio.setter
    def ratio(self, ratio):
        """Sets the ratio of this UeCommunication.

        Unsigned integer indicating Sampling Ratio (see clauses 4.15.1 of 3GPP TS 23.502), expressed in percent.  # noqa: E501

        :param ratio: The ratio of this UeCommunication.
        :type ratio: int
        """
        if ratio is not None and ratio > 100:  # noqa: E501
            raise ValueError("Invalid value for `ratio`, must be a value less than or equal to `100`")  # noqa: E501
        if ratio is not None and ratio < 1:  # noqa: E501
            raise ValueError("Invalid value for `ratio`, must be a value greater than or equal to `1`")  # noqa: E501

        self._ratio = ratio

    @property
    def confidence(self):
        """Gets the confidence of this UeCommunication.

        Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.  # noqa: E501

        :return: The confidence of this UeCommunication.
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this UeCommunication.

        Unsigned Integer, i.e. only value 0 and integers above 0 are permissible.  # noqa: E501

        :param confidence: The confidence of this UeCommunication.
        :type confidence: int
        """
        if confidence is not None and confidence < 0:  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must be a value greater than or equal to `0`")  # noqa: E501

        self._confidence = confidence
