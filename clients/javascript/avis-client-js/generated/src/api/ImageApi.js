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
import FormatEnum from "../model/FormatEnum";
import Image from "../model/Image";
import ImageRequest from "../model/ImageRequest";
import PaginatedImageList from "../model/PaginatedImageList";
import PaginatedQualityCriteriaResultList from "../model/PaginatedQualityCriteriaResultList";
import PatchedImageRequest from "../model/PatchedImageRequest";
import ValidationStatusEnum from "../model/ValidationStatusEnum";

/**
 * Image service.
 * @module api/ImageApi
 * @version 0.8.0
 */
export default class ImageApi {
  /**
   * Constructs a new ImageApi.
   * @alias module:api/ImageApi
   * @class
   * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
   * default to {@link module:ApiClient#instance} if unspecified.
   */
  constructor(apiClient) {
    this.apiClient = apiClient || ApiClient.instance;
  }

  /**
   * Callback function to receive the result of the imageCreate operation.
   * @callback module:api/ImageApi~imageCreateCallback
   * @param {String} error Error message, if any.
   * @param {module:model/Image} data The data returned by the service call.
   * @param {String} response The complete HTTP response.
   */

  /**
   * A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)
   * @param {Number} team
   * @param {Date} captureDatetime
   * @param {File} file
   * @param {Object} opts Optional parameters
   * @param {Number} [inspection]
   * @param {Number} [uploadedBy]
   * @param {Array.<Number>} [results]
   * @param {module:model/FormatEnum} [format]
   * @param {String} [partId]
   * @param {module:model/ValidationStatusEnum} [validationStatus]
   * @param {module:api/ImageApi~imageCreateCallback} callback The callback function, accepting three arguments: error, data, response
   * data is of type: {@link module:model/Image}
   */
  imageCreate(team, captureDatetime, file, opts, callback) {
    opts = opts || {};
    let postBody = null;
    // verify the required parameter 'team' is set
    if (team === undefined || team === null) {
      throw new Error(
        "Missing the required parameter 'team' when calling imageCreate",
      );
    }
    // verify the required parameter 'captureDatetime' is set
    if (captureDatetime === undefined || captureDatetime === null) {
      throw new Error(
        "Missing the required parameter 'captureDatetime' when calling imageCreate",
      );
    }
    // verify the required parameter 'file' is set
    if (file === undefined || file === null) {
      throw new Error(
        "Missing the required parameter 'file' when calling imageCreate",
      );
    }

    let pathParams = {};
    let queryParams = {};
    let headerParams = {};
    let formParams = {
      team: team,
      inspection: opts["inspection"],
      uploaded_by: opts["uploadedBy"],
      results: this.apiClient.buildCollectionParam(opts["results"], "csv"),
      format: opts["format"],
      capture_datetime: captureDatetime,
      file: file,
      part_id: opts["partId"],
      validation_status: opts["validationStatus"],
    };

    let authNames = ["cookieAuth", "ApiKeyAuth"];
    let contentTypes = ["multipart/form-data"];
    let accepts = ["application/json"];
    let returnType = Image;
    return this.apiClient.callApi(
      "/api/image/",
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
   * Callback function to receive the result of the imageDestroy operation.
   * @callback module:api/ImageApi~imageDestroyCallback
   * @param {String} error Error message, if any.
   * @param data This operation does not return a value.
   * @param {String} response The complete HTTP response.
   */

  /**
   * A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)
   * @param {Number} id A unique integer value identifying this image.
   * @param {module:api/ImageApi~imageDestroyCallback} callback The callback function, accepting three arguments: error, data, response
   */
  imageDestroy(id, callback) {
    let postBody = null;
    // verify the required parameter 'id' is set
    if (id === undefined || id === null) {
      throw new Error(
        "Missing the required parameter 'id' when calling imageDestroy",
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
      "/api/image/{id}/",
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
   * Callback function to receive the result of the imageList operation.
   * @callback module:api/ImageApi~imageListCallback
   * @param {String} error Error message, if any.
   * @param {module:model/PaginatedImageList} data The data returned by the service call.
   * @param {String} response The complete HTTP response.
   */

  /**
   * A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)
   * @param {Object} opts Optional parameters
   * @param {String} [fields]
   * @param {Array.<Number>} [id] Multiple values may be separated by commas.
   * @param {String} [ordering] Which field to use when ordering the results.
   * @param {Number} [page] A page number within the paginated result set.
   * @param {Number} [pageSize] Number of results to return per page.
   * @param {module:api/ImageApi~imageListCallback} callback The callback function, accepting three arguments: error, data, response
   * data is of type: {@link module:model/PaginatedImageList}
   */
  imageList(opts, callback) {
    opts = opts || {};
    let postBody = null;

    let pathParams = {};
    let queryParams = {
      fields: opts["fields"],
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
    let returnType = PaginatedImageList;
    return this.apiClient.callApi(
      "/api/image/",
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
   * Callback function to receive the result of the imagePartialUpdate operation.
   * @callback module:api/ImageApi~imagePartialUpdateCallback
   * @param {String} error Error message, if any.
   * @param {module:model/Image} data The data returned by the service call.
   * @param {String} response The complete HTTP response.
   */

  /**
   * A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)
   * @param {Number} id A unique integer value identifying this image.
   * @param {Object} opts Optional parameters
   * @param {module:model/PatchedImageRequest} [patchedImageRequest]
   * @param {module:api/ImageApi~imagePartialUpdateCallback} callback The callback function, accepting three arguments: error, data, response
   * data is of type: {@link module:model/Image}
   */
  imagePartialUpdate(id, opts, callback) {
    opts = opts || {};
    let postBody = opts["patchedImageRequest"];
    // verify the required parameter 'id' is set
    if (id === undefined || id === null) {
      throw new Error(
        "Missing the required parameter 'id' when calling imagePartialUpdate",
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
    let returnType = Image;
    return this.apiClient.callApi(
      "/api/image/{id}/",
      "PATCH",
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
   * Callback function to receive the result of the imageQualityList operation.
   * @callback module:api/ImageApi~imageQualityListCallback
   * @param {String} error Error message, if any.
   * @param {module:model/PaginatedQualityCriteriaResultList} data The data returned by the service call.
   * @param {String} response The complete HTTP response.
   */

  /**
   * A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)
   * @param {Object} opts Optional parameters
   * @param {Array.<Number>} [id] Multiple values may be separated by commas.
   * @param {String} [ordering] Which field to use when ordering the results.
   * @param {Number} [page] A page number within the paginated result set.
   * @param {Number} [pageSize] Number of results to return per page.
   * @param {module:api/ImageApi~imageQualityListCallback} callback The callback function, accepting three arguments: error, data, response
   * data is of type: {@link module:model/PaginatedQualityCriteriaResultList}
   */
  imageQualityList(opts, callback) {
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
    let returnType = PaginatedQualityCriteriaResultList;
    return this.apiClient.callApi(
      "/api/image/quality/",
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
   * Callback function to receive the result of the imageRetrieve operation.
   * @callback module:api/ImageApi~imageRetrieveCallback
   * @param {String} error Error message, if any.
   * @param {module:model/Image} data The data returned by the service call.
   * @param {String} response The complete HTTP response.
   */

  /**
   * A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)
   * @param {Number} id A unique integer value identifying this image.
   * @param {Object} opts Optional parameters
   * @param {String} [fields]
   * @param {module:api/ImageApi~imageRetrieveCallback} callback The callback function, accepting three arguments: error, data, response
   * data is of type: {@link module:model/Image}
   */
  imageRetrieve(id, opts, callback) {
    opts = opts || {};
    let postBody = null;
    // verify the required parameter 'id' is set
    if (id === undefined || id === null) {
      throw new Error(
        "Missing the required parameter 'id' when calling imageRetrieve",
      );
    }

    let pathParams = {
      id: id,
    };
    let queryParams = {
      fields: opts["fields"],
    };
    let headerParams = {};
    let formParams = {};

    let authNames = ["cookieAuth", "ApiKeyAuth"];
    let contentTypes = [];
    let accepts = ["application/json"];
    let returnType = Image;
    return this.apiClient.callApi(
      "/api/image/{id}/",
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
   * Callback function to receive the result of the imageUpdate operation.
   * @callback module:api/ImageApi~imageUpdateCallback
   * @param {String} error Error message, if any.
   * @param {module:model/Image} data The data returned by the service call.
   * @param {String} response The complete HTTP response.
   */

  /**
   * A base viewset that allows reading, creating and updating objects. The following functionalities are added by the mixins:  * CreateModelMixin: allows creating objects * UpdateModelMixin: allows updating objects * DestroyModelMixin: allows deleting objects * OptimizedReadOnlyTracedViewSet: allows reading objects and adds tracing and optimized queryset fetching (with the use of the `fields` query parameter)
   * @param {Number} id A unique integer value identifying this image.
   * @param {module:model/ImageRequest} imageRequest
   * @param {module:api/ImageApi~imageUpdateCallback} callback The callback function, accepting three arguments: error, data, response
   * data is of type: {@link module:model/Image}
   */
  imageUpdate(id, imageRequest, callback) {
    let postBody = imageRequest;
    // verify the required parameter 'id' is set
    if (id === undefined || id === null) {
      throw new Error(
        "Missing the required parameter 'id' when calling imageUpdate",
      );
    }
    // verify the required parameter 'imageRequest' is set
    if (imageRequest === undefined || imageRequest === null) {
      throw new Error(
        "Missing the required parameter 'imageRequest' when calling imageUpdate",
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
    let returnType = Image;
    return this.apiClient.callApi(
      "/api/image/{id}/",
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