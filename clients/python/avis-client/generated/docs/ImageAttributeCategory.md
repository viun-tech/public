# ImageAttributeCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**team** | **int** |  | 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**ml_model** | **int** |  | [optional] 

## Example

```python
from avis_client.models.image_attribute_category import ImageAttributeCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ImageAttributeCategory from a JSON string
image_attribute_category_instance = ImageAttributeCategory.from_json(json)
# print the JSON string representation of the object
print ImageAttributeCategory.to_json()

# convert the object into a dict
image_attribute_category_dict = image_attribute_category_instance.to_dict()
# create an instance of ImageAttributeCategory from a dict
image_attribute_category_form_dict = image_attribute_category.from_dict(image_attribute_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


