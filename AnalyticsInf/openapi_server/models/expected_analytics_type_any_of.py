# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ExpectedAnalyticsTypeAnyOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    MOBILITY = "MOBILITY"
    COMMUN = "COMMUN"
    MOBILITY_AND_COMMUN = "MOBILITY_AND_COMMUN"
    def __init__(self):  # noqa: E501
        """ExpectedAnalyticsTypeAnyOf - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'ExpectedAnalyticsTypeAnyOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExpectedAnalyticsType_anyOf of this ExpectedAnalyticsTypeAnyOf.  # noqa: E501
        :rtype: ExpectedAnalyticsTypeAnyOf
        """
        return util.deserialize_model(dikt, cls)