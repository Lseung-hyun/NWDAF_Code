import connexion

import six
import openapi_server
from openapi_server.models.analytics_data import AnalyticsData
from openapi_server.models.base_model_ import Model  # noqa: E501
from openapi_server.models.event_filter import EventFilter  # noqa: E501
from openapi_server.models.event_id import EventId  # noqa: E501
from openapi_server.models.event_reporting_requirement import EventReportingRequirement
from openapi_server.models.network_perf_info import NetworkPerfInfo
from openapi_server.models.network_perf_type import NetworkPerfType
from openapi_server.models.nf_load_level_information import NfLoadLevelInformation  # noqa: E501
from openapi_server.models.problem_details import ProblemDetails  # noqa: E501
from openapi_server.models.problem_details_analytics_info_request import ProblemDetailsAnalyticsInfoRequest
from openapi_server.models.service_experience_info import ServiceExperienceInfo
from openapi_server.models.slice_load_level_information import SliceLoadLevelInformation  # noqa: E501
from openapi_server.models.target_ue_information import TargetUeInformation  # noqa: E501
from openapi_server import util
from openapi_server.models.analytics_data import AnalyticsData
from openapi_server.models.ue_communication import UeCommunication
from openapi_server.models.ue_mobility import UeMobility
from openapi_server.models.test_scenario import analytic_result
from connexion.operations.openapi import OpenAPIOperation


service = 0

def get_nwdaf_analytics(event_id, ana_req=None, event_filter=None, supported_features=None, tgt_ue=None):  # noqa: E501

    if connexion.request.is_json:
        event_id =  EventId.from_dict(connexion.request.get_json())  # noqa: E501
        ana_req =  EventReportingRequirement.from_dict(connexion.request.get_json())  # noqa: E501
        event_filter =  EventFilter.from_dict(connexion.request.get_json())  # noqa: E501
        tgt_ue =  TargetUeInformation.from_dict(connexion.request.get_json())  # noqa: E501

        return "do some magic!"


    service = connexion.operations.openapi.tmpqry
    event_id = service["event-id"]
#    ana_req = service["ana-req"]
#    event_filter = service["event-filter"]
#    tgt_ue = service["tgt-ue"]


    if event_id == "LOAD_LEVEL_INFORMATION":
        return AnalyticsData(slice_load_level_infos =[SliceLoadLevelInformation()]).to_dict()

    if event_id == "NETWORK_PERFORMANCE":
        return AnalyticsData(nw_perfs=[NetworkPerfInfo()]).to_dict()

    if event_id == "DATA_ANALYTIC_REQUEST":
        ana_res = "Accuracy:", analytic_result()
        data_ana_res = ''.join(ana_res)
        return data_ana_res

    if event_id == "NF_LOAD":
        return AnalyticsData(nf_load_level_infos=[NfLoadLevelInformation()]).to_dict() 

    if event_id == "SERVICE_EXPERINECE":
        return AnalyticsData(svc_exps=[ServiceExperienceInfo()]).to_dict()

    if event_id == "UE_MOBILITY":
        return AnalyticsData(ue_mobs=[UeMobility()]).to_dict()

    if event_id == "UE_COMMUNICATION":
        return AnalyticsData(ue_comms=[UeCommunication()]).to_dict()  
 
# Additional services supportable (Defined in TS29.520) 

    else:
        return "Not Supported Service"




# Initially generated code 
#def get_nwdaf_analytics(event_id, ana_req=None, event_filter=None, supported_features=None, tgt_ue=None):  # noqa: E501

    """Read a NWDAF Analytics

     # noqa: E501

    :param event_id: Identify the analytics.
    :type event_id: dict | bytes
    :param ana_req: Identifies the analytics reporting requirement information.
    :type ana_req: dict | bytes
    :param event_filter: Identify the analytics.
    :type event_filter: dict | bytes
    :param supported_features: To filter irrelevant s related to unsupported features
    :type supported_features: str
    :param tgt_ue: Identify the target UE information.
    :type tgt_ue: dict | bytes

    :rtype: AnalyticsData
    """

#    if connexion.request.is_json:
#        event_id =  EventId.from_dict(connexion.request.get_json())  # noqa: E501
#        ana_req =  EventReportingRequirement.from_dict(connexion.request.get_json())  # noqa: E501
#        event_filter =  EventFilter.from_dict(connexion.request.get_json())  # noqa: E501
#        tgt_ue =  TargetUeInformation.from_dict(connexion.request.get_json())  # noqa: E501

#        return "do some magic!"

#    if event_id == "LOAD_LEVEL_INFORMATION":
#        return AnalyticsData(slice_load_level_infos =[SliceLoadLevelInformation()]).to_dict()

#    if event_id == "NETWORK_PERFORMANCE":
#            return AnalyticsData(nw_perfs=[NetworkPerfInfo()]).to_dict()

#    if event_id == "NF_LOAD":
#        return AnalyticsData(nf_load_level_infos=[NfLoadLevelInformation()]).to_dict() 

#    if event_id == "SERVICE_EXPERINECE":
#        return AnalyticsData(svc_exps=[ServiceExperienceInfo()]).to_dict()

#    if event_id == "UE_MOBILITY":
#        return AnalyticsData(ue_mobs=[UeMobility()]).to_dict()

#    if event_id == "UE_COMMUNICATION":
#        return AnalyticsData(ue_comms=[UeCommunication()]).to_dict()        