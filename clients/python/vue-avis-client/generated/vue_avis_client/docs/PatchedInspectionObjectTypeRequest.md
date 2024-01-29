# PatchedInspectionObjectTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | [optional] 
**instances** | **List[int]** |  | [optional] 
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from vue_avis_client.models.patched_inspection_object_type_request import PatchedInspectionObjectTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedInspectionObjectTypeRequest from a JSON string
patched_inspection_object_type_request_instance = PatchedInspectionObjectTypeRequest.from_json(json)
# print the JSON string representation of the object
print PatchedInspectionObjectTypeRequest.to_json()

# convert the object into a dict
patched_inspection_object_type_request_dict = patched_inspection_object_type_request_instance.to_dict()
# create an instance of PatchedInspectionObjectTypeRequest from a dict
patched_inspection_object_type_request_form_dict = patched_inspection_object_type_request.from_dict(patched_inspection_object_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


