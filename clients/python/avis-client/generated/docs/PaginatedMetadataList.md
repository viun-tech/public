# PaginatedMetadataList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Metadata]**](Metadata.md) |  | [optional] 

## Example

```python
from avis_client.models.paginated_metadata_list import PaginatedMetadataList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedMetadataList from a JSON string
paginated_metadata_list_instance = PaginatedMetadataList.from_json(json)
# print the JSON string representation of the object
print PaginatedMetadataList.to_json()

# convert the object into a dict
paginated_metadata_list_dict = paginated_metadata_list_instance.to_dict()
# create an instance of PaginatedMetadataList from a dict
paginated_metadata_list_form_dict = paginated_metadata_list.from_dict(paginated_metadata_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


