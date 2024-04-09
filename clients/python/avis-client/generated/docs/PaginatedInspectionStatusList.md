# PaginatedInspectionStatusList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[InspectionStatus]**](InspectionStatus.md) |  | [optional] 

## Example

```python
from avis_client.models.paginated_inspection_status_list import PaginatedInspectionStatusList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedInspectionStatusList from a JSON string
paginated_inspection_status_list_instance = PaginatedInspectionStatusList.from_json(json)
# print the JSON string representation of the object
print PaginatedInspectionStatusList.to_json()

# convert the object into a dict
paginated_inspection_status_list_dict = paginated_inspection_status_list_instance.to_dict()
# create an instance of PaginatedInspectionStatusList from a dict
paginated_inspection_status_list_form_dict = paginated_inspection_status_list.from_dict(paginated_inspection_status_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


