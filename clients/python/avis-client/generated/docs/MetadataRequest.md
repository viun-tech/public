# MetadataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | 
**configurations** | **List[int]** |  | [optional] 
**var_schema** | **int** |  | 
**data** | **object** |  | [optional] 

## Example

```python
from avis_client.models.metadata_request import MetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataRequest from a JSON string
metadata_request_instance = MetadataRequest.from_json(json)
# print the JSON string representation of the object
print MetadataRequest.to_json()

# convert the object into a dict
metadata_request_dict = metadata_request_instance.to_dict()
# create an instance of MetadataRequest from a dict
metadata_request_form_dict = metadata_request.from_dict(metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


