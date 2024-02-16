# PatchedMLModelTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from avis_client.models.patched_ml_model_type_request import PatchedMLModelTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMLModelTypeRequest from a JSON string
patched_ml_model_type_request_instance = PatchedMLModelTypeRequest.from_json(json)
# print the JSON string representation of the object
print PatchedMLModelTypeRequest.to_json()

# convert the object into a dict
patched_ml_model_type_request_dict = patched_ml_model_type_request_instance.to_dict()
# create an instance of PatchedMLModelTypeRequest from a dict
patched_ml_model_type_request_form_dict = patched_ml_model_type_request.from_dict(patched_ml_model_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


