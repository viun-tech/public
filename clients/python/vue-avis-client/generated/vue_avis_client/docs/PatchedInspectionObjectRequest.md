# PatchedInspectionObjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | [optional] 
**type** | **int** |  | [optional] 
**cases** | **List[int]** |  | [optional] 
**identifier** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from vue_avis_client.models.patched_inspection_object_request import PatchedInspectionObjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedInspectionObjectRequest from a JSON string
patched_inspection_object_request_instance = PatchedInspectionObjectRequest.from_json(json)
# print the JSON string representation of the object
print PatchedInspectionObjectRequest.to_json()

# convert the object into a dict
patched_inspection_object_request_dict = patched_inspection_object_request_instance.to_dict()
# create an instance of PatchedInspectionObjectRequest from a dict
patched_inspection_object_request_form_dict = patched_inspection_object_request.from_dict(patched_inspection_object_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


