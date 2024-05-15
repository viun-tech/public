/**
 * avis
 * VUE Autonomous Visual Inspection System (AVIS)
 *
 * The version of the OpenAPI document: 0.8.0
 *
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from "../ApiClient";
import ConfigurationStatistics from "../model/ConfigurationStatistics";
import ConfigurationStatisticsRequest from "../model/ConfigurationStatisticsRequest";
import InspectionImagesStatistics from "../model/InspectionImagesStatistics";
import InspectionImagesStatisticsRequest from "../model/InspectionImagesStatisticsRequest";
import InspectionStatistics from "../model/InspectionStatistics";
import InspectionStatisticsRequest from "../model/InspectionStatisticsRequest";
import PaginatedConfigurationStatisticsList from "../model/PaginatedConfigurationStatisticsList";
import PaginatedInspectionImagesStatisticsList from "../model/PaginatedInspectionImagesStatisticsList";
import PaginatedInspectionStatisticsList from "../model/PaginatedInspectionStatisticsList";

/**
 * Statistics service.
 * @module api/StatisticsApi
 * @version 0.8.0
 */
export default class StatisticsApi {
  /**
   * Constructs a new StatisticsApi.
   * @alias module:api/StatisticsApi
   * @class
   * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
   * default to {@link module:ApiClient#instance} if unspecified.
   */
  constructor(apiClient) {
    this.apiClient = apiClient || ApiClient.instance;
  }

  /**
   * Callback function to receive the result of the statisticsConfigurationCreate operation.
   * @callback module:api/StatisticsApi~statisticsConfigurationCreateCallback
   * @param {String} error Error message, if any.
   * @param {module:model/ConfigurationStatistics} data The data returned by the service call.
   * @param {String} response The complete HTTP response.
   */

  /**
   * A mixin that allows reading entities (listing and retrieving by id).
   * @param {module:model/ConfigurationStatisticsRequest} configurationStatisticsRequest
   * @param {module:api/StatisticsApi~statisticsConfigurationCreateCallback} callback The callback function, accepting three arguments: error, data, response
   * data is of type: {@link module:model/ConfigurationStatistics}
   */
  statisticsConfigurationCreate(configurationStatisticsRequest, callback) {
    let postBody = configurationStatisticsRequest;
    // verify the required parameter 'configurationStatisticsRequest' is set
    if (
      configurationStatisticsRequest === undefined ||
      configurationStatisticsRequest === null
    ) {
      throw new Error(
        "Missing the required parameter 'configurationStatisticsRequest' when calling statisticsConfigurationCreate",
      );
    }

    let pathParams = {};
    let queryParams = {};
    let headerParams = {};
    let formParams = {};

    let authNames = ["cookieAuth", "ApiKeyAuth"];
    let contentTypes = [
      "application/json",
      "application/x-www-form-urlencoded",
      "multipart/form-data",
    ];
    let accepts = ["application/json"];
    let returnType = ConfigurationStatistics;
    return this.apiClient.callApi(
      "/api/statistics/configuration/",
      "POST",
      pathParams,
      queryParams,
      headerParams,
      formParams,
      postBody,
      authNames,
      contentTypes,
      accepts,
      returnType,
      null,
      callback,
    );
  }

  /**
   * Callback function to receive the result of the statisticsConfigurationDestroy operation.
   * @callback module:api/StatisticsApi~statisticsConfigurationDestroyCallback
   * @param {String} error Error message, if any.
   * @param data This operation does not return a value.
   * @param {String} response The complete HTTP response.
   */

  /**
   * A mixin that allows reading entities (listing and retrieving by id).
   * @param {Number} id A unique integer value identifying this configuration.
   * @param {module:api/StatisticsApi~statisticsConfigurationDestroyCallback} callback The callback function, accepting three arguments: error, data, response
   */
  statisticsConfigurationDestroy(id, callback) {
    let postBody = null;
    // verify the required parameter 'id' is set
    if (id === undefined || id === null) {
      throw new Error(
        "Missing the required parameter 'id' when calling statisticsConfigurationDestroy",
      );
    }

    let pathParams = {
      id: id,
    };
    let queryParams = {};
    let headerParams = {};
    let formParams = {};

    let authNames = ["cookieAuth", "ApiKeyAuth"];
    let contentTypes = [];
    let accepts = [];
    let returnType = null;
    return this.apiClient.callApi(
      "/api/statistics/configuration/{id}/",
      "DELETE",
      pathParams,
      queryParams,
      headerParams,
      formParams,
      postBody,
      authNames,
      contentTypes,
      accepts,
      returnType,
      null,
      callback,
    );
  }

  /**
   * Callback function to receive the result of the statisticsConfigurationList operation.
   * @callback module:api/StatisticsApi~statisticsConfigurationListCallback
   * @param {String} error Error message, if any.
   * @param {module:model/PaginatedConfigurationStatisticsList} data The data returned by the service call.
   * @param {String} response The complete HTTP response.
   */

  /**
   * A mixin that allows reading entities (listing and retrieving by id).
   * @param {Object} opts Optional parameters
   * @param {Array.<Number>} [id] Multiple values may be separated by commas.
   * @param {String} [ordering] Which field to use when ordering the results.
   * @param {Number} [page] A page number within the paginated result set.
   * @param {Number} [pageSize] Number of results to return per page.
   * @param {module:api/StatisticsApi~statisticsConfigurationListCallback} callback The callback function, accepting three arguments: error, data, response
   * data is of type: {@link module:model/PaginatedConfigurationStatisticsList}
   */
  statisticsConfigurationList(opts, callback) {
    opts = opts || {};
    let postBody = null;

    let pathParams = {};
    let queryParams = {
      id: this.apiClient.buildCollectionParam(opts["id"], "csv"),
      ordering: opts["ordering"],
      page: opts["page"],
      page_size: opts["pageSize"],
    };
    let headerParams = {};
    let formParams = {};

    let authNames = ["cookieAuth", "ApiKeyAuth"];
    let contentTypes = [];
    let accepts = ["application/json"];
    let returnType = PaginatedConfigurationStatisticsList;
    return this.apiClient.callApi(
      "/api/statistics/configuration/",
      "GET",
      pathParams,
      queryParams,
      headerParams,
      formParams,
      postBody,
      authNames,
      contentTypes,
      accepts,
      returnType,
      null,
      callback,
    );
  }

  /**
   * Callback function to receive the result of the statisticsConfigurationRetrieve operation.
   * @callback module:api/StatisticsApi~statisticsConfigurationRetrieveCallback
   * @param {String} error Error message, if any.
   * @param {module:model/ConfigurationStatistics} data The data returned by the service call.
   * @param {String} response The complete HTTP response.
   */

  /**
   * A mixin that allows reading entities (listing and retrieving by id).
   * @param {Number} id A unique integer value identifying this configuration.
   * @param {module:api/StatisticsApi~statisticsConfigurationRetrieveCallback} callback The callback function, accepting three arguments: error, data, response
   * data is of type: {@link module:model/ConfigurationStatistics}
   */
  statisticsConfigurationRetrieve(id, callback) {
    let postBody = null;
    // verify the required parameter 'id' is set
    if (id === undefined || id === null) {
      throw new Error(
        "Missing the required parameter 'id' when calling statisticsConfigurationRetrieve",
      );
    }

    let pathParams = {
      id: id,
    };
    let queryParams = {};
    let headerParams = {};
    let formParams = {};

    let authNames = ["cookieAuth", "ApiKeyAuth"];
    let contentTypes = [];
    let accepts = ["application/json"];
    let returnType = ConfigurationStatistics;
    return this.apiClient.callApi(
      "/api/statistics/configuration/{id}/",
      "GET",
      pathParams,
      queryParams,
      headerParams,
      formParams,
      postBody,
      authNames,
      contentTypes,
      accepts,
      returnType,
      null,
      callback,
    );
  }

  /**
   * Callback function to receive the result of the statisticsConfigurationUpdate operation.
   * @callback module:api/StatisticsApi~statisticsConfigurationUpdateCallback
   * @param {String} error Error message, if any.
   * @param {module:model/ConfigurationStatistics} data The data returned by the service call.
   * @param {String} response The complete HTTP response.
   */

  /**
   * A mixin that allows reading entities (listing and retrieving by id).
   * @param {Number} id A unique integer value identifying this configuration.
   * @param {module:model/ConfigurationStatisticsRequest} configurationStatisticsRequest
   * @param {module:api/StatisticsApi~statisticsConfigurationUpdateCallback} callback The callback function, accepting three arguments: error, data, response
   * data is of type: {@link module:model/ConfigurationStatistics}
   */
  statisticsConfigurationUpdate(id, configurationStatisticsRequest, callback) {
    let postBody = configurationStatisticsRequest;
    // verify the required parameter 'id' is set
    if (id === undefined || id === null) {
      throw new Error(
        "Missing the required parameter 'id' when calling statisticsConfigurationUpdate",
      );
    }
    // verify the required parameter 'configurationStatisticsRequest' is set
    if (
      configurationStatisticsRequest === undefined ||
      configurationStatisticsRequest === null
    ) {
      throw new Error(
        "Missing the required parameter 'configurationStatisticsRequest' when calling statisticsConfigurationUpdate",
      );
    }

    let pathParams = {
      id: id,
    };
    let queryParams = {};
    let headerParams = {};
    let formParams = {};

    let authNames = ["cookieAuth", "ApiKeyAuth"];
    let contentTypes = [
      "application/json",
      "application/x-www-form-urlencoded",
      "multipart/form-data",
    ];
    let accepts = ["application/json"];
    let returnType = ConfigurationStatistics;
    return this.apiClient.callApi(
      "/api/statistics/configuration/{id}/",
      "PUT",
      pathParams,
      queryParams,
      headerParams,
      formParams,
      postBody,
      authNames,
      contentTypes,
      accepts,
      returnType,
      null,
      callback,
    );
  }

  /**
   * Callback function to receive the result of the statisticsInspectionCreate operation.
   * @callback module:api/StatisticsApi~statisticsInspectionCreateCallback
   * @param {String} error Error message, if any.
   * @param {module:model/InspectionImagesStatistics} data The data returned by the service call.
   * @param {String} response The complete HTTP response.
   */

  /**
   * A mixin that only allows retrieving entities by id.
   * @param {module:model/InspectionImagesStatisticsRequest} inspectionImagesStatisticsRequest
   * @param {module:api/StatisticsApi~statisticsInspectionCreateCallback} callback The callback function, accepting three arguments: error, data, response
   * data is of type: {@link module:model/InspectionImagesStatistics}
   */
  statisticsInspectionCreate(inspectionImagesStatisticsRequest, callback) {
    let postBody = inspectionImagesStatisticsRequest;
    // verify the required parameter 'inspectionImagesStatisticsRequest' is set
    if (
      inspectionImagesStatisticsRequest === undefined ||
      inspectionImagesStatisticsRequest === null
    ) {
      throw new Error(
        "Missing the required parameter 'inspectionImagesStatisticsRequest' when calling statisticsInspectionCreate",
      );
    }

    let pathParams = {};
    let queryParams = {};
    let headerParams = {};
    let formParams = {};

    let authNames = ["cookieAuth", "ApiKeyAuth"];
    let contentTypes = [
      "application/json",
      "application/x-www-form-urlencoded",
      "multipart/form-data",
    ];
    let accepts = ["application/json"];
    let returnType = InspectionImagesStatistics;
    return this.apiClient.callApi(
      "/api/statistics/inspection/",
      "POST",
      pathParams,
      queryParams,
      headerParams,
      formParams,
      postBody,
      authNames,
      contentTypes,
      accepts,
      returnType,
      null,
      callback,
    );
  }

  /**
   * Callback function to receive the result of the statisticsInspectionDestroy operation.
   * @callback module:api/StatisticsApi~statisticsInspectionDestroyCallback
   * @param {String} error Error message, if any.
   * @param data This operation does not return a value.
   * @param {String} response The complete HTTP response.
   */

  /**
   * A mixin that only allows retrieving entities by id.
   * @param {Number} id A unique integer value identifying this image.
   * @param {module:api/StatisticsApi~statisticsInspectionDestroyCallback} callback The callback function, accepting three arguments: error, data, response
   */
  statisticsInspectionDestroy(id, callback) {
    let postBody = null;
    // verify the required parameter 'id' is set
    if (id === undefined || id === null) {
      throw new Error(
        "Missing the required parameter 'id' when calling statisticsInspectionDestroy",
      );
    }

    let pathParams = {
      id: id,
    };
    let queryParams = {};
    let headerParams = {};
    let formParams = {};

    let authNames = ["cookieAuth", "ApiKeyAuth"];
    let contentTypes = [];
    let accepts = [];
    let returnType = null;
    return this.apiClient.callApi(
      "/api/statistics/inspection/{id}/",
      "DELETE",
      pathParams,
      queryParams,
      headerParams,
      formParams,
      postBody,
      authNames,
      contentTypes,
      accepts,
      returnType,
      null,
      callback,
    );
  }

  /**
   * Callback function to receive the result of the statisticsInspectionList operation.
   * @callback module:api/StatisticsApi~statisticsInspectionListCallback
   * @param {String} error Error message, if any.
   * @param {module:model/PaginatedInspectionImagesStatisticsList} data The data returned by the service call.
   * @param {String} response The complete HTTP response.
   */

  /**
   * A mixin that only allows retrieving entities by id.
   * @param {Object} opts Optional parameters
   * @param {Number} [page] A page number within the paginated result set.
   * @param {Number} [pageSize] Number of results to return per page.
   * @param {module:api/StatisticsApi~statisticsInspectionListCallback} callback The callback function, accepting three arguments: error, data, response
   * data is of type: {@link module:model/PaginatedInspectionImagesStatisticsList}
   */
  statisticsInspectionList(opts, callback) {
    opts = opts || {};
    let postBody = null;

    let pathParams = {};
    let queryParams = {
      page: opts["page"],
      page_size: opts["pageSize"],
    };
    let headerParams = {};
    let formParams = {};

    let authNames = ["cookieAuth", "ApiKeyAuth"];
    let contentTypes = [];
    let accepts = ["application/json"];
    let returnType = PaginatedInspectionImagesStatisticsList;
    return this.apiClient.callApi(
      "/api/statistics/inspection/",
      "GET",
      pathParams,
      queryParams,
      headerParams,
      formParams,
      postBody,
      authNames,
      contentTypes,
      accepts,
      returnType,
      null,
      callback,
    );
  }

  /**
   * Callback function to receive the result of the statisticsInspectionRetrieve operation.
   * @callback module:api/StatisticsApi~statisticsInspectionRetrieveCallback
   * @param {String} error Error message, if any.
   * @param {module:model/InspectionImagesStatistics} data The data returned by the service call.
   * @param {String} response The complete HTTP response.
   */

  /**
   * A mixin that only allows retrieving entities by id.
   * @param {Number} id A unique integer value identifying this image.
   * @param {module:api/StatisticsApi~statisticsInspectionRetrieveCallback} callback The callback function, accepting three arguments: error, data, response
   * data is of type: {@link module:model/InspectionImagesStatistics}
   */
  statisticsInspectionRetrieve(id, callback) {
    let postBody = null;
    // verify the required parameter 'id' is set
    if (id === undefined || id === null) {
      throw new Error(
        "Missing the required parameter 'id' when calling statisticsInspectionRetrieve",
      );
    }

    let pathParams = {
      id: id,
    };
    let queryParams = {};
    let headerParams = {};
    let formParams = {};

    let authNames = ["cookieAuth", "ApiKeyAuth"];
    let contentTypes = [];
    let accepts = ["application/json"];
    let returnType = InspectionImagesStatistics;
    return this.apiClient.callApi(
      "/api/statistics/inspection/{id}/",
      "GET",
      pathParams,
      queryParams,
      headerParams,
      formParams,
      postBody,
      authNames,
      contentTypes,
      accepts,
      returnType,
      null,
      callback,
    );
  }

  /**
   * Callback function to receive the result of the statisticsInspectionUpdate operation.
   * @callback module:api/StatisticsApi~statisticsInspectionUpdateCallback
   * @param {String} error Error message, if any.
   * @param {module:model/InspectionImagesStatistics} data The data returned by the service call.
   * @param {String} response The complete HTTP response.
   */

  /**
   * A mixin that only allows retrieving entities by id.
   * @param {Number} id A unique integer value identifying this image.
   * @param {module:model/InspectionImagesStatisticsRequest} inspectionImagesStatisticsRequest
   * @param {module:api/StatisticsApi~statisticsInspectionUpdateCallback} callback The callback function, accepting three arguments: error, data, response
   * data is of type: {@link module:model/InspectionImagesStatistics}
   */
  statisticsInspectionUpdate(id, inspectionImagesStatisticsRequest, callback) {
    let postBody = inspectionImagesStatisticsRequest;
    // verify the required parameter 'id' is set
    if (id === undefined || id === null) {
      throw new Error(
        "Missing the required parameter 'id' when calling statisticsInspectionUpdate",
      );
    }
    // verify the required parameter 'inspectionImagesStatisticsRequest' is set
    if (
      inspectionImagesStatisticsRequest === undefined ||
      inspectionImagesStatisticsRequest === null
    ) {
      throw new Error(
        "Missing the required parameter 'inspectionImagesStatisticsRequest' when calling statisticsInspectionUpdate",
      );
    }

    let pathParams = {
      id: id,
    };
    let queryParams = {};
    let headerParams = {};
    let formParams = {};

    let authNames = ["cookieAuth", "ApiKeyAuth"];
    let contentTypes = [
      "application/json",
      "application/x-www-form-urlencoded",
      "multipart/form-data",
    ];
    let accepts = ["application/json"];
    let returnType = InspectionImagesStatistics;
    return this.apiClient.callApi(
      "/api/statistics/inspection/{id}/",
      "PUT",
      pathParams,
      queryParams,
      headerParams,
      formParams,
      postBody,
      authNames,
      contentTypes,
      accepts,
      returnType,
      null,
      callback,
    );
  }

  /**
   * Callback function to receive the result of the statisticsTeamCreate operation.
   * @callback module:api/StatisticsApi~statisticsTeamCreateCallback
   * @param {String} error Error message, if any.
   * @param {module:model/InspectionStatistics} data The data returned by the service call.
   * @param {String} response The complete HTTP response.
   */

  /**
   * A mixin that only allows retrieving entities by id.
   * @param {module:model/InspectionStatisticsRequest} inspectionStatisticsRequest
   * @param {module:api/StatisticsApi~statisticsTeamCreateCallback} callback The callback function, accepting three arguments: error, data, response
   * data is of type: {@link module:model/InspectionStatistics}
   */
  statisticsTeamCreate(inspectionStatisticsRequest, callback) {
    let postBody = inspectionStatisticsRequest;
    // verify the required parameter 'inspectionStatisticsRequest' is set
    if (
      inspectionStatisticsRequest === undefined ||
      inspectionStatisticsRequest === null
    ) {
      throw new Error(
        "Missing the required parameter 'inspectionStatisticsRequest' when calling statisticsTeamCreate",
      );
    }

    let pathParams = {};
    let queryParams = {};
    let headerParams = {};
    let formParams = {};

    let authNames = ["cookieAuth", "ApiKeyAuth"];
    let contentTypes = [
      "application/json",
      "application/x-www-form-urlencoded",
      "multipart/form-data",
    ];
    let accepts = ["application/json"];
    let returnType = InspectionStatistics;
    return this.apiClient.callApi(
      "/api/statistics/team/",
      "POST",
      pathParams,
      queryParams,
      headerParams,
      formParams,
      postBody,
      authNames,
      contentTypes,
      accepts,
      returnType,
      null,
      callback,
    );
  }

  /**
   * Callback function to receive the result of the statisticsTeamDestroy operation.
   * @callback module:api/StatisticsApi~statisticsTeamDestroyCallback
   * @param {String} error Error message, if any.
   * @param data This operation does not return a value.
   * @param {String} response The complete HTTP response.
   */

  /**
   * A mixin that only allows retrieving entities by id.
   * @param {Number} id A unique integer value identifying this inspection.
   * @param {module:api/StatisticsApi~statisticsTeamDestroyCallback} callback The callback function, accepting three arguments: error, data, response
   */
  statisticsTeamDestroy(id, callback) {
    let postBody = null;
    // verify the required parameter 'id' is set
    if (id === undefined || id === null) {
      throw new Error(
        "Missing the required parameter 'id' when calling statisticsTeamDestroy",
      );
    }

    let pathParams = {
      id: id,
    };
    let queryParams = {};
    let headerParams = {};
    let formParams = {};

    let authNames = ["cookieAuth", "ApiKeyAuth"];
    let contentTypes = [];
    let accepts = [];
    let returnType = null;
    return this.apiClient.callApi(
      "/api/statistics/team/{id}/",
      "DELETE",
      pathParams,
      queryParams,
      headerParams,
      formParams,
      postBody,
      authNames,
      contentTypes,
      accepts,
      returnType,
      null,
      callback,
    );
  }

  /**
   * Callback function to receive the result of the statisticsTeamList operation.
   * @callback module:api/StatisticsApi~statisticsTeamListCallback
   * @param {String} error Error message, if any.
   * @param {module:model/PaginatedInspectionStatisticsList} data The data returned by the service call.
   * @param {String} response The complete HTTP response.
   */

  /**
   * A mixin that only allows retrieving entities by id.
   * @param {Object} opts Optional parameters
   * @param {Number} [page] A page number within the paginated result set.
   * @param {Number} [pageSize] Number of results to return per page.
   * @param {module:api/StatisticsApi~statisticsTeamListCallback} callback The callback function, accepting three arguments: error, data, response
   * data is of type: {@link module:model/PaginatedInspectionStatisticsList}
   */
  statisticsTeamList(opts, callback) {
    opts = opts || {};
    let postBody = null;

    let pathParams = {};
    let queryParams = {
      page: opts["page"],
      page_size: opts["pageSize"],
    };
    let headerParams = {};
    let formParams = {};

    let authNames = ["cookieAuth", "ApiKeyAuth"];
    let contentTypes = [];
    let accepts = ["application/json"];
    let returnType = PaginatedInspectionStatisticsList;
    return this.apiClient.callApi(
      "/api/statistics/team/",
      "GET",
      pathParams,
      queryParams,
      headerParams,
      formParams,
      postBody,
      authNames,
      contentTypes,
      accepts,
      returnType,
      null,
      callback,
    );
  }

  /**
   * Callback function to receive the result of the statisticsTeamRetrieve operation.
   * @callback module:api/StatisticsApi~statisticsTeamRetrieveCallback
   * @param {String} error Error message, if any.
   * @param {module:model/InspectionStatistics} data The data returned by the service call.
   * @param {String} response The complete HTTP response.
   */

  /**
   * A mixin that only allows retrieving entities by id.
   * @param {Number} id A unique integer value identifying this inspection.
   * @param {module:api/StatisticsApi~statisticsTeamRetrieveCallback} callback The callback function, accepting three arguments: error, data, response
   * data is of type: {@link module:model/InspectionStatistics}
   */
  statisticsTeamRetrieve(id, callback) {
    let postBody = null;
    // verify the required parameter 'id' is set
    if (id === undefined || id === null) {
      throw new Error(
        "Missing the required parameter 'id' when calling statisticsTeamRetrieve",
      );
    }

    let pathParams = {
      id: id,
    };
    let queryParams = {};
    let headerParams = {};
    let formParams = {};

    let authNames = ["cookieAuth", "ApiKeyAuth"];
    let contentTypes = [];
    let accepts = ["application/json"];
    let returnType = InspectionStatistics;
    return this.apiClient.callApi(
      "/api/statistics/team/{id}/",
      "GET",
      pathParams,
      queryParams,
      headerParams,
      formParams,
      postBody,
      authNames,
      contentTypes,
      accepts,
      returnType,
      null,
      callback,
    );
  }

  /**
   * Callback function to receive the result of the statisticsTeamUpdate operation.
   * @callback module:api/StatisticsApi~statisticsTeamUpdateCallback
   * @param {String} error Error message, if any.
   * @param {module:model/InspectionStatistics} data The data returned by the service call.
   * @param {String} response The complete HTTP response.
   */

  /**
   * A mixin that only allows retrieving entities by id.
   * @param {Number} id A unique integer value identifying this inspection.
   * @param {module:model/InspectionStatisticsRequest} inspectionStatisticsRequest
   * @param {module:api/StatisticsApi~statisticsTeamUpdateCallback} callback The callback function, accepting three arguments: error, data, response
   * data is of type: {@link module:model/InspectionStatistics}
   */
  statisticsTeamUpdate(id, inspectionStatisticsRequest, callback) {
    let postBody = inspectionStatisticsRequest;
    // verify the required parameter 'id' is set
    if (id === undefined || id === null) {
      throw new Error(
        "Missing the required parameter 'id' when calling statisticsTeamUpdate",
      );
    }
    // verify the required parameter 'inspectionStatisticsRequest' is set
    if (
      inspectionStatisticsRequest === undefined ||
      inspectionStatisticsRequest === null
    ) {
      throw new Error(
        "Missing the required parameter 'inspectionStatisticsRequest' when calling statisticsTeamUpdate",
      );
    }

    let pathParams = {
      id: id,
    };
    let queryParams = {};
    let headerParams = {};
    let formParams = {};

    let authNames = ["cookieAuth", "ApiKeyAuth"];
    let contentTypes = [
      "application/json",
      "application/x-www-form-urlencoded",
      "multipart/form-data",
    ];
    let accepts = ["application/json"];
    let returnType = InspectionStatistics;
    return this.apiClient.callApi(
      "/api/statistics/team/{id}/",
      "PUT",
      pathParams,
      queryParams,
      headerParams,
      formParams,
      postBody,
      authNames,
      contentTypes,
      accepts,
      returnType,
      null,
      callback,
    );
  }
}