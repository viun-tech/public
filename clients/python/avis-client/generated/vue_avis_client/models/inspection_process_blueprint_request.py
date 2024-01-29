# coding: utf-8

"""
    avis

    VUE Autonomous Visual Inspection System (AVIS)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class InspectionProcessBlueprintRequest(BaseModel):
    """
    InspectionProcessBlueprintRequest
    """ # noqa: E501
    team: StrictInt
    name: Annotated[str, Field(min_length=1, strict=True)]
    metadata_schema: Optional[StrictInt] = None
    image_quality_gate: Optional[StrictInt] = None
    ml_model: Optional[StrictInt] = None
    inspection_object_type: Optional[StrictInt] = None
    description: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["team", "name", "metadata_schema", "image_quality_gate", "ml_model", "inspection_object_type", "description"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of InspectionProcessBlueprintRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if metadata_schema (nullable) is None
        # and model_fields_set contains the field
        if self.metadata_schema is None and "metadata_schema" in self.model_fields_set:
            _dict['metadata_schema'] = None

        # set to None if image_quality_gate (nullable) is None
        # and model_fields_set contains the field
        if self.image_quality_gate is None and "image_quality_gate" in self.model_fields_set:
            _dict['image_quality_gate'] = None

        # set to None if ml_model (nullable) is None
        # and model_fields_set contains the field
        if self.ml_model is None and "ml_model" in self.model_fields_set:
            _dict['ml_model'] = None

        # set to None if inspection_object_type (nullable) is None
        # and model_fields_set contains the field
        if self.inspection_object_type is None and "inspection_object_type" in self.model_fields_set:
            _dict['inspection_object_type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of InspectionProcessBlueprintRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "team": obj.get("team"),
            "name": obj.get("name"),
            "metadata_schema": obj.get("metadata_schema"),
            "image_quality_gate": obj.get("image_quality_gate"),
            "ml_model": obj.get("ml_model"),
            "inspection_object_type": obj.get("inspection_object_type"),
            "description": obj.get("description")
        })
        return _obj


