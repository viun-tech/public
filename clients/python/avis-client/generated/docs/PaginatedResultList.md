# PaginatedResultList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Result]**](Result.md) |  | 

## Example

```python
from avis_client.models.paginated_result_list import PaginatedResultList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResultList from a JSON string
paginated_result_list_instance = PaginatedResultList.from_json(json)
# print the JSON string representation of the object
print PaginatedResultList.to_json()

# convert the object into a dict
paginated_result_list_dict = paginated_result_list_instance.to_dict()
# create an instance of PaginatedResultList from a dict
paginated_result_list_form_dict = paginated_result_list.from_dict(paginated_result_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


