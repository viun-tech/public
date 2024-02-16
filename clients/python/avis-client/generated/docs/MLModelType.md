# MLModelType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**slug** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from avis_client.models.ml_model_type import MLModelType

# TODO update the JSON string below
json = "{}"
# create an instance of MLModelType from a JSON string
ml_model_type_instance = MLModelType.from_json(json)
# print the JSON string representation of the object
print MLModelType.to_json()

# convert the object into a dict
ml_model_type_dict = ml_model_type_instance.to_dict()
# create an instance of MLModelType from a dict
ml_model_type_form_dict = ml_model_type.from_dict(ml_model_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


