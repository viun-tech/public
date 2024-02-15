# ImageAttributeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | 
**category** | **int** |  | 
**classification_results** | **List[int]** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from avis_client.models.image_attribute_request import ImageAttributeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImageAttributeRequest from a JSON string
image_attribute_request_instance = ImageAttributeRequest.from_json(json)
# print the JSON string representation of the object
print ImageAttributeRequest.to_json()

# convert the object into a dict
image_attribute_request_dict = image_attribute_request_instance.to_dict()
# create an instance of ImageAttributeRequest from a dict
image_attribute_request_form_dict = image_attribute_request.from_dict(image_attribute_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


