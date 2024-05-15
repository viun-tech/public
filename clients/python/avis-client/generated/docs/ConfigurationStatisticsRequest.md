# ConfigurationStatisticsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | **int** |  |
**opened_inspections** | **int** |  |
**inspections_marked_for_validation** | **int** |  |

## Example

```python
from avis_client.models.configuration_statistics_request import ConfigurationStatisticsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationStatisticsRequest from a JSON string
configuration_statistics_request_instance = ConfigurationStatisticsRequest.from_json(json)
# print the JSON string representation of the object
print ConfigurationStatisticsRequest.to_json()

# convert the object into a dict
configuration_statistics_request_dict = configuration_statistics_request_instance.to_dict()
# create an instance of ConfigurationStatisticsRequest from a dict
configuration_statistics_request_form_dict = configuration_statistics_request.from_dict(configuration_statistics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
