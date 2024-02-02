# InspectionMetadataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  |
**blueprints** | **List[int]** |  | [optional]
**var_schema** | **int** |  |
**data** | **object** |  | [optional]

## Example

```python
from avis_client.models.inspection_metadata_request import InspectionMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionMetadataRequest from a JSON string
inspection_metadata_request_instance = InspectionMetadataRequest.from_json(json)
# print the JSON string representation of the object
print InspectionMetadataRequest.to_json()

# convert the object into a dict
inspection_metadata_request_dict = inspection_metadata_request_instance.to_dict()
# create an instance of InspectionMetadataRequest from a dict
inspection_metadata_request_form_dict = inspection_metadata_request.from_dict(inspection_metadata_request_dict)
```
[[Back to Model list]](../#documentation-for-models) [[Back to API list]](../#documentation-for-api-endpoints) [[Back to README]](../)
