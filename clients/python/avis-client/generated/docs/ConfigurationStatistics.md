# ConfigurationStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | **int** |  |
**opened_inspections** | **int** |  |
**inspections_marked_for_validation** | **int** |  |

## Example

```python
from avis_client.models.configuration_statistics import ConfigurationStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationStatistics from a JSON string
configuration_statistics_instance = ConfigurationStatistics.from_json(json)
# print the JSON string representation of the object
print ConfigurationStatistics.to_json()

# convert the object into a dict
configuration_statistics_dict = configuration_statistics_instance.to_dict()
# create an instance of ConfigurationStatistics from a dict
configuration_statistics_form_dict = configuration_statistics.from_dict(configuration_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
