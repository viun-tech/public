# coding: utf-8

"""
    avis

    VUE Autonomous Visual Inspection System (AVIS)

    The version of the OpenAPI document: 0.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from avis_client.models.patched_result_request_status import PatchedResultRequestStatus

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class PatchedResultRequest(BaseModel):
    """
    PatchedResultRequest
    """  # noqa: E501

    team: Optional[StrictInt] = None
    reported_by: Optional[StrictInt] = None
    inferred_by: Optional[StrictInt] = None
    image: Optional[StrictInt] = None
    image_attributes: Optional[List[StrictInt]] = None
    status: Optional[PatchedResultRequestStatus] = None
    failure_reason: Optional[StrictStr] = None
    comment: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = [
        "team",
        "reported_by",
        "inferred_by",
        "image",
        "image_attributes",
        "status",
        "failure_reason",
        "comment",
    ]

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
        """Create an instance of PatchedResultRequest from a JSON string"""
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
            exclude={},
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict["status"] = self.status.to_dict()
        # set to None if reported_by (nullable) is None
        # and model_fields_set contains the field
        if self.reported_by is None and "reported_by" in self.model_fields_set:
            _dict["reported_by"] = None

        # set to None if inferred_by (nullable) is None
        # and model_fields_set contains the field
        if self.inferred_by is None and "inferred_by" in self.model_fields_set:
            _dict["inferred_by"] = None

        # set to None if image (nullable) is None
        # and model_fields_set contains the field
        if self.image is None and "image" in self.model_fields_set:
            _dict["image"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PatchedResultRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "team": obj.get("team"),
                "reported_by": obj.get("reported_by"),
                "inferred_by": obj.get("inferred_by"),
                "image": obj.get("image"),
                "image_attributes": obj.get("image_attributes"),
                "status": PatchedResultRequestStatus.from_dict(obj.get("status"))
                if obj.get("status") is not None
                else None,
                "failure_reason": obj.get("failure_reason"),
                "comment": obj.get("comment"),
            }
        )
        return _obj
