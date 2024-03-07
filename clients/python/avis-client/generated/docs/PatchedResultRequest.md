# PatchedResultRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | [optional] 
**reported_by** | **int** |  | [optional] 
**inferred_by** | **int** |  | [optional] 
**image** | **int** |  | [optional] 
**image_attributes** | **List[int]** |  | [optional] 
**status** | [**PatchedResultRequestStatus**](PatchedResultRequestStatus.md) |  | [optional] 
**failure_reason** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from avis_client.models.patched_result_request import PatchedResultRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedResultRequest from a JSON string
patched_result_request_instance = PatchedResultRequest.from_json(json)
# print the JSON string representation of the object
print PatchedResultRequest.to_json()

# convert the object into a dict
patched_result_request_dict = patched_result_request_instance.to_dict()
# create an instance of PatchedResultRequest from a dict
patched_result_request_form_dict = patched_result_request.from_dict(patched_result_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


