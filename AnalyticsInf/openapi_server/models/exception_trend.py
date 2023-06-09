# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.exception_trend_any_of import ExceptionTrendAnyOf
from openapi_server import util

from openapi_server.models.exception_trend_any_of import ExceptionTrendAnyOf  # noqa: E501

class ExceptionTrend(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self):  # noqa: E501
        """ExceptionTrend - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'ExceptionTrend':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ExceptionTrend of this ExceptionTrend.  # noqa: E501
        :rtype: ExceptionTrend
        """
        return util.deserialize_model(dikt, cls)
