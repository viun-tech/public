# PaginatedInspectionStatisticsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  |
**next** | **str** |  | [optional]
**previous** | **str** |  | [optional]
**results** | [**List[InspectionStatistics]**](InspectionStatistics.md) |  |

## Example

```python
from avis_client.models.paginated_inspection_statistics_list import PaginatedInspectionStatisticsList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedInspectionStatisticsList from a JSON string
paginated_inspection_statistics_list_instance = PaginatedInspectionStatisticsList.from_json(json)
# print the JSON string representation of the object
print PaginatedInspectionStatisticsList.to_json()

# convert the object into a dict
paginated_inspection_statistics_list_dict = paginated_inspection_statistics_list_instance.to_dict()
# create an instance of PaginatedInspectionStatisticsList from a dict
paginated_inspection_statistics_list_form_dict = paginated_inspection_statistics_list.from_dict(paginated_inspection_statistics_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
