# Avis.StatisticsApi

All URIs are relative to _http://localhost:8000_

| Method                                                                                  | HTTP request                                   | Description |
| --------------------------------------------------------------------------------------- | ---------------------------------------------- | ----------- |
| [**statisticsConfigurationCreate**](StatisticsApi.md#statisticsConfigurationCreate)     | **POST** /api/statistics/configuration/        |
| [**statisticsConfigurationDestroy**](StatisticsApi.md#statisticsConfigurationDestroy)   | **DELETE** /api/statistics/configuration/{id}/ |
| [**statisticsConfigurationList**](StatisticsApi.md#statisticsConfigurationList)         | **GET** /api/statistics/configuration/         |
| [**statisticsConfigurationRetrieve**](StatisticsApi.md#statisticsConfigurationRetrieve) | **GET** /api/statistics/configuration/{id}/    |
| [**statisticsConfigurationUpdate**](StatisticsApi.md#statisticsConfigurationUpdate)     | **PUT** /api/statistics/configuration/{id}/    |
| [**statisticsInspectionCreate**](StatisticsApi.md#statisticsInspectionCreate)           | **POST** /api/statistics/inspection/           |
| [**statisticsInspectionDestroy**](StatisticsApi.md#statisticsInspectionDestroy)         | **DELETE** /api/statistics/inspection/{id}/    |
| [**statisticsInspectionList**](StatisticsApi.md#statisticsInspectionList)               | **GET** /api/statistics/inspection/            |
| [**statisticsInspectionRetrieve**](StatisticsApi.md#statisticsInspectionRetrieve)       | **GET** /api/statistics/inspection/{id}/       |
| [**statisticsInspectionUpdate**](StatisticsApi.md#statisticsInspectionUpdate)           | **PUT** /api/statistics/inspection/{id}/       |
| [**statisticsTeamCreate**](StatisticsApi.md#statisticsTeamCreate)                       | **POST** /api/statistics/team/                 |
| [**statisticsTeamDestroy**](StatisticsApi.md#statisticsTeamDestroy)                     | **DELETE** /api/statistics/team/{id}/          |
| [**statisticsTeamList**](StatisticsApi.md#statisticsTeamList)                           | **GET** /api/statistics/team/                  |
| [**statisticsTeamRetrieve**](StatisticsApi.md#statisticsTeamRetrieve)                   | **GET** /api/statistics/team/{id}/             |
| [**statisticsTeamUpdate**](StatisticsApi.md#statisticsTeamUpdate)                       | **PUT** /api/statistics/team/{id}/             |

## statisticsConfigurationCreate

> ConfigurationStatistics statisticsConfigurationCreate(configurationStatisticsRequest)

A mixin that allows reading entities (listing and retrieving by id).

### Example

```javascript
import Avis from "avis";
let defaultClient = Avis.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications["cookieAuth"];
cookieAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications["ApiKeyAuth"];
ApiKeyAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new Avis.StatisticsApi();
let configurationStatisticsRequest = new Avis.ConfigurationStatisticsRequest(); // ConfigurationStatisticsRequest |
apiInstance.statisticsConfigurationCreate(
  configurationStatisticsRequest,
  (error, data, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log("API called successfully. Returned data: " + data);
    }
  },
);
```

### Parameters

| Name                               | Type                                                                    | Description | Notes |
| ---------------------------------- | ----------------------------------------------------------------------- | ----------- | ----- |
| **configurationStatisticsRequest** | [**ConfigurationStatisticsRequest**](ConfigurationStatisticsRequest.md) |             |

### Return type

[**ConfigurationStatistics**](ConfigurationStatistics.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## statisticsConfigurationDestroy

> statisticsConfigurationDestroy(id)

A mixin that allows reading entities (listing and retrieving by id).

### Example

```javascript
import Avis from "avis";
let defaultClient = Avis.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications["cookieAuth"];
cookieAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications["ApiKeyAuth"];
ApiKeyAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new Avis.StatisticsApi();
let id = 56; // Number | A unique integer value identifying this configuration.
apiInstance.statisticsConfigurationDestroy(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully.");
  }
});
```

### Parameters

| Name   | Type       | Description                                            | Notes |
| ------ | ---------- | ------------------------------------------------------ | ----- |
| **id** | **Number** | A unique integer value identifying this configuration. |

### Return type

null (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

## statisticsConfigurationList

> PaginatedConfigurationStatisticsList statisticsConfigurationList(opts)

A mixin that allows reading entities (listing and retrieving by id).

### Example

```javascript
import Avis from "avis";
let defaultClient = Avis.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications["cookieAuth"];
cookieAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications["ApiKeyAuth"];
ApiKeyAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new Avis.StatisticsApi();
let opts = {
  id: [null], // [Number] | Multiple values may be separated by commas.
  ordering: "ordering_example", // String | Which field to use when ordering the results.
  page: 56, // Number | A page number within the paginated result set.
  pageSize: 56, // Number | Number of results to return per page.
};
apiInstance.statisticsConfigurationList(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name         | Type                      | Description                                    | Notes      |
| ------------ | ------------------------- | ---------------------------------------------- | ---------- |
| **id**       | [**[Number]**](Number.md) | Multiple values may be separated by commas.    | [optional] |
| **ordering** | **String**                | Which field to use when ordering the results.  | [optional] |
| **page**     | **Number**                | A page number within the paginated result set. | [optional] |
| **pageSize** | **Number**                | Number of results to return per page.          | [optional] |

### Return type

[**PaginatedConfigurationStatisticsList**](PaginatedConfigurationStatisticsList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## statisticsConfigurationRetrieve

> ConfigurationStatistics statisticsConfigurationRetrieve(id)

A mixin that allows reading entities (listing and retrieving by id).

### Example

```javascript
import Avis from "avis";
let defaultClient = Avis.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications["cookieAuth"];
cookieAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications["ApiKeyAuth"];
ApiKeyAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new Avis.StatisticsApi();
let id = 56; // Number | A unique integer value identifying this configuration.
apiInstance.statisticsConfigurationRetrieve(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name   | Type       | Description                                            | Notes |
| ------ | ---------- | ------------------------------------------------------ | ----- |
| **id** | **Number** | A unique integer value identifying this configuration. |

### Return type

[**ConfigurationStatistics**](ConfigurationStatistics.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## statisticsConfigurationUpdate

> ConfigurationStatistics statisticsConfigurationUpdate(id, configurationStatisticsRequest)

A mixin that allows reading entities (listing and retrieving by id).

### Example

```javascript
import Avis from "avis";
let defaultClient = Avis.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications["cookieAuth"];
cookieAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications["ApiKeyAuth"];
ApiKeyAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new Avis.StatisticsApi();
let id = 56; // Number | A unique integer value identifying this configuration.
let configurationStatisticsRequest = new Avis.ConfigurationStatisticsRequest(); // ConfigurationStatisticsRequest |
apiInstance.statisticsConfigurationUpdate(
  id,
  configurationStatisticsRequest,
  (error, data, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log("API called successfully. Returned data: " + data);
    }
  },
);
```

### Parameters

| Name                               | Type                                                                    | Description                                            | Notes |
| ---------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------ | ----- |
| **id**                             | **Number**                                                              | A unique integer value identifying this configuration. |
| **configurationStatisticsRequest** | [**ConfigurationStatisticsRequest**](ConfigurationStatisticsRequest.md) |                                                        |

### Return type

[**ConfigurationStatistics**](ConfigurationStatistics.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## statisticsInspectionCreate

> InspectionImagesStatistics statisticsInspectionCreate(inspectionImagesStatisticsRequest)

A mixin that only allows retrieving entities by id.

### Example

```javascript
import Avis from "avis";
let defaultClient = Avis.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications["cookieAuth"];
cookieAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications["ApiKeyAuth"];
ApiKeyAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new Avis.StatisticsApi();
let inspectionImagesStatisticsRequest =
  new Avis.InspectionImagesStatisticsRequest(); // InspectionImagesStatisticsRequest |
apiInstance.statisticsInspectionCreate(
  inspectionImagesStatisticsRequest,
  (error, data, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log("API called successfully. Returned data: " + data);
    }
  },
);
```

### Parameters

| Name                                  | Type                                                                          | Description | Notes |
| ------------------------------------- | ----------------------------------------------------------------------------- | ----------- | ----- |
| **inspectionImagesStatisticsRequest** | [**InspectionImagesStatisticsRequest**](InspectionImagesStatisticsRequest.md) |             |

### Return type

[**InspectionImagesStatistics**](InspectionImagesStatistics.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## statisticsInspectionDestroy

> statisticsInspectionDestroy(id)

A mixin that only allows retrieving entities by id.

### Example

```javascript
import Avis from "avis";
let defaultClient = Avis.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications["cookieAuth"];
cookieAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications["ApiKeyAuth"];
ApiKeyAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new Avis.StatisticsApi();
let id = 56; // Number | A unique integer value identifying this image.
apiInstance.statisticsInspectionDestroy(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully.");
  }
});
```

### Parameters

| Name   | Type       | Description                                    | Notes |
| ------ | ---------- | ---------------------------------------------- | ----- |
| **id** | **Number** | A unique integer value identifying this image. |

### Return type

null (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

## statisticsInspectionList

> PaginatedInspectionImagesStatisticsList statisticsInspectionList(opts)

A mixin that only allows retrieving entities by id.

### Example

```javascript
import Avis from "avis";
let defaultClient = Avis.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications["cookieAuth"];
cookieAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications["ApiKeyAuth"];
ApiKeyAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new Avis.StatisticsApi();
let opts = {
  page: 56, // Number | A page number within the paginated result set.
  pageSize: 56, // Number | Number of results to return per page.
};
apiInstance.statisticsInspectionList(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name         | Type       | Description                                    | Notes      |
| ------------ | ---------- | ---------------------------------------------- | ---------- |
| **page**     | **Number** | A page number within the paginated result set. | [optional] |
| **pageSize** | **Number** | Number of results to return per page.          | [optional] |

### Return type

[**PaginatedInspectionImagesStatisticsList**](PaginatedInspectionImagesStatisticsList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## statisticsInspectionRetrieve

> InspectionImagesStatistics statisticsInspectionRetrieve(id)

A mixin that only allows retrieving entities by id.

### Example

```javascript
import Avis from "avis";
let defaultClient = Avis.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications["cookieAuth"];
cookieAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications["ApiKeyAuth"];
ApiKeyAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new Avis.StatisticsApi();
let id = 56; // Number | A unique integer value identifying this image.
apiInstance.statisticsInspectionRetrieve(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name   | Type       | Description                                    | Notes |
| ------ | ---------- | ---------------------------------------------- | ----- |
| **id** | **Number** | A unique integer value identifying this image. |

### Return type

[**InspectionImagesStatistics**](InspectionImagesStatistics.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## statisticsInspectionUpdate

> InspectionImagesStatistics statisticsInspectionUpdate(id, inspectionImagesStatisticsRequest)

A mixin that only allows retrieving entities by id.

### Example

```javascript
import Avis from "avis";
let defaultClient = Avis.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications["cookieAuth"];
cookieAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications["ApiKeyAuth"];
ApiKeyAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new Avis.StatisticsApi();
let id = 56; // Number | A unique integer value identifying this image.
let inspectionImagesStatisticsRequest =
  new Avis.InspectionImagesStatisticsRequest(); // InspectionImagesStatisticsRequest |
apiInstance.statisticsInspectionUpdate(
  id,
  inspectionImagesStatisticsRequest,
  (error, data, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log("API called successfully. Returned data: " + data);
    }
  },
);
```

### Parameters

| Name                                  | Type                                                                          | Description                                    | Notes |
| ------------------------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------- | ----- |
| **id**                                | **Number**                                                                    | A unique integer value identifying this image. |
| **inspectionImagesStatisticsRequest** | [**InspectionImagesStatisticsRequest**](InspectionImagesStatisticsRequest.md) |                                                |

### Return type

[**InspectionImagesStatistics**](InspectionImagesStatistics.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## statisticsTeamCreate

> InspectionStatistics statisticsTeamCreate(inspectionStatisticsRequest)

A mixin that only allows retrieving entities by id.

### Example

```javascript
import Avis from "avis";
let defaultClient = Avis.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications["cookieAuth"];
cookieAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications["ApiKeyAuth"];
ApiKeyAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new Avis.StatisticsApi();
let inspectionStatisticsRequest = new Avis.InspectionStatisticsRequest(); // InspectionStatisticsRequest |
apiInstance.statisticsTeamCreate(
  inspectionStatisticsRequest,
  (error, data, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log("API called successfully. Returned data: " + data);
    }
  },
);
```

### Parameters

| Name                            | Type                                                              | Description | Notes |
| ------------------------------- | ----------------------------------------------------------------- | ----------- | ----- |
| **inspectionStatisticsRequest** | [**InspectionStatisticsRequest**](InspectionStatisticsRequest.md) |             |

### Return type

[**InspectionStatistics**](InspectionStatistics.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

## statisticsTeamDestroy

> statisticsTeamDestroy(id)

A mixin that only allows retrieving entities by id.

### Example

```javascript
import Avis from "avis";
let defaultClient = Avis.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications["cookieAuth"];
cookieAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications["ApiKeyAuth"];
ApiKeyAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new Avis.StatisticsApi();
let id = 56; // Number | A unique integer value identifying this inspection.
apiInstance.statisticsTeamDestroy(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully.");
  }
});
```

### Parameters

| Name   | Type       | Description                                         | Notes |
| ------ | ---------- | --------------------------------------------------- | ----- |
| **id** | **Number** | A unique integer value identifying this inspection. |

### Return type

null (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

## statisticsTeamList

> PaginatedInspectionStatisticsList statisticsTeamList(opts)

A mixin that only allows retrieving entities by id.

### Example

```javascript
import Avis from "avis";
let defaultClient = Avis.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications["cookieAuth"];
cookieAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications["ApiKeyAuth"];
ApiKeyAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new Avis.StatisticsApi();
let opts = {
  page: 56, // Number | A page number within the paginated result set.
  pageSize: 56, // Number | Number of results to return per page.
};
apiInstance.statisticsTeamList(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name         | Type       | Description                                    | Notes      |
| ------------ | ---------- | ---------------------------------------------- | ---------- |
| **page**     | **Number** | A page number within the paginated result set. | [optional] |
| **pageSize** | **Number** | Number of results to return per page.          | [optional] |

### Return type

[**PaginatedInspectionStatisticsList**](PaginatedInspectionStatisticsList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## statisticsTeamRetrieve

> InspectionStatistics statisticsTeamRetrieve(id)

A mixin that only allows retrieving entities by id.

### Example

```javascript
import Avis from "avis";
let defaultClient = Avis.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications["cookieAuth"];
cookieAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications["ApiKeyAuth"];
ApiKeyAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new Avis.StatisticsApi();
let id = 56; // Number | A unique integer value identifying this inspection.
apiInstance.statisticsTeamRetrieve(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log("API called successfully. Returned data: " + data);
  }
});
```

### Parameters

| Name   | Type       | Description                                         | Notes |
| ------ | ---------- | --------------------------------------------------- | ----- |
| **id** | **Number** | A unique integer value identifying this inspection. |

### Return type

[**InspectionStatistics**](InspectionStatistics.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## statisticsTeamUpdate

> InspectionStatistics statisticsTeamUpdate(id, inspectionStatisticsRequest)

A mixin that only allows retrieving entities by id.

### Example

```javascript
import Avis from "avis";
let defaultClient = Avis.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications["cookieAuth"];
cookieAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications["ApiKeyAuth"];
ApiKeyAuth.apiKey = "YOUR API KEY";
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new Avis.StatisticsApi();
let id = 56; // Number | A unique integer value identifying this inspection.
let inspectionStatisticsRequest = new Avis.InspectionStatisticsRequest(); // InspectionStatisticsRequest |
apiInstance.statisticsTeamUpdate(
  id,
  inspectionStatisticsRequest,
  (error, data, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log("API called successfully. Returned data: " + data);
    }
  },
);
```

### Parameters

| Name                            | Type                                                              | Description                                         | Notes |
| ------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------- | ----- |
| **id**                          | **Number**                                                        | A unique integer value identifying this inspection. |
| **inspectionStatisticsRequest** | [**InspectionStatisticsRequest**](InspectionStatisticsRequest.md) |                                                     |

### Return type

[**InspectionStatistics**](InspectionStatistics.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json
