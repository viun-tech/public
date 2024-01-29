# PatchedInspectionMetadataSchemaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | [optional]
**var_json** | **Dict[str, object]** |  | [optional]

## Example

```python
from vue_avis_client.models.patched_inspection_metadata_schema_request import PatchedInspectionMetadataSchemaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedInspectionMetadataSchemaRequest from a JSON string
patched_inspection_metadata_schema_request_instance = PatchedInspectionMetadataSchemaRequest.from_json(json)
# print the JSON string representation of the object
print PatchedInspectionMetadataSchemaRequest.to_json()

# convert the object into a dict
patched_inspection_metadata_schema_request_dict = patched_inspection_metadata_schema_request_instance.to_dict()
# create an instance of PatchedInspectionMetadataSchemaRequest from a dict
patched_inspection_metadata_schema_request_form_dict = patched_inspection_metadata_schema_request.from_dict(patched_inspection_metadata_schema_request_dict)
```
[[Back to Model list]](..#documentation-for-models) [[Back to API list]](..#documentation-for-api-endpoints) [[Back to README]](..)
