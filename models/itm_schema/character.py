# coding: utf-8

"""
    ITM TA3 API

    This is the specification of the TA3 API for In The Moment (ITM).  Currently, the Evaluation API for TA2 supports functionality for the Phase 1 Evaluation.  The API is based on the OpenAPI 3.0.3 specification.

    The version of the OpenAPI document: 0.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from .character_tag_enum import CharacterTagEnum
from .demographics import Demographics
from .directness_enum import DirectnessEnum
from .injury import Injury
from .intent_enum import IntentEnum
from .rapport_enum import RapportEnum
from .vitals import Vitals
from typing import Optional, Set
from typing_extensions import Self

class Character(BaseModel):
    """
    a character in the scene, including injured patients, civilians, medics, etc.
    """ # noqa: E501
    id: StrictStr = Field(description="A unique character ID throughout the scenario")
    name: StrictStr = Field(description="display name, as in a dashboard")
    unstructured: StrictStr = Field(description="Natural language, plain text description of the character")
    unstructured_postassess: Optional[StrictStr] = Field(default=None, description="unstructured description updated after character assessment")
    has_blanket: Optional[StrictBool] = Field(default=False, description="whether or not this character has a blanket (either wrapped around or underneath)")
    unseen: Optional[StrictBool] = Field(default=False, description="whether or not this character is visible in the scene or merely heard or reported about from a nearby location")
    intent: Optional[IntentEnum] = None
    directness_of_causality: Optional[DirectnessEnum] = None
    rapport: Optional[RapportEnum] = None
    demographics: Demographics
    injuries: Optional[List[Injury]] = Field(default=None, description="A list of Injuries for the character")
    vitals: Optional[Vitals] = None
    visited: Optional[StrictBool] = Field(default=False, description="whether or not this character has been visited by the ADM in the current scenario")
    tag: Optional[CharacterTagEnum] = None
    __properties: ClassVar[List[str]] = ["id", "name", "unstructured", "unstructured_postassess", "has_blanket", "unseen", "intent", "directness_of_causality", "rapport", "demographics", "injuries", "vitals", "visited", "tag"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Character from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of demographics
        if self.demographics:
            _dict['demographics'] = self.demographics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in injuries (list)
        _items = []
        if self.injuries:
            for _item_injuries in self.injuries:
                if _item_injuries:
                    _items.append(_item_injuries.to_dict())
            _dict['injuries'] = _items
        # override the default output from pydantic by calling `to_dict()` of vitals
        if self.vitals:
            _dict['vitals'] = self.vitals.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Character from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "unstructured": obj.get("unstructured"),
            "unstructured_postassess": obj.get("unstructured_postassess"),
            "has_blanket": obj.get("has_blanket") if obj.get("has_blanket") is not None else False,
            "unseen": obj.get("unseen") if obj.get("unseen") is not None else False,
            "intent": obj.get("intent"),
            "directness_of_causality": obj.get("directness_of_causality"),
            "rapport": obj.get("rapport"),
            "demographics": Demographics.from_dict(obj["demographics"]) if obj.get("demographics") is not None else None,
            "injuries": [Injury.from_dict(_item) for _item in obj["injuries"]] if obj.get("injuries") is not None else None,
            "vitals": Vitals.from_dict(obj["vitals"]) if obj.get("vitals") is not None else None,
            "visited": obj.get("visited") if obj.get("visited") is not None else False,
            "tag": obj.get("tag")
        })
        return _obj


