# Result


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**team** | **int** |  | 
**reported_by** | **int** |  | [optional] 
**inferred_by** | **int** |  | [optional] 
**image** | **int** |  | [optional] 
**image_attributes** | **List[int]** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**status** | [**PatchedResultRequestStatus**](PatchedResultRequestStatus.md) |  | [optional] 
**failure_reason** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from avis_client.models.result import Result

# TODO update the JSON string below
json = "{}"
# create an instance of Result from a JSON string
result_instance = Result.from_json(json)
# print the JSON string representation of the object
print Result.to_json()

# convert the object into a dict
result_dict = result_instance.to_dict()
# create an instance of Result from a dict
result_form_dict = result.from_dict(result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


