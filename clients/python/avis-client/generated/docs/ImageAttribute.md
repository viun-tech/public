# ImageAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**team** | **int** |  | 
**category** | **int** |  | 
**results** | **List[int]** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**value** | **str** |  | [optional] 

## Example

```python
from avis_client.models.image_attribute import ImageAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of ImageAttribute from a JSON string
image_attribute_instance = ImageAttribute.from_json(json)
# print the JSON string representation of the object
print ImageAttribute.to_json()

# convert the object into a dict
image_attribute_dict = image_attribute_instance.to_dict()
# create an instance of ImageAttribute from a dict
image_attribute_form_dict = image_attribute.from_dict(image_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


