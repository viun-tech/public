# InspectionStatisticsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_inspections** | **int** |  | 
**closed_inspections** | **int** |  | 
**opened_inspections** | **int** |  | 
**validation_requests** | **int** |  | 

## Example

```python
from avis_client.models.inspection_statistics_request import InspectionStatisticsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionStatisticsRequest from a JSON string
inspection_statistics_request_instance = InspectionStatisticsRequest.from_json(json)
# print the JSON string representation of the object
print InspectionStatisticsRequest.to_json()

# convert the object into a dict
inspection_statistics_request_dict = inspection_statistics_request_instance.to_dict()
# create an instance of InspectionStatisticsRequest from a dict
inspection_statistics_request_form_dict = inspection_statistics_request.from_dict(inspection_statistics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


