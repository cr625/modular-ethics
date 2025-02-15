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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from .character import Character
from .environment import Environment
from .event import Event
from .meta_info import MetaInfo
from .mission import Mission
from .supplies import Supplies
from .threat_state import ThreatState
from typing import Optional, Set
from typing_extensions import Self

class State(BaseModel):
    """
    the current tactical & environmental state of the scenario and of its characters
    """ # noqa: E501
    unstructured: StrictStr = Field(description="Natural language, plain text description of a scene's state")
    elapsed_time: Optional[StrictInt] = Field(default=None, description="The simulated elapsed time (in seconds) since the scenario started")
    meta_info: Optional[MetaInfo] = None
    scenario_complete: Optional[StrictBool] = Field(default=None, description="set to true if the scenario is complete; subsequent calls involving that scenario will return an error code")
    mission: Optional[Mission] = None
    environment: Environment
    threat_state: Optional[ThreatState] = None
    events: Optional[List[Event]] = Field(default=None, description="A list of scenario events to inform decision-making")
    supplies: List[Supplies] = Field(description="A list of supplies available to the medic")
    characters: List[Character] = Field(description="A list of characters in the scene, including injured patients, civilians, medics, etc.")
    __properties: ClassVar[List[str]] = ["unstructured", "elapsed_time", "meta_info", "scenario_complete", "mission", "environment", "threat_state", "events", "supplies", "characters"]

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
        """Create an instance of State from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of meta_info
        if self.meta_info:
            _dict['meta_info'] = self.meta_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mission
        if self.mission:
            _dict['mission'] = self.mission.to_dict()
        # override the default output from pydantic by calling `to_dict()` of environment
        if self.environment:
            _dict['environment'] = self.environment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of threat_state
        if self.threat_state:
            _dict['threat_state'] = self.threat_state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in events (list)
        _items = []
        if self.events:
            for _item_events in self.events:
                if _item_events:
                    _items.append(_item_events.to_dict())
            _dict['events'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in supplies (list)
        _items = []
        if self.supplies:
            for _item_supplies in self.supplies:
                if _item_supplies:
                    _items.append(_item_supplies.to_dict())
            _dict['supplies'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in characters (list)
        _items = []
        if self.characters:
            for _item_characters in self.characters:
                if _item_characters:
                    _items.append(_item_characters.to_dict())
            _dict['characters'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of State from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "unstructured": obj.get("unstructured"),
            "elapsed_time": obj.get("elapsed_time"),
            "meta_info": MetaInfo.from_dict(obj["meta_info"]) if obj.get("meta_info") is not None else None,
            "scenario_complete": obj.get("scenario_complete"),
            "mission": Mission.from_dict(obj["mission"]) if obj.get("mission") is not None else None,
            "environment": Environment.from_dict(obj["environment"]) if obj.get("environment") is not None else None,
            "threat_state": ThreatState.from_dict(obj["threat_state"]) if obj.get("threat_state") is not None else None,
            "events": [Event.from_dict(_item) for _item in obj["events"]] if obj.get("events") is not None else None,
            "supplies": [Supplies.from_dict(_item) for _item in obj["supplies"]] if obj.get("supplies") is not None else None,
            "characters": [Character.from_dict(_item) for _item in obj["characters"]] if obj.get("characters") is not None else None
        })
        return _obj


