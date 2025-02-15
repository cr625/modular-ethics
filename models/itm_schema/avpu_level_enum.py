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


class AvpuLevelEnum(str, Enum):
    """
    Character level of response; anything but ALERT is considered unconscious.  See [Levels of Response](https://www.firstresponse.org.uk/first-aid-az/3-general/first-aid/79-levels-of-response) for details
    """

    """
    allowed enum values
    """
    ALERT = 'ALERT'
    VOICE = 'VOICE'
    PAIN = 'PAIN'
    UNRESPONSIVE = 'UNRESPONSIVE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AvpuLevelEnum from a JSON string"""
        return cls(json.loads(json_str))


