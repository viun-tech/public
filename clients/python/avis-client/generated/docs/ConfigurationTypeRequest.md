# ConfigurationTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | 
**name** | **str** |  | 
**metadata_schema** | **int** |  | [optional] 
**quality_criteria** | **int** |  | [optional] 
**product_category** | **int** |  | [optional] 
**image_attribute_categories** | **List[int]** |  | [optional] 
**description** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 

## Example

```python
from avis_client.models.configuration_type_request import ConfigurationTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationTypeRequest from a JSON string
configuration_type_request_instance = ConfigurationTypeRequest.from_json(json)
# print the JSON string representation of the object
print ConfigurationTypeRequest.to_json()

# convert the object into a dict
configuration_type_request_dict = configuration_type_request_instance.to_dict()
# create an instance of ConfigurationTypeRequest from a dict
configuration_type_request_form_dict = configuration_type_request.from_dict(configuration_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


