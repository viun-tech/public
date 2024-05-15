# PatchedConfigurationTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**metadata_schema** | **int** |  | [optional] 
**quality_criteria** | **int** |  | [optional] 
**product_category** | **int** |  | [optional] 
**image_attribute_categories** | **List[int]** |  | [optional] 
**description** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 

## Example

```python
from avis_client.models.patched_configuration_type_request import PatchedConfigurationTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedConfigurationTypeRequest from a JSON string
patched_configuration_type_request_instance = PatchedConfigurationTypeRequest.from_json(json)
# print the JSON string representation of the object
print PatchedConfigurationTypeRequest.to_json()

# convert the object into a dict
patched_configuration_type_request_dict = patched_configuration_type_request_instance.to_dict()
# create an instance of PatchedConfigurationTypeRequest from a dict
patched_configuration_type_request_form_dict = patched_configuration_type_request.from_dict(patched_configuration_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


