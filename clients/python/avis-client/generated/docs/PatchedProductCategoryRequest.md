# PatchedProductCategoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team** | **int** |  | [optional] 
**instances** | **List[int]** |  | [optional] 
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from avis_client.models.patched_product_category_request import PatchedProductCategoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedProductCategoryRequest from a JSON string
patched_product_category_request_instance = PatchedProductCategoryRequest.from_json(json)
# print the JSON string representation of the object
print PatchedProductCategoryRequest.to_json()

# convert the object into a dict
patched_product_category_request_dict = patched_product_category_request_instance.to_dict()
# create an instance of PatchedProductCategoryRequest from a dict
patched_product_category_request_form_dict = patched_product_category_request.from_dict(patched_product_category_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


