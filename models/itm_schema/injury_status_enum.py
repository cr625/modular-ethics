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


class InjuryStatusEnum(str, Enum):
    """
    Whether the injury is known prior- and post-assessment, and to what extent it's been treated
    """

    """
    allowed enum values
    """
    HIDDEN = 'hidden'
    DISCOVERABLE = 'discoverable'
    VISIBLE = 'visible'
    DISCOVERED = 'discovered'
    PARTIALLY_TREATED = 'partially treated'
    TREATED = 'treated'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of InjuryStatusEnum from a JSON string"""
        return cls(json.loads(json_str))


