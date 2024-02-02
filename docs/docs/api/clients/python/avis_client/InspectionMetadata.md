# InspectionMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly]
**team** | **int** |  |
**blueprints** | **List[int]** |  | [optional]
**var_schema** | **int** |  |
**data** | **object** |  | [optional]
**created_at** | **datetime** |  | [readonly]
**updated_at** | **datetime** |  | [readonly]

## Example

```python
from avis_client.models.inspection_metadata import InspectionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionMetadata from a JSON string
inspection_metadata_instance = InspectionMetadata.from_json(json)
# print the JSON string representation of the object
print InspectionMetadata.to_json()

# convert the object into a dict
inspection_metadata_dict = inspection_metadata_instance.to_dict()
# create an instance of InspectionMetadata from a dict
inspection_metadata_form_dict = inspection_metadata.from_dict(inspection_metadata_dict)
```
[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)
