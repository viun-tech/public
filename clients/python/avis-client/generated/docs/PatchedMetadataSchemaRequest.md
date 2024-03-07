# PatchedMetadataSchemaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | [optional] 
**var_json** | **object** |  | [optional] 

## Example

```python
from avis_client.models.patched_metadata_schema_request import PatchedMetadataSchemaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMetadataSchemaRequest from a JSON string
patched_metadata_schema_request_instance = PatchedMetadataSchemaRequest.from_json(json)
# print the JSON string representation of the object
print PatchedMetadataSchemaRequest.to_json()

# convert the object into a dict
patched_metadata_schema_request_dict = patched_metadata_schema_request_instance.to_dict()
# create an instance of PatchedMetadataSchemaRequest from a dict
patched_metadata_schema_request_form_dict = patched_metadata_schema_request.from_dict(patched_metadata_schema_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


