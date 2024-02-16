# PatchedImageAttributeCategoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**ml_model** | **int** |  | [optional] 

## Example

```python
from avis_client.models.patched_image_attribute_category_request import PatchedImageAttributeCategoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedImageAttributeCategoryRequest from a JSON string
patched_image_attribute_category_request_instance = PatchedImageAttributeCategoryRequest.from_json(json)
# print the JSON string representation of the object
print PatchedImageAttributeCategoryRequest.to_json()

# convert the object into a dict
patched_image_attribute_category_request_dict = patched_image_attribute_category_request_instance.to_dict()
# create an instance of PatchedImageAttributeCategoryRequest from a dict
patched_image_attribute_category_request_form_dict = patched_image_attribute_category_request.from_dict(patched_image_attribute_category_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


