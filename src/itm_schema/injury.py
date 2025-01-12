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
from .injury_location_enum import InjuryLocationEnum
from .injury_severity_enum import InjurySeverityEnum
from .injury_status_enum import InjuryStatusEnum
from .injury_type_enum import InjuryTypeEnum
from typing import Optional, Set
from typing_extensions import Self

class Injury(BaseModel):
    """
    An injury on a character.
    """ # noqa: E501
    name: InjuryTypeEnum
    location: InjuryLocationEnum
    severity: Optional[InjurySeverityEnum] = None
    status: InjuryStatusEnum
    source_character: Optional[StrictStr] = Field(default=None, description="The character id of the person responsible for the injury, subject to the character's `directness_of_causality`")
    treatments_required: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="The number of successful treatments required to treat the injury fully, which sets `status` to `treated`")
    treatments_applied: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=0, description="The number of successful treatments applied to the injury")
    __properties: ClassVar[List[str]] = ["name", "location", "severity", "status", "source_character", "treatments_required", "treatments_applied"]

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
        """Create an instance of Injury from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Injury from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "location": obj.get("location"),
            "severity": obj.get("severity"),
            "status": obj.get("status"),
            "source_character": obj.get("source_character"),
            "treatments_required": obj.get("treatments_required"),
            "treatments_applied": obj.get("treatments_applied") if obj.get("treatments_applied") is not None else 0
        })
        return _obj


