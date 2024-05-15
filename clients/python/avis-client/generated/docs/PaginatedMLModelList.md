# PaginatedMLModelList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[MLModel]**](MLModel.md) |  | 

## Example

```python
from avis_client.models.paginated_ml_model_list import PaginatedMLModelList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedMLModelList from a JSON string
paginated_ml_model_list_instance = PaginatedMLModelList.from_json(json)
# print the JSON string representation of the object
print PaginatedMLModelList.to_json()

# convert the object into a dict
paginated_ml_model_list_dict = paginated_ml_model_list_instance.to_dict()
# create an instance of PaginatedMLModelList from a dict
paginated_ml_model_list_form_dict = paginated_ml_model_list.from_dict(paginated_ml_model_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


