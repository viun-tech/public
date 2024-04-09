# PaginatedMLModelTypeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[MLModelType]**](MLModelType.md) |  | [optional] 

## Example

```python
from avis_client.models.paginated_ml_model_type_list import PaginatedMLModelTypeList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedMLModelTypeList from a JSON string
paginated_ml_model_type_list_instance = PaginatedMLModelTypeList.from_json(json)
# print the JSON string representation of the object
print PaginatedMLModelTypeList.to_json()

# convert the object into a dict
paginated_ml_model_type_list_dict = paginated_ml_model_type_list_instance.to_dict()
# create an instance of PaginatedMLModelTypeList from a dict
paginated_ml_model_type_list_form_dict = paginated_ml_model_type_list.from_dict(paginated_ml_model_type_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


