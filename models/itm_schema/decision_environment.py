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
from .aid import Aid
from .air_quality_enum import AirQualityEnum
from .injury_trigger_enum import InjuryTriggerEnum
from .movement_restriction_enum import MovementRestrictionEnum
from .oxygen_levels_enum import OxygenLevelsEnum
from .population_density_enum import PopulationDensityEnum
from .sound_restriction_enum import SoundRestrictionEnum
from typing import Optional, Set
from typing_extensions import Self

class DecisionEnvironment(BaseModel):
    """
    Environmental elements that impact decision-making
    """ # noqa: E501
    unstructured: StrictStr = Field(description="Natural language, plain text description of decision-impacting environmental factors")
    aid: Optional[List[Aid]] = Field(default=None, description="A list of available forms of aid")
    movement_restriction: Optional[MovementRestrictionEnum] = None
    sound_restriction: Optional[SoundRestrictionEnum] = None
    oxygen_levels: Optional[OxygenLevelsEnum] = None
    population_density: Optional[PopulationDensityEnum] = None
    injury_triggers: Optional[InjuryTriggerEnum] = None
    air_quality: Optional[AirQualityEnum] = None
    city_infrastructure: Optional[StrictStr] = Field(default=None, description="Refers to building/city infrastructure that should be noted and known (safe house, etc.)")
    __properties: ClassVar[List[str]] = ["unstructured", "aid", "movement_restriction", "sound_restriction", "oxygen_levels", "population_density", "injury_triggers", "air_quality", "city_infrastructure"]

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
        """Create an instance of DecisionEnvironment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in aid (list)
        _items = []
        if self.aid:
            for _item_aid in self.aid:
                if _item_aid:
                    _items.append(_item_aid.to_dict())
            _dict['aid'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DecisionEnvironment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "unstructured": obj.get("unstructured"),
            "aid": [Aid.from_dict(_item) for _item in obj["aid"]] if obj.get("aid") is not None else None,
            "movement_restriction": obj.get("movement_restriction"),
            "sound_restriction": obj.get("sound_restriction"),
            "oxygen_levels": obj.get("oxygen_levels"),
            "population_density": obj.get("population_density"),
            "injury_triggers": obj.get("injury_triggers"),
            "air_quality": obj.get("air_quality"),
            "city_infrastructure": obj.get("city_infrastructure")
        })
        return _obj


