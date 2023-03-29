# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.abnormal_behaviour import AbnormalBehaviour
from openapi_server.models.analytics_metadata_info import AnalyticsMetadataInfo
from openapi_server.models.dn_perf_info import DnPerfInfo
from openapi_server.models.network_perf_info import NetworkPerfInfo
from openapi_server.models.nf_load_level_information import NfLoadLevelInformation
from openapi_server.models.nsi_load_level_info import NsiLoadLevelInfo
from openapi_server.models.nwdaf_event import NwdafEvent
from openapi_server.models.nwdaf_failure_code import NwdafFailureCode
from openapi_server.models.qos_sustainability_info import QosSustainabilityInfo
from openapi_server.models.service_experience_info import ServiceExperienceInfo
from openapi_server.models.slice_load_level_information import SliceLoadLevelInformation
from openapi_server.models.ue_communication import UeCommunication
from openapi_server.models.ue_mobility import UeMobility
from openapi_server.models.user_data_congestion_info import UserDataCongestionInfo
from openapi_server import util

from openapi_server.models.abnormal_behaviour import AbnormalBehaviour  # noqa: E501
from openapi_server.models.analytics_metadata_info import AnalyticsMetadataInfo  # noqa: E501
from openapi_server.models.dn_perf_info import DnPerfInfo  # noqa: E501
from openapi_server.models.network_perf_info import NetworkPerfInfo  # noqa: E501
from openapi_server.models.nf_load_level_information import NfLoadLevelInformation  # noqa: E501
from openapi_server.models.nsi_load_level_info import NsiLoadLevelInfo  # noqa: E501
from openapi_server.models.nwdaf_event import NwdafEvent  # noqa: E501
from openapi_server.models.nwdaf_failure_code import NwdafFailureCode  # noqa: E501
from openapi_server.models.qos_sustainability_info import QosSustainabilityInfo  # noqa: E501
from openapi_server.models.service_experience_info import ServiceExperienceInfo  # noqa: E501
from openapi_server.models.slice_load_level_information import SliceLoadLevelInformation  # noqa: E501
from openapi_server.models.ue_communication import UeCommunication  # noqa: E501
from openapi_server.models.ue_mobility import UeMobility  # noqa: E501
from openapi_server.models.user_data_congestion_info import UserDataCongestionInfo  # noqa: E501

class EventNotification(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, event=None, start=None, expiry=None, time_stamp_gen=None, fail_notify_code=None, rv_wait_time=None, ana_meta_info=None, nf_load_level_infos=None, nsi_load_level_infos=None, slice_load_level_info=None, svc_exps=None, qos_sustain_infos=None, ue_comms=None, ue_mobs=None, user_data_cong_infos=None, abnor_behavrs=None, nw_perfs=None, dn_perf_infos=None):  # noqa: E501
        """EventNotification - a model defined in OpenAPI

        :param event: The event of this EventNotification.  # noqa: E501
        :type event: NwdafEvent
        :param start: The start of this EventNotification.  # noqa: E501
        :type start: datetime
        :param expiry: The expiry of this EventNotification.  # noqa: E501
        :type expiry: datetime
        :param time_stamp_gen: The time_stamp_gen of this EventNotification.  # noqa: E501
        :type time_stamp_gen: datetime
        :param fail_notify_code: The fail_notify_code of this EventNotification.  # noqa: E501
        :type fail_notify_code: NwdafFailureCode
        :param rv_wait_time: The rv_wait_time of this EventNotification.  # noqa: E501
        :type rv_wait_time: int
        :param ana_meta_info: The ana_meta_info of this EventNotification.  # noqa: E501
        :type ana_meta_info: AnalyticsMetadataInfo
        :param nf_load_level_infos: The nf_load_level_infos of this EventNotification.  # noqa: E501
        :type nf_load_level_infos: List[NfLoadLevelInformation]
        :param nsi_load_level_infos: The nsi_load_level_infos of this EventNotification.  # noqa: E501
        :type nsi_load_level_infos: List[NsiLoadLevelInfo]
        :param slice_load_level_info: The slice_load_level_info of this EventNotification.  # noqa: E501
        :type slice_load_level_info: SliceLoadLevelInformation
        :param svc_exps: The svc_exps of this EventNotification.  # noqa: E501
        :type svc_exps: List[ServiceExperienceInfo]
        :param qos_sustain_infos: The qos_sustain_infos of this EventNotification.  # noqa: E501
        :type qos_sustain_infos: List[QosSustainabilityInfo]
        :param ue_comms: The ue_comms of this EventNotification.  # noqa: E501
        :type ue_comms: List[UeCommunication]
        :param ue_mobs: The ue_mobs of this EventNotification.  # noqa: E501
        :type ue_mobs: List[UeMobility]
        :param user_data_cong_infos: The user_data_cong_infos of this EventNotification.  # noqa: E501
        :type user_data_cong_infos: List[UserDataCongestionInfo]
        :param abnor_behavrs: The abnor_behavrs of this EventNotification.  # noqa: E501
        :type abnor_behavrs: List[AbnormalBehaviour]
        :param nw_perfs: The nw_perfs of this EventNotification.  # noqa: E501
        :type nw_perfs: List[NetworkPerfInfo]
        :param dn_perf_infos: The dn_perf_infos of this EventNotification.  # noqa: E501
        :type dn_perf_infos: List[DnPerfInfo]
        """
        self.openapi_types = {
            'event': NwdafEvent,
            'start': datetime,
            'expiry': datetime,
            'time_stamp_gen': datetime,
            'fail_notify_code': NwdafFailureCode,
            'rv_wait_time': int,
            'ana_meta_info': AnalyticsMetadataInfo,
            'nf_load_level_infos': List[NfLoadLevelInformation],
            'nsi_load_level_infos': List[NsiLoadLevelInfo],
            'slice_load_level_info': SliceLoadLevelInformation,
            'svc_exps': List[ServiceExperienceInfo],
            'qos_sustain_infos': List[QosSustainabilityInfo],
            'ue_comms': List[UeCommunication],
            'ue_mobs': List[UeMobility],
            'user_data_cong_infos': List[UserDataCongestionInfo],
            'abnor_behavrs': List[AbnormalBehaviour],
            'nw_perfs': List[NetworkPerfInfo],
            'dn_perf_infos': List[DnPerfInfo]
        }

        self.attribute_map = {
            'event': 'event',
            'start': 'start',
            'expiry': 'expiry',
            'time_stamp_gen': 'timeStampGen',
            'fail_notify_code': 'failNotifyCode',
            'rv_wait_time': 'rvWaitTime',
            'ana_meta_info': 'anaMetaInfo',
            'nf_load_level_infos': 'nfLoadLevelInfos',
            'nsi_load_level_infos': 'nsiLoadLevelInfos',
            'slice_load_level_info': 'sliceLoadLevelInfo',
            'svc_exps': 'svcExps',
            'qos_sustain_infos': 'qosSustainInfos',
            'ue_comms': 'ueComms',
            'ue_mobs': 'ueMobs',
            'user_data_cong_infos': 'userDataCongInfos',
            'abnor_behavrs': 'abnorBehavrs',
            'nw_perfs': 'nwPerfs',
            'dn_perf_infos': 'dnPerfInfos'
        }

        self._event = event
        self._start = start
        self._expiry = expiry
        self._time_stamp_gen = time_stamp_gen
        self._fail_notify_code = fail_notify_code
        self._rv_wait_time = rv_wait_time
        self._ana_meta_info = ana_meta_info
        self._nf_load_level_infos = nf_load_level_infos
        self._nsi_load_level_infos = nsi_load_level_infos
        self._slice_load_level_info = slice_load_level_info
        self._svc_exps = svc_exps
        self._qos_sustain_infos = qos_sustain_infos
        self._ue_comms = ue_comms
        self._ue_mobs = ue_mobs
        self._user_data_cong_infos = user_data_cong_infos
        self._abnor_behavrs = abnor_behavrs
        self._nw_perfs = nw_perfs
        self._dn_perf_infos = dn_perf_infos

    @classmethod
    def from_dict(cls, dikt) -> 'EventNotification':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EventNotification of this EventNotification.  # noqa: E501
        :rtype: EventNotification
        """
        return util.deserialize_model(dikt, cls)

    @property
    def event(self):
        """Gets the event of this EventNotification.


        :return: The event of this EventNotification.
        :rtype: NwdafEvent
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this EventNotification.


        :param event: The event of this EventNotification.
        :type event: NwdafEvent
        """
        if event is None:
            raise ValueError("Invalid value for `event`, must not be `None`")  # noqa: E501

        self._event = event

    @property
    def start(self):
        """Gets the start of this EventNotification.

        string with format \"date-time\" as defined in OpenAPI.  # noqa: E501

        :return: The start of this EventNotification.
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this EventNotification.

        string with format \"date-time\" as defined in OpenAPI.  # noqa: E501

        :param start: The start of this EventNotification.
        :type start: datetime
        """

        self._start = start

    @property
    def expiry(self):
        """Gets the expiry of this EventNotification.

        string with format \"date-time\" as defined in OpenAPI.  # noqa: E501

        :return: The expiry of this EventNotification.
        :rtype: datetime
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this EventNotification.

        string with format \"date-time\" as defined in OpenAPI.  # noqa: E501

        :param expiry: The expiry of this EventNotification.
        :type expiry: datetime
        """

        self._expiry = expiry

    @property
    def time_stamp_gen(self):
        """Gets the time_stamp_gen of this EventNotification.

        string with format \"date-time\" as defined in OpenAPI.  # noqa: E501

        :return: The time_stamp_gen of this EventNotification.
        :rtype: datetime
        """
        return self._time_stamp_gen

    @time_stamp_gen.setter
    def time_stamp_gen(self, time_stamp_gen):
        """Sets the time_stamp_gen of this EventNotification.

        string with format \"date-time\" as defined in OpenAPI.  # noqa: E501

        :param time_stamp_gen: The time_stamp_gen of this EventNotification.
        :type time_stamp_gen: datetime
        """

        self._time_stamp_gen = time_stamp_gen

    @property
    def fail_notify_code(self):
        """Gets the fail_notify_code of this EventNotification.


        :return: The fail_notify_code of this EventNotification.
        :rtype: NwdafFailureCode
        """
        return self._fail_notify_code

    @fail_notify_code.setter
    def fail_notify_code(self, fail_notify_code):
        """Sets the fail_notify_code of this EventNotification.


        :param fail_notify_code: The fail_notify_code of this EventNotification.
        :type fail_notify_code: NwdafFailureCode
        """

        self._fail_notify_code = fail_notify_code

    @property
    def rv_wait_time(self):
        """Gets the rv_wait_time of this EventNotification.

        indicating a time in seconds.  # noqa: E501

        :return: The rv_wait_time of this EventNotification.
        :rtype: int
        """
        return self._rv_wait_time

    @rv_wait_time.setter
    def rv_wait_time(self, rv_wait_time):
        """Sets the rv_wait_time of this EventNotification.

        indicating a time in seconds.  # noqa: E501

        :param rv_wait_time: The rv_wait_time of this EventNotification.
        :type rv_wait_time: int
        """

        self._rv_wait_time = rv_wait_time

    @property
    def ana_meta_info(self):
        """Gets the ana_meta_info of this EventNotification.


        :return: The ana_meta_info of this EventNotification.
        :rtype: AnalyticsMetadataInfo
        """
        return self._ana_meta_info

    @ana_meta_info.setter
    def ana_meta_info(self, ana_meta_info):
        """Sets the ana_meta_info of this EventNotification.


        :param ana_meta_info: The ana_meta_info of this EventNotification.
        :type ana_meta_info: AnalyticsMetadataInfo
        """

        self._ana_meta_info = ana_meta_info

    @property
    def nf_load_level_infos(self):
        """Gets the nf_load_level_infos of this EventNotification.


        :return: The nf_load_level_infos of this EventNotification.
        :rtype: List[NfLoadLevelInformation]
        """
        return self._nf_load_level_infos

    @nf_load_level_infos.setter
    def nf_load_level_infos(self, nf_load_level_infos):
        """Sets the nf_load_level_infos of this EventNotification.


        :param nf_load_level_infos: The nf_load_level_infos of this EventNotification.
        :type nf_load_level_infos: List[NfLoadLevelInformation]
        """
        if nf_load_level_infos is not None and len(nf_load_level_infos) < 1:
            raise ValueError("Invalid value for `nf_load_level_infos`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._nf_load_level_infos = nf_load_level_infos

    @property
    def nsi_load_level_infos(self):
        """Gets the nsi_load_level_infos of this EventNotification.


        :return: The nsi_load_level_infos of this EventNotification.
        :rtype: List[NsiLoadLevelInfo]
        """
        return self._nsi_load_level_infos

    @nsi_load_level_infos.setter
    def nsi_load_level_infos(self, nsi_load_level_infos):
        """Sets the nsi_load_level_infos of this EventNotification.


        :param nsi_load_level_infos: The nsi_load_level_infos of this EventNotification.
        :type nsi_load_level_infos: List[NsiLoadLevelInfo]
        """
        if nsi_load_level_infos is not None and len(nsi_load_level_infos) < 1:
            raise ValueError("Invalid value for `nsi_load_level_infos`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._nsi_load_level_infos = nsi_load_level_infos

    @property
    def slice_load_level_info(self):
        """Gets the slice_load_level_info of this EventNotification.


        :return: The slice_load_level_info of this EventNotification.
        :rtype: SliceLoadLevelInformation
        """
        return self._slice_load_level_info

    @slice_load_level_info.setter
    def slice_load_level_info(self, slice_load_level_info):
        """Sets the slice_load_level_info of this EventNotification.


        :param slice_load_level_info: The slice_load_level_info of this EventNotification.
        :type slice_load_level_info: SliceLoadLevelInformation
        """

        self._slice_load_level_info = slice_load_level_info

    @property
    def svc_exps(self):
        """Gets the svc_exps of this EventNotification.


        :return: The svc_exps of this EventNotification.
        :rtype: List[ServiceExperienceInfo]
        """
        return self._svc_exps

    @svc_exps.setter
    def svc_exps(self, svc_exps):
        """Sets the svc_exps of this EventNotification.


        :param svc_exps: The svc_exps of this EventNotification.
        :type svc_exps: List[ServiceExperienceInfo]
        """
        if svc_exps is not None and len(svc_exps) < 1:
            raise ValueError("Invalid value for `svc_exps`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._svc_exps = svc_exps

    @property
    def qos_sustain_infos(self):
        """Gets the qos_sustain_infos of this EventNotification.


        :return: The qos_sustain_infos of this EventNotification.
        :rtype: List[QosSustainabilityInfo]
        """
        return self._qos_sustain_infos

    @qos_sustain_infos.setter
    def qos_sustain_infos(self, qos_sustain_infos):
        """Sets the qos_sustain_infos of this EventNotification.


        :param qos_sustain_infos: The qos_sustain_infos of this EventNotification.
        :type qos_sustain_infos: List[QosSustainabilityInfo]
        """
        if qos_sustain_infos is not None and len(qos_sustain_infos) < 1:
            raise ValueError("Invalid value for `qos_sustain_infos`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._qos_sustain_infos = qos_sustain_infos

    @property
    def ue_comms(self):
        """Gets the ue_comms of this EventNotification.


        :return: The ue_comms of this EventNotification.
        :rtype: List[UeCommunication]
        """
        return self._ue_comms

    @ue_comms.setter
    def ue_comms(self, ue_comms):
        """Sets the ue_comms of this EventNotification.


        :param ue_comms: The ue_comms of this EventNotification.
        :type ue_comms: List[UeCommunication]
        """
        if ue_comms is not None and len(ue_comms) < 1:
            raise ValueError("Invalid value for `ue_comms`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ue_comms = ue_comms

    @property
    def ue_mobs(self):
        """Gets the ue_mobs of this EventNotification.


        :return: The ue_mobs of this EventNotification.
        :rtype: List[UeMobility]
        """
        return self._ue_mobs

    @ue_mobs.setter
    def ue_mobs(self, ue_mobs):
        """Sets the ue_mobs of this EventNotification.


        :param ue_mobs: The ue_mobs of this EventNotification.
        :type ue_mobs: List[UeMobility]
        """
        if ue_mobs is not None and len(ue_mobs) < 1:
            raise ValueError("Invalid value for `ue_mobs`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._ue_mobs = ue_mobs

    @property
    def user_data_cong_infos(self):
        """Gets the user_data_cong_infos of this EventNotification.


        :return: The user_data_cong_infos of this EventNotification.
        :rtype: List[UserDataCongestionInfo]
        """
        return self._user_data_cong_infos

    @user_data_cong_infos.setter
    def user_data_cong_infos(self, user_data_cong_infos):
        """Sets the user_data_cong_infos of this EventNotification.


        :param user_data_cong_infos: The user_data_cong_infos of this EventNotification.
        :type user_data_cong_infos: List[UserDataCongestionInfo]
        """
        if user_data_cong_infos is not None and len(user_data_cong_infos) < 1:
            raise ValueError("Invalid value for `user_data_cong_infos`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._user_data_cong_infos = user_data_cong_infos

    @property
    def abnor_behavrs(self):
        """Gets the abnor_behavrs of this EventNotification.


        :return: The abnor_behavrs of this EventNotification.
        :rtype: List[AbnormalBehaviour]
        """
        return self._abnor_behavrs

    @abnor_behavrs.setter
    def abnor_behavrs(self, abnor_behavrs):
        """Sets the abnor_behavrs of this EventNotification.


        :param abnor_behavrs: The abnor_behavrs of this EventNotification.
        :type abnor_behavrs: List[AbnormalBehaviour]
        """
        if abnor_behavrs is not None and len(abnor_behavrs) < 1:
            raise ValueError("Invalid value for `abnor_behavrs`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._abnor_behavrs = abnor_behavrs

    @property
    def nw_perfs(self):
        """Gets the nw_perfs of this EventNotification.


        :return: The nw_perfs of this EventNotification.
        :rtype: List[NetworkPerfInfo]
        """
        return self._nw_perfs

    @nw_perfs.setter
    def nw_perfs(self, nw_perfs):
        """Sets the nw_perfs of this EventNotification.


        :param nw_perfs: The nw_perfs of this EventNotification.
        :type nw_perfs: List[NetworkPerfInfo]
        """
        if nw_perfs is not None and len(nw_perfs) < 1:
            raise ValueError("Invalid value for `nw_perfs`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._nw_perfs = nw_perfs

    @property
    def dn_perf_infos(self):
        """Gets the dn_perf_infos of this EventNotification.


        :return: The dn_perf_infos of this EventNotification.
        :rtype: List[DnPerfInfo]
        """
        return self._dn_perf_infos

    @dn_perf_infos.setter
    def dn_perf_infos(self, dn_perf_infos):
        """Sets the dn_perf_infos of this EventNotification.


        :param dn_perf_infos: The dn_perf_infos of this EventNotification.
        :type dn_perf_infos: List[DnPerfInfo]
        """
        if dn_perf_infos is not None and len(dn_perf_infos) < 1:
            raise ValueError("Invalid value for `dn_perf_infos`, number of items must be greater than or equal to `1`")  # noqa: E501

        self._dn_perf_infos = dn_perf_infos
