# PaginatedConfigurationTypeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  |
**next** | **str** |  | [optional]
**previous** | **str** |  | [optional]
**results** | [**List[ConfigurationType]**](ConfigurationType.md) |  |

## Example

```python
from avis_client.models.paginated_configuration_type_list import PaginatedConfigurationTypeList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedConfigurationTypeList from a JSON string
paginated_configuration_type_list_instance = PaginatedConfigurationTypeList.from_json(json)
# print the JSON string representation of the object
print PaginatedConfigurationTypeList.to_json()

# convert the object into a dict
paginated_configuration_type_list_dict = paginated_configuration_type_list_instance.to_dict()
# create an instance of PaginatedConfigurationTypeList from a dict
paginated_configuration_type_list_form_dict = paginated_configuration_type_list.from_dict(paginated_configuration_type_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
