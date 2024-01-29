# PatchedImageQualityGateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | [optional]
**blueprints** | **List[int]** |  | [optional]
**good_quality_classes** | **List[str]** |  | [optional]
**uncertain_quality_classes** | **List[str]** |  | [optional]
**bad_quality_classes** | **List[str]** |  | [optional]

## Example

```python
from vue_avis_client.models.patched_image_quality_gate_request import PatchedImageQualityGateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedImageQualityGateRequest from a JSON string
patched_image_quality_gate_request_instance = PatchedImageQualityGateRequest.from_json(json)
# print the JSON string representation of the object
print PatchedImageQualityGateRequest.to_json()

# convert the object into a dict
patched_image_quality_gate_request_dict = patched_image_quality_gate_request_instance.to_dict()
# create an instance of PatchedImageQualityGateRequest from a dict
patched_image_quality_gate_request_form_dict = patched_image_quality_gate_request.from_dict(patched_image_quality_gate_request_dict)
```
[[Back to Model list]](..#documentation-for-models) [[Back to API list]](..#documentation-for-api-endpoints) [[Back to README]](..)
