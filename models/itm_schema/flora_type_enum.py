# coding: utf-8

"""
    ITM TA3 API

    This is the specification of the TA3 API for In The Moment (ITM).  Currently, the Evaluation API for TA2 supports functionality for the Phase 1 Evaluation.  The API is based on the OpenAPI 3.0.3 specification.

    The version of the OpenAPI document: 0.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class FloraTypeEnum(str, Enum):
    """
    Descriptor of local vegetation.
    """

    """
    allowed enum values
    """
    NONE = 'none'
    LIMITED = 'limited'
    NORMAL = 'normal'
    LUSH = 'lush'
    EXTENSIVE = 'extensive'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FloraTypeEnum from a JSON string"""
        return cls(json.loads(json_str))


