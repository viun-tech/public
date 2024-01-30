# InspectionMetadataSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**team** | **int** |  | 
**var_json** | **object** |  | 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from vue_avis_client.models.inspection_metadata_schema import InspectionMetadataSchema

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionMetadataSchema from a JSON string
inspection_metadata_schema_instance = InspectionMetadataSchema.from_json(json)
# print the JSON string representation of the object
print InspectionMetadataSchema.to_json()

# convert the object into a dict
inspection_metadata_schema_dict = inspection_metadata_schema_instance.to_dict()
# create an instance of InspectionMetadataSchema from a dict
inspection_metadata_schema_form_dict = inspection_metadata_schema.from_dict(inspection_metadata_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


