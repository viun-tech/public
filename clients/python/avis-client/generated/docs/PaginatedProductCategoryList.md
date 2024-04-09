# PaginatedProductCategoryList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[ProductCategory]**](ProductCategory.md) |  | [optional] 

## Example

```python
from avis_client.models.paginated_product_category_list import PaginatedProductCategoryList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedProductCategoryList from a JSON string
paginated_product_category_list_instance = PaginatedProductCategoryList.from_json(json)
# print the JSON string representation of the object
print PaginatedProductCategoryList.to_json()

# convert the object into a dict
paginated_product_category_list_dict = paginated_product_category_list_instance.to_dict()
# create an instance of PaginatedProductCategoryList from a dict
paginated_product_category_list_form_dict = paginated_product_category_list.from_dict(paginated_product_category_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


