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
 * The PatchedQualityCriteriaRequest model module.
 * @module model/PatchedQualityCriteriaRequest
 * @version 0.8.0
 */
class PatchedQualityCriteriaRequest {
  /**
   * Constructs a new <code>PatchedQualityCriteriaRequest</code>.
   * @alias module:model/PatchedQualityCriteriaRequest
   */
  constructor() {
    PatchedQualityCriteriaRequest.initialize(this);
  }

  /**
   * Initializes the fields of this object.
   * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
   * Only for internal use.
   */
  static initialize(obj) {}

  /**
   * Constructs a <code>PatchedQualityCriteriaRequest</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/PatchedQualityCriteriaRequest} obj Optional instance to populate.
   * @return {module:model/PatchedQualityCriteriaRequest} The populated <code>PatchedQualityCriteriaRequest</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new PatchedQualityCriteriaRequest();

      if (data.hasOwnProperty("team")) {
        obj["team"] = ApiClient.convertToType(data["team"], "Number");
      }
      if (data.hasOwnProperty("configurations")) {
        obj["configurations"] = ApiClient.convertToType(
          data["configurations"],
          ["Number"],
        );
      }
      if (data.hasOwnProperty("good_quality_classes")) {
        obj["good_quality_classes"] = ApiClient.convertToType(
          data["good_quality_classes"],
          ["String"],
        );
      }
      if (data.hasOwnProperty("uncertain_quality_classes")) {
        obj["uncertain_quality_classes"] = ApiClient.convertToType(
          data["uncertain_quality_classes"],
          ["String"],
        );
      }
      if (data.hasOwnProperty("bad_quality_classes")) {
        obj["bad_quality_classes"] = ApiClient.convertToType(
          data["bad_quality_classes"],
          ["String"],
        );
      }
    }
    return obj;
  }

  /**
   * Validates the JSON data with respect to <code>PatchedQualityCriteriaRequest</code>.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PatchedQualityCriteriaRequest</code>.
   */
  static validateJSON(data) {
    // ensure the json data is an array
    if (!Array.isArray(data["configurations"])) {
      throw new Error(
        "Expected the field `configurations` to be an array in the JSON data but got " +
          data["configurations"],
      );
    }
    // ensure the json data is an array
    if (!Array.isArray(data["good_quality_classes"])) {
      throw new Error(
        "Expected the field `good_quality_classes` to be an array in the JSON data but got " +
          data["good_quality_classes"],
      );
    }
    // ensure the json data is an array
    if (!Array.isArray(data["uncertain_quality_classes"])) {
      throw new Error(
        "Expected the field `uncertain_quality_classes` to be an array in the JSON data but got " +
          data["uncertain_quality_classes"],
      );
    }
    // ensure the json data is an array
    if (!Array.isArray(data["bad_quality_classes"])) {
      throw new Error(
        "Expected the field `bad_quality_classes` to be an array in the JSON data but got " +
          data["bad_quality_classes"],
      );
    }

    return true;
  }
}

/**
 * @member {Number} team
 */
PatchedQualityCriteriaRequest.prototype["team"] = undefined;

/**
 * @member {Array.<Number>} configurations
 */
PatchedQualityCriteriaRequest.prototype["configurations"] = undefined;

/**
 * @member {Array.<String>} good_quality_classes
 */
PatchedQualityCriteriaRequest.prototype["good_quality_classes"] = undefined;

/**
 * @member {Array.<String>} uncertain_quality_classes
 */
PatchedQualityCriteriaRequest.prototype["uncertain_quality_classes"] =
  undefined;

/**
 * @member {Array.<String>} bad_quality_classes
 */
PatchedQualityCriteriaRequest.prototype["bad_quality_classes"] = undefined;

export default PatchedQualityCriteriaRequest;
