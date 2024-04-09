# PaginatedImageAttributeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ImageAttribute]**](ImageAttribute.md) |  | [optional] 

## Example

```python
from avis_client.models.paginated_image_attribute_list import PaginatedImageAttributeList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedImageAttributeList from a JSON string
paginated_image_attribute_list_instance = PaginatedImageAttributeList.from_json(json)
# print the JSON string representation of the object
print PaginatedImageAttributeList.to_json()

# convert the object into a dict
paginated_image_attribute_list_dict = paginated_image_attribute_list_instance.to_dict()
# create an instance of PaginatedImageAttributeList from a dict
paginated_image_attribute_list_form_dict = paginated_image_attribute_list.from_dict(paginated_image_attribute_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


