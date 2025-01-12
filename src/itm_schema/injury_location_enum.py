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


class InjuryLocationEnum(str, Enum):
    """
    the injury location on the character's body
    """

    """
    allowed enum values
    """
    RIGHT_FOREARM = 'right forearm'
    LEFT_FOREARM = 'left forearm'
    RIGHT_HAND = 'right hand'
    LEFT_HAND = 'left hand'
    RIGHT_LEG = 'right leg'
    LEFT_LEG = 'left leg'
    RIGHT_CALF = 'right calf'
    LEFT_CALF = 'left calf'
    RIGHT_THIGH = 'right thigh'
    LEFT_THIGH = 'left thigh'
    RIGHT_STOMACH = 'right stomach'
    LEFT_STOMACH = 'left stomach'
    RIGHT_BICEP = 'right bicep'
    LEFT_BICEP = 'left bicep'
    RIGHT_SHOULDER = 'right shoulder'
    LEFT_SHOULDER = 'left shoulder'
    RIGHT_SIDE = 'right side'
    LEFT_SIDE = 'left side'
    RIGHT_CHEST = 'right chest'
    LEFT_CHEST = 'left chest'
    CENTER_CHEST = 'center chest'
    RIGHT_WRIST = 'right wrist'
    LEFT_WRIST = 'left wrist'
    LEFT_FACE = 'left face'
    RIGHT_FACE = 'right face'
    LEFT_NECK = 'left neck'
    RIGHT_NECK = 'right neck'
    INTERNAL = 'internal'
    HEAD = 'head'
    NECK = 'neck'
    STOMACH = 'stomach'
    UNSPECIFIED = 'unspecified'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of InjuryLocationEnum from a JSON string"""
        return cls(json.loads(json_str))


