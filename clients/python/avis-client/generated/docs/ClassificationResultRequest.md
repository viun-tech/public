# ClassificationResultRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  |
**reported_by** | **int** |  | [optional]
**inferred_by** | **int** |  | [optional]
**image** | **int** |  | [optional]
**result** | **object** |  | [optional]
**status** | [**ClassificationResultStatus**](ClassificationResultStatus.md) |  | [optional]
**failure_reason** | **str** |  | [optional]
**comment** | **str** |  | [optional]

## Example

```python
from avis_client.models.classification_result_request import ClassificationResultRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClassificationResultRequest from a JSON string
classification_result_request_instance = ClassificationResultRequest.from_json(json)
# print the JSON string representation of the object
print ClassificationResultRequest.to_json()

# convert the object into a dict
classification_result_request_dict = classification_result_request_instance.to_dict()
# create an instance of ClassificationResultRequest from a dict
classification_result_request_form_dict = classification_result_request.from_dict(classification_result_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
