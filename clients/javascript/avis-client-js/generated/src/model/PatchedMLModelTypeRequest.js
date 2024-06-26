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
 * The PatchedMLModelTypeRequest model module.
 * @module model/PatchedMLModelTypeRequest
 * @version 0.8.0
 */
class PatchedMLModelTypeRequest {
  /**
   * Constructs a new <code>PatchedMLModelTypeRequest</code>.
   * @alias module:model/PatchedMLModelTypeRequest
   */
  constructor() {
    PatchedMLModelTypeRequest.initialize(this);
  }

  /**
   * Initializes the fields of this object.
   * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
   * Only for internal use.
   */
  static initialize(obj) {}

  /**
   * Constructs a <code>PatchedMLModelTypeRequest</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/PatchedMLModelTypeRequest} obj Optional instance to populate.
   * @return {module:model/PatchedMLModelTypeRequest} The populated <code>PatchedMLModelTypeRequest</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new PatchedMLModelTypeRequest();

      if (data.hasOwnProperty("slug")) {
        obj["slug"] = ApiClient.convertToType(data["slug"], "String");
      }
      if (data.hasOwnProperty("name")) {
        obj["name"] = ApiClient.convertToType(data["name"], "String");
      }
      if (data.hasOwnProperty("description")) {
        obj["description"] = ApiClient.convertToType(
          data["description"],
          "String",
        );
      }
    }
    return obj;
  }

  /**
   * Validates the JSON data with respect to <code>PatchedMLModelTypeRequest</code>.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PatchedMLModelTypeRequest</code>.
   */
  static validateJSON(data) {
    // ensure the json data is a string
    if (
      data["slug"] &&
      !(typeof data["slug"] === "string" || data["slug"] instanceof String)
    ) {
      throw new Error(
        "Expected the field `slug` to be a primitive type in the JSON string but got " +
          data["slug"],
      );
    }
    // ensure the json data is a string
    if (
      data["name"] &&
      !(typeof data["name"] === "string" || data["name"] instanceof String)
    ) {
      throw new Error(
        "Expected the field `name` to be a primitive type in the JSON string but got " +
          data["name"],
      );
    }
    // ensure the json data is a string
    if (
      data["description"] &&
      !(
        typeof data["description"] === "string" ||
        data["description"] instanceof String
      )
    ) {
      throw new Error(
        "Expected the field `description` to be a primitive type in the JSON string but got " +
          data["description"],
      );
    }

    return true;
  }
}

/**
 * @member {String} slug
 */
PatchedMLModelTypeRequest.prototype["slug"] = undefined;

/**
 * @member {String} name
 */
PatchedMLModelTypeRequest.prototype["name"] = undefined;

/**
 * @member {String} description
 */
PatchedMLModelTypeRequest.prototype["description"] = undefined;

export default PatchedMLModelTypeRequest;
