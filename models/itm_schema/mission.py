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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from .civilian_presence_enum import CivilianPresenceEnum
from .communication_capability_enum import CommunicationCapabilityEnum
from .medical_policies_enum import MedicalPoliciesEnum
from .mission_importance_enum import MissionImportanceEnum
from .mission_type_enum import MissionTypeEnum
from typing import Optional, Set
from typing_extensions import Self

class Mission(BaseModel):
    """
    Mission parameters that impact decision-making
    """ # noqa: E501
    unstructured: StrictStr = Field(description="natural language description of current mission")
    mission_type: MissionTypeEnum
    character_importance: Optional[List[Dict[str, MissionImportanceEnum]]] = Field(default=None, description="A list of pairs of character ids with an indicator of how mission-critical the character is")
    civilian_presence: Optional[CivilianPresenceEnum] = None
    communication_capability: Optional[CommunicationCapabilityEnum] = CommunicationCapabilityEnum.BOTH
    roe: Optional[StrictStr] = Field(default=None, description="rules of engagement to inform decision-making, but not to restrict decision space")
    political_climate: Optional[StrictStr] = Field(default=None, description="The political climate in a mission to inform decision-making")
    medical_policies: Optional[List[MedicalPoliciesEnum]] = Field(default=None, description="A list of medical policies; omit this property if no special policy is in place")
    __properties: ClassVar[List[str]] = ["unstructured", "mission_type", "character_importance", "civilian_presence", "communication_capability", "roe", "political_climate", "medical_policies"]

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
        """Create an instance of Mission from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in character_importance (list)
        _items = []
        if self.character_importance:
            for _item_character_importance in self.character_importance:
                if _item_character_importance:
                    _items.append(_item_character_importance.to_dict())
            _dict['character_importance'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Mission from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "unstructured": obj.get("unstructured"),
            "mission_type": obj.get("mission_type"),
            "character_importance": [Dict[str, MissionImportanceEnum].from_dict(_item) for _item in obj["character_importance"]] if obj.get("character_importance") is not None else None,
            "civilian_presence": obj.get("civilian_presence"),
            "communication_capability": obj.get("communication_capability") if obj.get("communication_capability") is not None else CommunicationCapabilityEnum.BOTH,
            "roe": obj.get("roe"),
            "political_climate": obj.get("political_climate"),
            "medical_policies": obj.get("medical_policies")
        })
        return _obj


