# InspectionMetadataSchemaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  |
**var_json** | **object** |  |

## Example

```python
from avis_client.models.inspection_metadata_schema_request import InspectionMetadataSchemaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionMetadataSchemaRequest from a JSON string
inspection_metadata_schema_request_instance = InspectionMetadataSchemaRequest.from_json(json)
# print the JSON string representation of the object
print InspectionMetadataSchemaRequest.to_json()

# convert the object into a dict
inspection_metadata_schema_request_dict = inspection_metadata_schema_request_instance.to_dict()
# create an instance of InspectionMetadataSchemaRequest from a dict
inspection_metadata_schema_request_form_dict = inspection_metadata_schema_request.from_dict(inspection_metadata_schema_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
