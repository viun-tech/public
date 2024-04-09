# InspectionStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_inspections** | **int** |  | 
**closed_inspections** | **int** |  | 
**opened_inspections** | **int** |  | 
**validation_requests** | **int** |  | 

## Example

```python
from avis_client.models.inspection_statistics import InspectionStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionStatistics from a JSON string
inspection_statistics_instance = InspectionStatistics.from_json(json)
# print the JSON string representation of the object
print InspectionStatistics.to_json()

# convert the object into a dict
inspection_statistics_dict = inspection_statistics_instance.to_dict()
# create an instance of InspectionStatistics from a dict
inspection_statistics_form_dict = inspection_statistics.from_dict(inspection_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


