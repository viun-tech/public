# PatchedInspectionMetadataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | [optional]
**blueprints** | **List[int]** |  | [optional]
**var_schema** | **int** |  | [optional]
**data** | **object** |  | [optional]

## Example

```python
from avis_client.models.patched_inspection_metadata_request import PatchedInspectionMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedInspectionMetadataRequest from a JSON string
patched_inspection_metadata_request_instance = PatchedInspectionMetadataRequest.from_json(json)
# print the JSON string representation of the object
print PatchedInspectionMetadataRequest.to_json()

# convert the object into a dict
patched_inspection_metadata_request_dict = patched_inspection_metadata_request_instance.to_dict()
# create an instance of PatchedInspectionMetadataRequest from a dict
patched_inspection_metadata_request_form_dict = patched_inspection_metadata_request.from_dict(patched_inspection_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
