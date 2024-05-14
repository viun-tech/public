# PaginatedInspectionValidationStatusList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  |
**next** | **str** |  | [optional]
**previous** | **str** |  | [optional]
**results** | [**List[InspectionValidationStatus]**](InspectionValidationStatus.md) |  |

## Example

```python
from avis_client.models.paginated_inspection_validation_status_list import PaginatedInspectionValidationStatusList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedInspectionValidationStatusList from a JSON string
paginated_inspection_validation_status_list_instance = PaginatedInspectionValidationStatusList.from_json(json)
# print the JSON string representation of the object
print PaginatedInspectionValidationStatusList.to_json()

# convert the object into a dict
paginated_inspection_validation_status_list_dict = paginated_inspection_validation_status_list_instance.to_dict()
# create an instance of PaginatedInspectionValidationStatusList from a dict
paginated_inspection_validation_status_list_form_dict = paginated_inspection_validation_status_list.from_dict(paginated_inspection_validation_status_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
