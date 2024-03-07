# ResultRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | 
**reported_by** | **int** |  | [optional] 
**inferred_by** | **int** |  | [optional] 
**image** | **int** |  | [optional] 
**image_attributes** | **List[int]** |  | [optional] 
**status** | [**PatchedResultRequestStatus**](PatchedResultRequestStatus.md) |  | [optional] 
**failure_reason** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from avis_client.models.result_request import ResultRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResultRequest from a JSON string
result_request_instance = ResultRequest.from_json(json)
# print the JSON string representation of the object
print ResultRequest.to_json()

# convert the object into a dict
result_request_dict = result_request_instance.to_dict()
# create an instance of ResultRequest from a dict
result_request_form_dict = result_request.from_dict(result_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


