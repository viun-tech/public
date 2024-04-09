# PaginatedInspectionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Inspection]**](Inspection.md) |  | [optional] 

## Example

```python
from avis_client.models.paginated_inspection_list import PaginatedInspectionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedInspectionList from a JSON string
paginated_inspection_list_instance = PaginatedInspectionList.from_json(json)
# print the JSON string representation of the object
print PaginatedInspectionList.to_json()

# convert the object into a dict
paginated_inspection_list_dict = paginated_inspection_list_instance.to_dict()
# create an instance of PaginatedInspectionList from a dict
paginated_inspection_list_form_dict = paginated_inspection_list.from_dict(paginated_inspection_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


