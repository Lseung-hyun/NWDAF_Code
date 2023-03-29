# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.cell_global_id import CellGlobalId
from openapi_server.models.location_area_id import LocationAreaId
from openapi_server.models.routing_area_id import RoutingAreaId
from openapi_server.models.service_area_id import ServiceAreaId
import re
from openapi_server import util

from openapi_server.models.cell_global_id import CellGlobalId  # noqa: E501
from openapi_server.models.location_area_id import LocationAreaId  # noqa: E501
from openapi_server.models.routing_area_id import RoutingAreaId  # noqa: E501
from openapi_server.models.service_area_id import ServiceAreaId  # noqa: E501
import re  # noqa: E501

class GeraLocation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, location_number=None, cgi=None, rai=None, sai=None, lai=None, vlr_number=None, msc_number=None, age_of_location_information=None, ue_location_timestamp=None, geographical_information=None, geodetic_information=None):  # noqa: E501
        """GeraLocation - a model defined in OpenAPI

        :param location_number: The location_number of this GeraLocation.  # noqa: E501
        :type location_number: str
        :param cgi: The cgi of this GeraLocation.  # noqa: E501
        :type cgi: CellGlobalId
        :param rai: The rai of this GeraLocation.  # noqa: E501
        :type rai: RoutingAreaId
        :param sai: The sai of this GeraLocation.  # noqa: E501
        :type sai: ServiceAreaId
        :param lai: The lai of this GeraLocation.  # noqa: E501
        :type lai: LocationAreaId
        :param vlr_number: The vlr_number of this GeraLocation.  # noqa: E501
        :type vlr_number: str
        :param msc_number: The msc_number of this GeraLocation.  # noqa: E501
        :type msc_number: str
        :param age_of_location_information: The age_of_location_information of this GeraLocation.  # noqa: E501
        :type age_of_location_information: int
        :param ue_location_timestamp: The ue_location_timestamp of this GeraLocation.  # noqa: E501
        :type ue_location_timestamp: datetime
        :param geographical_information: The geographical_information of this GeraLocation.  # noqa: E501
        :type geographical_information: str
        :param geodetic_information: The geodetic_information of this GeraLocation.  # noqa: E501
        :type geodetic_information: str
        """
        self.openapi_types = {
            'location_number': str,
            'cgi': CellGlobalId,
            'rai': RoutingAreaId,
            'sai': ServiceAreaId,
            'lai': LocationAreaId,
            'vlr_number': str,
            'msc_number': str,
            'age_of_location_information': int,
            'ue_location_timestamp': datetime,
            'geographical_information': str,
            'geodetic_information': str
        }

        self.attribute_map = {
            'location_number': 'locationNumber',
            'cgi': 'cgi',
            'rai': 'rai',
            'sai': 'sai',
            'lai': 'lai',
            'vlr_number': 'vlrNumber',
            'msc_number': 'mscNumber',
            'age_of_location_information': 'ageOfLocationInformation',
            'ue_location_timestamp': 'ueLocationTimestamp',
            'geographical_information': 'geographicalInformation',
            'geodetic_information': 'geodeticInformation'
        }

        self._location_number = location_number
        self._cgi = cgi
        self._rai = rai
        self._sai = sai
        self._lai = lai
        self._vlr_number = vlr_number
        self._msc_number = msc_number
        self._age_of_location_information = age_of_location_information
        self._ue_location_timestamp = ue_location_timestamp
        self._geographical_information = geographical_information
        self._geodetic_information = geodetic_information

    @classmethod
    def from_dict(cls, dikt) -> 'GeraLocation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GeraLocation of this GeraLocation.  # noqa: E501
        :rtype: GeraLocation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def location_number(self):
        """Gets the location_number of this GeraLocation.

        Location number within the PLMN. See 3GPP TS 23.003, clause 4.5.  # noqa: E501

        :return: The location_number of this GeraLocation.
        :rtype: str
        """
        return self._location_number

    @location_number.setter
    def location_number(self, location_number):
        """Sets the location_number of this GeraLocation.

        Location number within the PLMN. See 3GPP TS 23.003, clause 4.5.  # noqa: E501

        :param location_number: The location_number of this GeraLocation.
        :type location_number: str
        """

        self._location_number = location_number

    @property
    def cgi(self):
        """Gets the cgi of this GeraLocation.


        :return: The cgi of this GeraLocation.
        :rtype: CellGlobalId
        """
        return self._cgi

    @cgi.setter
    def cgi(self, cgi):
        """Sets the cgi of this GeraLocation.


        :param cgi: The cgi of this GeraLocation.
        :type cgi: CellGlobalId
        """

        self._cgi = cgi

    @property
    def rai(self):
        """Gets the rai of this GeraLocation.


        :return: The rai of this GeraLocation.
        :rtype: RoutingAreaId
        """
        return self._rai

    @rai.setter
    def rai(self, rai):
        """Sets the rai of this GeraLocation.


        :param rai: The rai of this GeraLocation.
        :type rai: RoutingAreaId
        """

        self._rai = rai

    @property
    def sai(self):
        """Gets the sai of this GeraLocation.


        :return: The sai of this GeraLocation.
        :rtype: ServiceAreaId
        """
        return self._sai

    @sai.setter
    def sai(self, sai):
        """Sets the sai of this GeraLocation.


        :param sai: The sai of this GeraLocation.
        :type sai: ServiceAreaId
        """

        self._sai = sai

    @property
    def lai(self):
        """Gets the lai of this GeraLocation.


        :return: The lai of this GeraLocation.
        :rtype: LocationAreaId
        """
        return self._lai

    @lai.setter
    def lai(self, lai):
        """Sets the lai of this GeraLocation.


        :param lai: The lai of this GeraLocation.
        :type lai: LocationAreaId
        """

        self._lai = lai

    @property
    def vlr_number(self):
        """Gets the vlr_number of this GeraLocation.

        VLR number. See 3GPP TS 23.003 clause 5.1.  # noqa: E501

        :return: The vlr_number of this GeraLocation.
        :rtype: str
        """
        return self._vlr_number

    @vlr_number.setter
    def vlr_number(self, vlr_number):
        """Sets the vlr_number of this GeraLocation.

        VLR number. See 3GPP TS 23.003 clause 5.1.  # noqa: E501

        :param vlr_number: The vlr_number of this GeraLocation.
        :type vlr_number: str
        """

        self._vlr_number = vlr_number

    @property
    def msc_number(self):
        """Gets the msc_number of this GeraLocation.

        MSC number. See 3GPP TS 23.003 clause 5.1.  # noqa: E501

        :return: The msc_number of this GeraLocation.
        :rtype: str
        """
        return self._msc_number

    @msc_number.setter
    def msc_number(self, msc_number):
        """Sets the msc_number of this GeraLocation.

        MSC number. See 3GPP TS 23.003 clause 5.1.  # noqa: E501

        :param msc_number: The msc_number of this GeraLocation.
        :type msc_number: str
        """

        self._msc_number = msc_number

    @property
    def age_of_location_information(self):
        """Gets the age_of_location_information of this GeraLocation.

        The value represents the elapsed time in minutes since the last network contact of the mobile station.  Value \"0\" indicates that the location information was obtained after a successful paging procedure for Active Location Retrieval when the UE is in idle mode or after a successful location reporting procedure the UE is in connected mode.Any other value than \"0\" indicates that the location information is the last known one.See 3GPP TS 29.002 clause 17.7.8.  # noqa: E501

        :return: The age_of_location_information of this GeraLocation.
        :rtype: int
        """
        return self._age_of_location_information

    @age_of_location_information.setter
    def age_of_location_information(self, age_of_location_information):
        """Sets the age_of_location_information of this GeraLocation.

        The value represents the elapsed time in minutes since the last network contact of the mobile station.  Value \"0\" indicates that the location information was obtained after a successful paging procedure for Active Location Retrieval when the UE is in idle mode or after a successful location reporting procedure the UE is in connected mode.Any other value than \"0\" indicates that the location information is the last known one.See 3GPP TS 29.002 clause 17.7.8.  # noqa: E501

        :param age_of_location_information: The age_of_location_information of this GeraLocation.
        :type age_of_location_information: int
        """
        if age_of_location_information is not None and age_of_location_information > 32767:  # noqa: E501
            raise ValueError("Invalid value for `age_of_location_information`, must be a value less than or equal to `32767`")  # noqa: E501
        if age_of_location_information is not None and age_of_location_information < 0:  # noqa: E501
            raise ValueError("Invalid value for `age_of_location_information`, must be a value greater than or equal to `0`")  # noqa: E501

        self._age_of_location_information = age_of_location_information

    @property
    def ue_location_timestamp(self):
        """Gets the ue_location_timestamp of this GeraLocation.

        string with format \"date-time\" as defined in OpenAPI.  # noqa: E501

        :return: The ue_location_timestamp of this GeraLocation.
        :rtype: datetime
        """
        return self._ue_location_timestamp

    @ue_location_timestamp.setter
    def ue_location_timestamp(self, ue_location_timestamp):
        """Sets the ue_location_timestamp of this GeraLocation.

        string with format \"date-time\" as defined in OpenAPI.  # noqa: E501

        :param ue_location_timestamp: The ue_location_timestamp of this GeraLocation.
        :type ue_location_timestamp: datetime
        """

        self._ue_location_timestamp = ue_location_timestamp

    @property
    def geographical_information(self):
        """Gets the geographical_information of this GeraLocation.

        Refer to geographical Information.See 3GPP TS 23.032 clause 7.3.2. Only the description of an ellipsoid point with uncertainty circle is allowed to be used.  # noqa: E501

        :return: The geographical_information of this GeraLocation.
        :rtype: str
        """
        return self._geographical_information

    @geographical_information.setter
    def geographical_information(self, geographical_information):
        """Sets the geographical_information of this GeraLocation.

        Refer to geographical Information.See 3GPP TS 23.032 clause 7.3.2. Only the description of an ellipsoid point with uncertainty circle is allowed to be used.  # noqa: E501

        :param geographical_information: The geographical_information of this GeraLocation.
        :type geographical_information: str
        """
        if geographical_information is not None and not re.search(r'^[0-9A-F]{16}$', geographical_information):  # noqa: E501
            raise ValueError("Invalid value for `geographical_information`, must be a follow pattern or equal to `/^[0-9A-F]{16}$/`")  # noqa: E501

        self._geographical_information = geographical_information

    @property
    def geodetic_information(self):
        """Gets the geodetic_information of this GeraLocation.

        Refers to Calling Geodetic Location.See ITU-T Recommendation Q.763 (1999) clause 3.88.2. Only the description of an ellipsoid point with uncertainty circle is allowed to be used.  # noqa: E501

        :return: The geodetic_information of this GeraLocation.
        :rtype: str
        """
        return self._geodetic_information

    @geodetic_information.setter
    def geodetic_information(self, geodetic_information):
        """Sets the geodetic_information of this GeraLocation.

        Refers to Calling Geodetic Location.See ITU-T Recommendation Q.763 (1999) clause 3.88.2. Only the description of an ellipsoid point with uncertainty circle is allowed to be used.  # noqa: E501

        :param geodetic_information: The geodetic_information of this GeraLocation.
        :type geodetic_information: str
        """
        if geodetic_information is not None and not re.search(r'^[0-9A-F]{20}$', geodetic_information):  # noqa: E501
            raise ValueError("Invalid value for `geodetic_information`, must be a follow pattern or equal to `/^[0-9A-F]{20}$/`")  # noqa: E501

        self._geodetic_information = geodetic_information