# MetadataSchema


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
from avis_client.models.metadata_schema import MetadataSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataSchema from a JSON string
metadata_schema_instance = MetadataSchema.from_json(json)
# print the JSON string representation of the object
print MetadataSchema.to_json()

# convert the object into a dict
metadata_schema_dict = metadata_schema_instance.to_dict()
# create an instance of MetadataSchema from a dict
metadata_schema_form_dict = metadata_schema.from_dict(metadata_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


