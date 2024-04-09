# InspectionImagesStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_images** | **int** |  | 
**images_to_inspect** | **int** |  | 

## Example

```python
from avis_client.models.inspection_images_statistics import InspectionImagesStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionImagesStatistics from a JSON string
inspection_images_statistics_instance = InspectionImagesStatistics.from_json(json)
# print the JSON string representation of the object
print InspectionImagesStatistics.to_json()

# convert the object into a dict
inspection_images_statistics_dict = inspection_images_statistics_instance.to_dict()
# create an instance of InspectionImagesStatistics from a dict
inspection_images_statistics_form_dict = inspection_images_statistics.from_dict(inspection_images_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


