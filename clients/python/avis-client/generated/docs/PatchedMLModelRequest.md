# PatchedMLModelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **object** |  | [optional] 
**model** | **int** |  | [optional] 
**version** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from avis_client.models.patched_ml_model_request import PatchedMLModelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMLModelRequest from a JSON string
patched_ml_model_request_instance = PatchedMLModelRequest.from_json(json)
# print the JSON string representation of the object
print PatchedMLModelRequest.to_json()

# convert the object into a dict
patched_ml_model_request_dict = patched_ml_model_request_instance.to_dict()
# create an instance of PatchedMLModelRequest from a dict
patched_ml_model_request_form_dict = patched_ml_model_request.from_dict(patched_ml_model_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


