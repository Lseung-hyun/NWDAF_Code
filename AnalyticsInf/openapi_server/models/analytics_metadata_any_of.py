# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class AnalyticsMetadataAnyOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    NUM_OF_SAMPLES = "NUM_OF_SAMPLES"
    DATA_WINDOW = "DATA_WINDOW"
    DATA_STAT_PROPS = "DATA_STAT_PROPS"
    STRATEGY = "STRATEGY"
    ACCURACY = "ACCURACY"
    def __init__(self):  # noqa: E501
        """AnalyticsMetadataAnyOf - a model defined in OpenAPI

        """
        self.openapi_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'AnalyticsMetadataAnyOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AnalyticsMetadata_anyOf of this AnalyticsMetadataAnyOf.  # noqa: E501
        :rtype: AnalyticsMetadataAnyOf
        """
        return util.deserialize_model(dikt, cls)
