# MLModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly]
**model** | **int** |  |
**created_at** | **datetime** |  | [readonly]
**updated_at** | **datetime** |  | [readonly]
**version** | **str** |  | [optional]
**url** | **str** |  | [optional]
**teams** | **List[int]** |  | [readonly]

## Example

```python
from avis_client.models.ml_model import MLModel

# TODO update the JSON string below
json = "{}"
# create an instance of MLModel from a JSON string
ml_model_instance = MLModel.from_json(json)
# print the JSON string representation of the object
print MLModel.to_json()

# convert the object into a dict
ml_model_dict = ml_model_instance.to_dict()
# create an instance of MLModel from a dict
ml_model_form_dict = ml_model.from_dict(ml_model_dict)
```
[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)
