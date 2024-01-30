# ClassificationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**team** | **int** |  | 
**reported_by** | **int** |  | [optional] 
**inferred_by** | **int** |  | [optional] 
**image** | **int** |  | [optional] 
**result** | **object** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**status** | [**ClassificationResultStatus**](ClassificationResultStatus.md) |  | [optional] 
**failure_reason** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from vue_avis_client.models.classification_result import ClassificationResult

# TODO update the JSON string below
json = "{}"
# create an instance of ClassificationResult from a JSON string
classification_result_instance = ClassificationResult.from_json(json)
# print the JSON string representation of the object
print ClassificationResult.to_json()

# convert the object into a dict
classification_result_dict = classification_result_instance.to_dict()
# create an instance of ClassificationResult from a dict
classification_result_form_dict = classification_result.from_dict(classification_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


