# PatchedMetadataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | [optional] 
**configurations** | **List[int]** |  | [optional] 
**var_schema** | **int** |  | [optional] 
**data** | **object** |  | [optional] 

## Example

```python
from avis_client.models.patched_metadata_request import PatchedMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMetadataRequest from a JSON string
patched_metadata_request_instance = PatchedMetadataRequest.from_json(json)
# print the JSON string representation of the object
print PatchedMetadataRequest.to_json()

# convert the object into a dict
patched_metadata_request_dict = patched_metadata_request_instance.to_dict()
# create an instance of PatchedMetadataRequest from a dict
patched_metadata_request_form_dict = patched_metadata_request.from_dict(patched_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


