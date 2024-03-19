# MetadataSchemaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | 
**var_json** | **object** |  | 

## Example

```python
from avis_client.models.metadata_schema_request import MetadataSchemaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataSchemaRequest from a JSON string
metadata_schema_request_instance = MetadataSchemaRequest.from_json(json)
# print the JSON string representation of the object
print MetadataSchemaRequest.to_json()

# convert the object into a dict
metadata_schema_request_dict = metadata_schema_request_instance.to_dict()
# create an instance of MetadataSchemaRequest from a dict
metadata_schema_request_form_dict = metadata_schema_request.from_dict(metadata_schema_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


