# InspectionImagesStatisticsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_images** | **int** |  | 
**images_to_inspect** | **int** |  | 

## Example

```python
from avis_client.models.inspection_images_statistics_request import InspectionImagesStatisticsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionImagesStatisticsRequest from a JSON string
inspection_images_statistics_request_instance = InspectionImagesStatisticsRequest.from_json(json)
# print the JSON string representation of the object
print InspectionImagesStatisticsRequest.to_json()

# convert the object into a dict
inspection_images_statistics_request_dict = inspection_images_statistics_request_instance.to_dict()
# create an instance of InspectionImagesStatisticsRequest from a dict
inspection_images_statistics_request_form_dict = inspection_images_statistics_request.from_dict(inspection_images_statistics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


