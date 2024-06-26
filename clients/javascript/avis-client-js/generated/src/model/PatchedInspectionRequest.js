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

/**
 * The PatchedInspectionRequest model module.
 * @module model/PatchedInspectionRequest
 * @version 0.8.0
 */
class PatchedInspectionRequest {
  /**
   * Constructs a new <code>PatchedInspectionRequest</code>.
   * @alias module:model/PatchedInspectionRequest
   */
  constructor() {
    PatchedInspectionRequest.initialize(this);
  }

  /**
   * Initializes the fields of this object.
   * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
   * Only for internal use.
   */
  static initialize(obj) {}

  /**
   * Constructs a <code>PatchedInspectionRequest</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/PatchedInspectionRequest} obj Optional instance to populate.
   * @return {module:model/PatchedInspectionRequest} The populated <code>PatchedInspectionRequest</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new PatchedInspectionRequest();

      if (data.hasOwnProperty("team")) {
        obj["team"] = ApiClient.convertToType(data["team"], "Number");
      }
      if (data.hasOwnProperty("product")) {
        obj["product"] = ApiClient.convertToType(data["product"], "Number");
      }
      if (data.hasOwnProperty("opened_by")) {
        obj["opened_by"] = ApiClient.convertToType(data["opened_by"], "Number");
      }
      if (data.hasOwnProperty("closed_by")) {
        obj["closed_by"] = ApiClient.convertToType(data["closed_by"], "Number");
      }
      if (data.hasOwnProperty("images")) {
        obj["images"] = ApiClient.convertToType(data["images"], ["Number"]);
      }
      if (data.hasOwnProperty("close_datetime")) {
        obj["close_datetime"] = ApiClient.convertToType(
          data["close_datetime"],
          "Date",
        );
      }
      if (data.hasOwnProperty("configuration")) {
        obj["configuration"] = ApiClient.convertToType(
          data["configuration"],
          "Number",
        );
      }
      if (data.hasOwnProperty("metadata")) {
        obj["metadata"] = ApiClient.convertToType(data["metadata"], "Number");
      }
    }
    return obj;
  }

  /**
   * Validates the JSON data with respect to <code>PatchedInspectionRequest</code>.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PatchedInspectionRequest</code>.
   */
  static validateJSON(data) {
    // ensure the json data is an array
    if (!Array.isArray(data["images"])) {
      throw new Error(
        "Expected the field `images` to be an array in the JSON data but got " +
          data["images"],
      );
    }

    return true;
  }
}

/**
 * @member {Number} team
 */
PatchedInspectionRequest.prototype["team"] = undefined;

/**
 * @member {Number} product
 */
PatchedInspectionRequest.prototype["product"] = undefined;

/**
 * @member {Number} opened_by
 */
PatchedInspectionRequest.prototype["opened_by"] = undefined;

/**
 * @member {Number} closed_by
 */
PatchedInspectionRequest.prototype["closed_by"] = undefined;

/**
 * @member {Array.<Number>} images
 */
PatchedInspectionRequest.prototype["images"] = undefined;

/**
 * @member {Date} close_datetime
 */
PatchedInspectionRequest.prototype["close_datetime"] = undefined;

/**
 * @member {Number} configuration
 */
PatchedInspectionRequest.prototype["configuration"] = undefined;

/**
 * @member {Number} metadata
 */
PatchedInspectionRequest.prototype["metadata"] = undefined;

export default PatchedInspectionRequest;
