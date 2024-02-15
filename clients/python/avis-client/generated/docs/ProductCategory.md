# ProductCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**team** | **int** |  | 
**instances** | **List[int]** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from avis_client.models.product_category import ProductCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCategory from a JSON string
product_category_instance = ProductCategory.from_json(json)
# print the JSON string representation of the object
print ProductCategory.to_json()

# convert the object into a dict
product_category_dict = product_category_instance.to_dict()
# create an instance of ProductCategory from a dict
product_category_form_dict = product_category.from_dict(product_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


