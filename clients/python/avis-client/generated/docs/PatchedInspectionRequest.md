# PatchedInspectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | [optional] 
**product** | **int** |  | [optional] 
**opened_by** | **int** |  | [optional] 
**closed_by** | **int** |  | [optional] 
**images** | **List[int]** |  | [optional] 
**close_datetime** | **datetime** |  | [optional] 
**blueprint** | **int** |  | [optional] 
**metadata** | **int** |  | [optional] 

## Example

```python
from avis_client.models.patched_inspection_request import PatchedInspectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedInspectionRequest from a JSON string
patched_inspection_request_instance = PatchedInspectionRequest.from_json(json)
# print the JSON string representation of the object
print PatchedInspectionRequest.to_json()

# convert the object into a dict
patched_inspection_request_dict = patched_inspection_request_instance.to_dict()
# create an instance of PatchedInspectionRequest from a dict
patched_inspection_request_form_dict = patched_inspection_request.from_dict(patched_inspection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


