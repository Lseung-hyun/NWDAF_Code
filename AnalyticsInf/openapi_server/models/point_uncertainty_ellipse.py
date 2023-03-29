# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.gad_shape import GADShape
from openapi_server.models.geographical_coordinates import GeographicalCoordinates
from openapi_server.models.point_uncertainty_ellipse_all_of import PointUncertaintyEllipseAllOf
from openapi_server.models.supported_gad_shapes import SupportedGADShapes
from openapi_server.models.uncertainty_ellipse import UncertaintyEllipse
from openapi_server import util

from openapi_server.models.gad_shape import GADShape  # noqa: E501
from openapi_server.models.geographical_coordinates import GeographicalCoordinates  # noqa: E501
from openapi_server.models.point_uncertainty_ellipse_all_of import PointUncertaintyEllipseAllOf  # noqa: E501
from openapi_server.models.supported_gad_shapes import SupportedGADShapes  # noqa: E501
from openapi_server.models.uncertainty_ellipse import UncertaintyEllipse  # noqa: E501

class PointUncertaintyEllipse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, shape=None, point=None, uncertainty_ellipse=None, confidence=None):  # noqa: E501
        """PointUncertaintyEllipse - a model defined in OpenAPI

        :param shape: The shape of this PointUncertaintyEllipse.  # noqa: E501
        :type shape: SupportedGADShapes
        :param point: The point of this PointUncertaintyEllipse.  # noqa: E501
        :type point: GeographicalCoordinates
        :param uncertainty_ellipse: The uncertainty_ellipse of this PointUncertaintyEllipse.  # noqa: E501
        :type uncertainty_ellipse: UncertaintyEllipse
        :param confidence: The confidence of this PointUncertaintyEllipse.  # noqa: E501
        :type confidence: int
        """
        self.openapi_types = {
            'shape': SupportedGADShapes,
            'point': GeographicalCoordinates,
            'uncertainty_ellipse': UncertaintyEllipse,
            'confidence': int
        }

        self.attribute_map = {
            'shape': 'shape',
            'point': 'point',
            'uncertainty_ellipse': 'uncertaintyEllipse',
            'confidence': 'confidence'
        }

        self._shape = shape
        self._point = point
        self._uncertainty_ellipse = uncertainty_ellipse
        self._confidence = confidence

    @classmethod
    def from_dict(cls, dikt) -> 'PointUncertaintyEllipse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PointUncertaintyEllipse of this PointUncertaintyEllipse.  # noqa: E501
        :rtype: PointUncertaintyEllipse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def shape(self):
        """Gets the shape of this PointUncertaintyEllipse.


        :return: The shape of this PointUncertaintyEllipse.
        :rtype: SupportedGADShapes
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Sets the shape of this PointUncertaintyEllipse.


        :param shape: The shape of this PointUncertaintyEllipse.
        :type shape: SupportedGADShapes
        """
        if shape is None:
            raise ValueError("Invalid value for `shape`, must not be `None`")  # noqa: E501

        self._shape = shape

    @property
    def point(self):
        """Gets the point of this PointUncertaintyEllipse.


        :return: The point of this PointUncertaintyEllipse.
        :rtype: GeographicalCoordinates
        """
        return self._point

    @point.setter
    def point(self, point):
        """Sets the point of this PointUncertaintyEllipse.


        :param point: The point of this PointUncertaintyEllipse.
        :type point: GeographicalCoordinates
        """
        if point is None:
            raise ValueError("Invalid value for `point`, must not be `None`")  # noqa: E501

        self._point = point

    @property
    def uncertainty_ellipse(self):
        """Gets the uncertainty_ellipse of this PointUncertaintyEllipse.


        :return: The uncertainty_ellipse of this PointUncertaintyEllipse.
        :rtype: UncertaintyEllipse
        """
        return self._uncertainty_ellipse

    @uncertainty_ellipse.setter
    def uncertainty_ellipse(self, uncertainty_ellipse):
        """Sets the uncertainty_ellipse of this PointUncertaintyEllipse.


        :param uncertainty_ellipse: The uncertainty_ellipse of this PointUncertaintyEllipse.
        :type uncertainty_ellipse: UncertaintyEllipse
        """
        if uncertainty_ellipse is None:
            raise ValueError("Invalid value for `uncertainty_ellipse`, must not be `None`")  # noqa: E501

        self._uncertainty_ellipse = uncertainty_ellipse

    @property
    def confidence(self):
        """Gets the confidence of this PointUncertaintyEllipse.

        Indicates value of confidence.  # noqa: E501

        :return: The confidence of this PointUncertaintyEllipse.
        :rtype: int
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this PointUncertaintyEllipse.

        Indicates value of confidence.  # noqa: E501

        :param confidence: The confidence of this PointUncertaintyEllipse.
        :type confidence: int
        """
        if confidence is None:
            raise ValueError("Invalid value for `confidence`, must not be `None`")  # noqa: E501
        if confidence is not None and confidence > 100:  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must be a value less than or equal to `100`")  # noqa: E501
        if confidence is not None and confidence < 0:  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must be a value greater than or equal to `0`")  # noqa: E501

        self._confidence = confidence
