# PatchedInspectionProcessBlueprintRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | [optional]
**name** | **str** |  | [optional]
**metadata_schema** | **int** |  | [optional]
**image_quality_gate** | **int** |  | [optional]
**ml_model** | **int** |  | [optional]
**inspection_object_type** | **int** |  | [optional]
**description** | **str** |  | [optional]

## Example

```python
from vue_avis_client.models.patched_inspection_process_blueprint_request import PatchedInspectionProcessBlueprintRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedInspectionProcessBlueprintRequest from a JSON string
patched_inspection_process_blueprint_request_instance = PatchedInspectionProcessBlueprintRequest.from_json(json)
# print the JSON string representation of the object
print PatchedInspectionProcessBlueprintRequest.to_json()

# convert the object into a dict
patched_inspection_process_blueprint_request_dict = patched_inspection_process_blueprint_request_instance.to_dict()
# create an instance of PatchedInspectionProcessBlueprintRequest from a dict
patched_inspection_process_blueprint_request_form_dict = patched_inspection_process_blueprint_request.from_dict(patched_inspection_process_blueprint_request_dict)
```
[[Back to Model list]](..#documentation-for-models) [[Back to API list]](..#documentation-for-api-endpoints) [[Back to README]](..)
