# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.plmn_id import PlmnId
import re
from openapi_server import util

from openapi_server.models.plmn_id import PlmnId  # noqa: E501
import re  # noqa: E501

class RoutingAreaId(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, plmn_id=None, lac=None, rac=None):  # noqa: E501
        """RoutingAreaId - a model defined in OpenAPI

        :param plmn_id: The plmn_id of this RoutingAreaId.  # noqa: E501
        :type plmn_id: PlmnId
        :param lac: The lac of this RoutingAreaId.  # noqa: E501
        :type lac: str
        :param rac: The rac of this RoutingAreaId.  # noqa: E501
        :type rac: str
        """
        self.openapi_types = {
            'plmn_id': PlmnId,
            'lac': str,
            'rac': str
        }

        self.attribute_map = {
            'plmn_id': 'plmnId',
            'lac': 'lac',
            'rac': 'rac'
        }

        self._plmn_id = plmn_id
        self._lac = lac
        self._rac = rac

    @classmethod
    def from_dict(cls, dikt) -> 'RoutingAreaId':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RoutingAreaId of this RoutingAreaId.  # noqa: E501
        :rtype: RoutingAreaId
        """
        return util.deserialize_model(dikt, cls)

    @property
    def plmn_id(self):
        """Gets the plmn_id of this RoutingAreaId.


        :return: The plmn_id of this RoutingAreaId.
        :rtype: PlmnId
        """
        return self._plmn_id

    @plmn_id.setter
    def plmn_id(self, plmn_id):
        """Sets the plmn_id of this RoutingAreaId.


        :param plmn_id: The plmn_id of this RoutingAreaId.
        :type plmn_id: PlmnId
        """
        if plmn_id is None:
            raise ValueError("Invalid value for `plmn_id`, must not be `None`")  # noqa: E501

        self._plmn_id = plmn_id

    @property
    def lac(self):
        """Gets the lac of this RoutingAreaId.

        Location Area Code  # noqa: E501

        :return: The lac of this RoutingAreaId.
        :rtype: str
        """
        return self._lac

    @lac.setter
    def lac(self, lac):
        """Sets the lac of this RoutingAreaId.

        Location Area Code  # noqa: E501

        :param lac: The lac of this RoutingAreaId.
        :type lac: str
        """
        if lac is None:
            raise ValueError("Invalid value for `lac`, must not be `None`")  # noqa: E501
        if lac is not None and not re.search(r'^[A-Fa-f0-9]{4}$', lac):  # noqa: E501
            raise ValueError("Invalid value for `lac`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{4}$/`")  # noqa: E501

        self._lac = lac

    @property
    def rac(self):
        """Gets the rac of this RoutingAreaId.

        Routing Area Code  # noqa: E501

        :return: The rac of this RoutingAreaId.
        :rtype: str
        """
        return self._rac

    @rac.setter
    def rac(self, rac):
        """Sets the rac of this RoutingAreaId.

        Routing Area Code  # noqa: E501

        :param rac: The rac of this RoutingAreaId.
        :type rac: str
        """
        if rac is None:
            raise ValueError("Invalid value for `rac`, must not be `None`")  # noqa: E501
        if rac is not None and not re.search(r'^[A-Fa-f0-9]{2}$', rac):  # noqa: E501
            raise ValueError("Invalid value for `rac`, must be a follow pattern or equal to `/^[A-Fa-f0-9]{2}$/`")  # noqa: E501

        self._rac = rac