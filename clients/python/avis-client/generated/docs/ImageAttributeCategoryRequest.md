# ImageAttributeCategoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**ml_model** | **int** |  | [optional] 

## Example

```python
from avis_client.models.image_attribute_category_request import ImageAttributeCategoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImageAttributeCategoryRequest from a JSON string
image_attribute_category_request_instance = ImageAttributeCategoryRequest.from_json(json)
# print the JSON string representation of the object
print ImageAttributeCategoryRequest.to_json()

# convert the object into a dict
image_attribute_category_request_dict = image_attribute_category_request_instance.to_dict()
# create an instance of ImageAttributeCategoryRequest from a dict
image_attribute_category_request_form_dict = image_attribute_category_request.from_dict(image_attribute_category_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


