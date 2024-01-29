# PatchedClassificationResultRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | [optional] 
**reported_by** | **int** |  | [optional] 
**inferred_by** | **int** |  | [optional] 
**image** | **int** |  | [optional] 
**result** | **object** |  | [optional] 
**status** | [**ClassificationResultStatus**](ClassificationResultStatus.md) |  | [optional] 
**failure_reason** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from vue_avis_client.models.patched_classification_result_request import PatchedClassificationResultRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedClassificationResultRequest from a JSON string
patched_classification_result_request_instance = PatchedClassificationResultRequest.from_json(json)
# print the JSON string representation of the object
print PatchedClassificationResultRequest.to_json()

# convert the object into a dict
patched_classification_result_request_dict = patched_classification_result_request_instance.to_dict()
# create an instance of PatchedClassificationResultRequest from a dict
patched_classification_result_request_form_dict = patched_classification_result_request.from_dict(patched_classification_result_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


