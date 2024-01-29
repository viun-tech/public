# MLModelTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slug** | **str** |  | [optional]
**name** | **str** |  | [optional]
**description** | **str** |  | [optional]

## Example

```python
from vue_avis_client.models.ml_model_type_request import MLModelTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MLModelTypeRequest from a JSON string
ml_model_type_request_instance = MLModelTypeRequest.from_json(json)
# print the JSON string representation of the object
print MLModelTypeRequest.to_json()

# convert the object into a dict
ml_model_type_request_dict = ml_model_type_request_instance.to_dict()
# create an instance of MLModelTypeRequest from a dict
ml_model_type_request_form_dict = ml_model_type_request.from_dict(ml_model_type_request_dict)
```
[[Back to Model list]](..#documentation-for-models) [[Back to API list]](..#documentation-for-api-endpoints) [[Back to README]](..)
