# PatchedImageAttributeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | [optional] 
**category** | **int** |  | [optional] 
**results** | **List[int]** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from avis_client.models.patched_image_attribute_request import PatchedImageAttributeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedImageAttributeRequest from a JSON string
patched_image_attribute_request_instance = PatchedImageAttributeRequest.from_json(json)
# print the JSON string representation of the object
print PatchedImageAttributeRequest.to_json()

# convert the object into a dict
patched_image_attribute_request_dict = patched_image_attribute_request_instance.to_dict()
# create an instance of PatchedImageAttributeRequest from a dict
patched_image_attribute_request_form_dict = patched_image_attribute_request.from_dict(patched_image_attribute_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


