# ProductCategoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | 
**instances** | **List[int]** |  | [optional] 
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from avis_client.models.product_category_request import ProductCategoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCategoryRequest from a JSON string
product_category_request_instance = ProductCategoryRequest.from_json(json)
# print the JSON string representation of the object
print ProductCategoryRequest.to_json()

# convert the object into a dict
product_category_request_dict = product_category_request_instance.to_dict()
# create an instance of ProductCategoryRequest from a dict
product_category_request_form_dict = product_category_request.from_dict(product_category_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


