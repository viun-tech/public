# PaginatedInspectionImagesStatisticsList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[InspectionImagesStatistics]**](InspectionImagesStatistics.md) |  | [optional] 

## Example

```python
from avis_client.models.paginated_inspection_images_statistics_list import PaginatedInspectionImagesStatisticsList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedInspectionImagesStatisticsList from a JSON string
paginated_inspection_images_statistics_list_instance = PaginatedInspectionImagesStatisticsList.from_json(json)
# print the JSON string representation of the object
print PaginatedInspectionImagesStatisticsList.to_json()

# convert the object into a dict
paginated_inspection_images_statistics_list_dict = paginated_inspection_images_statistics_list_instance.to_dict()
# create an instance of PaginatedInspectionImagesStatisticsList from a dict
paginated_inspection_images_statistics_list_form_dict = paginated_inspection_images_statistics_list.from_dict(paginated_inspection_images_statistics_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


