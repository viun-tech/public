# PaginatedMetadataSchemaList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[MetadataSchema]**](MetadataSchema.md) |  | [optional] 

## Example

```python
from avis_client.models.paginated_metadata_schema_list import PaginatedMetadataSchemaList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedMetadataSchemaList from a JSON string
paginated_metadata_schema_list_instance = PaginatedMetadataSchemaList.from_json(json)
# print the JSON string representation of the object
print PaginatedMetadataSchemaList.to_json()

# convert the object into a dict
paginated_metadata_schema_list_dict = paginated_metadata_schema_list_instance.to_dict()
# create an instance of PaginatedMetadataSchemaList from a dict
paginated_metadata_schema_list_form_dict = paginated_metadata_schema_list.from_dict(paginated_metadata_schema_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


