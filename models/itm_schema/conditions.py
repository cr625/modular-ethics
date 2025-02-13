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
from typing_extensions import Annotated
from .conditions_character_vitals_inner import ConditionsCharacterVitalsInner
from .supplies import Supplies
from typing import Optional, Set
from typing_extensions import Self

class Conditions(BaseModel):
    """
    Conditions that specify whether to transition to the next scene or send a probe response
    """ # noqa: E501
    elapsed_time_lt: Optional[Annotated[int, Field(strict=True, ge=5)]] = Field(default=None, description="True if the scenario elapsed time (in seconds) is less than the specified value")
    elapsed_time_gt: Optional[Annotated[int, Field(strict=True, ge=5)]] = Field(default=None, description="True if the scenario elapsed time (in seconds) is greater than the specified value")
    actions: Optional[List[List[StrictStr]]] = Field(default=None, description="True if any of the specified lists of actions have been taken; multiple action ID lists have \"or\" semantics; multiple action IDs within a list have \"and\" semantics")
    probes: Optional[List[StrictStr]] = Field(default=None, description="True if the specified list of probe_ids have been answered")
    probe_responses: Optional[List[StrictStr]] = Field(default=None, description="True if the specified list of probe responses (choice) have been sent")
    character_vitals: Optional[List[ConditionsCharacterVitalsInner]] = Field(default=None, description="True if any of the specified collection of vital values have been met for the specified character_id")
    supplies: Optional[List[Supplies]] = Field(default=None, description="True if any of the specified supplies reach or go below the specified quantity")
    __properties: ClassVar[List[str]] = ["elapsed_time_lt", "elapsed_time_gt", "actions", "probes", "probe_responses", "character_vitals", "supplies"]

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
        """Create an instance of Conditions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in character_vitals (list)
        _items = []
        if self.character_vitals:
            for _item_character_vitals in self.character_vitals:
                if _item_character_vitals:
                    _items.append(_item_character_vitals.to_dict())
            _dict['character_vitals'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in supplies (list)
        _items = []
        if self.supplies:
            for _item_supplies in self.supplies:
                if _item_supplies:
                    _items.append(_item_supplies.to_dict())
            _dict['supplies'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Conditions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "elapsed_time_lt": obj.get("elapsed_time_lt"),
            "elapsed_time_gt": obj.get("elapsed_time_gt"),
            "actions": obj.get("actions"),
            "probes": obj.get("probes"),
            "probe_responses": obj.get("probe_responses"),
            "character_vitals": [ConditionsCharacterVitalsInner.from_dict(_item) for _item in obj["character_vitals"]] if obj.get("character_vitals") is not None else None,
            "supplies": [Supplies.from_dict(_item) for _item in obj["supplies"]] if obj.get("supplies") is not None else None
        })
        return _obj


