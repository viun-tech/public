# coding: utf-8

"""
    avis

    VUE Autonomous Visual Inspection System (AVIS)

    The version of the OpenAPI document: 0.7.0
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

class PatchedConfigurationTypeRequest(BaseModel):
    """
    PatchedConfigurationTypeRequest
    """ # noqa: E501
    team: Optional[StrictInt] = None
    name: Optional[Annotated[str, Field(min_length=1, strict=True)]] = None
    metadata_schema: Optional[StrictInt] = None
    quality_criteria: Optional[StrictInt] = None
    product_category: Optional[StrictInt] = None
    image_attribute_categories: Optional[List[StrictInt]] = None
    description: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["team", "name", "metadata_schema", "quality_criteria", "product_category", "image_attribute_categories", "description"]

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
        """Create an instance of PatchedConfigurationTypeRequest from a JSON string"""
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

        # set to None if quality_criteria (nullable) is None
        # and model_fields_set contains the field
        if self.quality_criteria is None and "quality_criteria" in self.model_fields_set:
            _dict['quality_criteria'] = None

        # set to None if product_category (nullable) is None
        # and model_fields_set contains the field
        if self.product_category is None and "product_category" in self.model_fields_set:
            _dict['product_category'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PatchedConfigurationTypeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "team": obj.get("team"),
            "name": obj.get("name"),
            "metadata_schema": obj.get("metadata_schema"),
            "quality_criteria": obj.get("quality_criteria"),
            "product_category": obj.get("product_category"),
            "image_attribute_categories": obj.get("image_attribute_categories"),
            "description": obj.get("description")
        })
        return _obj


