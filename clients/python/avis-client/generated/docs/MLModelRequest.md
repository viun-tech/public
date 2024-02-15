# MLModelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | **object** |  | 
**model** | **int** |  | 
**version** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from avis_client.models.ml_model_request import MLModelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MLModelRequest from a JSON string
ml_model_request_instance = MLModelRequest.from_json(json)
# print the JSON string representation of the object
print MLModelRequest.to_json()

# convert the object into a dict
ml_model_request_dict = ml_model_request_instance.to_dict()
# create an instance of MLModelRequest from a dict
ml_model_request_form_dict = ml_model_request.from_dict(ml_model_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


