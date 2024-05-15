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
 * The ImageAttributeRequest model module.
 * @module model/ImageAttributeRequest
 * @version 0.8.0
 */
class ImageAttributeRequest {
  /**
   * Constructs a new <code>ImageAttributeRequest</code>.
   * @alias module:model/ImageAttributeRequest
   * @param team {Number}
   * @param category {Number}
   */
  constructor(team, category) {
    ImageAttributeRequest.initialize(this, team, category);
  }

  /**
   * Initializes the fields of this object.
   * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
   * Only for internal use.
   */
  static initialize(obj, team, category) {
    obj["team"] = team;
    obj["category"] = category;
  }

  /**
   * Constructs a <code>ImageAttributeRequest</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/ImageAttributeRequest} obj Optional instance to populate.
   * @return {module:model/ImageAttributeRequest} The populated <code>ImageAttributeRequest</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new ImageAttributeRequest();

      if (data.hasOwnProperty("team")) {
        obj["team"] = ApiClient.convertToType(data["team"], "Number");
      }
      if (data.hasOwnProperty("category")) {
        obj["category"] = ApiClient.convertToType(data["category"], "Number");
      }
      if (data.hasOwnProperty("results")) {
        obj["results"] = ApiClient.convertToType(data["results"], ["Number"]);
      }
      if (data.hasOwnProperty("value")) {
        obj["value"] = ApiClient.convertToType(data["value"], "String");
      }
    }
    return obj;
  }

  /**
   * Validates the JSON data with respect to <code>ImageAttributeRequest</code>.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ImageAttributeRequest</code>.
   */
  static validateJSON(data) {
    // check to make sure all required properties are present in the JSON string
    for (const property of ImageAttributeRequest.RequiredProperties) {
      if (!data[property]) {
        throw new Error(
          "The required field `" +
            property +
            "` is not found in the JSON data: " +
            JSON.stringify(data),
        );
      }
    }
    // ensure the json data is an array
    if (!Array.isArray(data["results"])) {
      throw new Error(
        "Expected the field `results` to be an array in the JSON data but got " +
          data["results"],
      );
    }
    // ensure the json data is a string
    if (
      data["value"] &&
      !(typeof data["value"] === "string" || data["value"] instanceof String)
    ) {
      throw new Error(
        "Expected the field `value` to be a primitive type in the JSON string but got " +
          data["value"],
      );
    }

    return true;
  }
}

ImageAttributeRequest.RequiredProperties = ["team", "category"];

/**
 * @member {Number} team
 */
ImageAttributeRequest.prototype["team"] = undefined;

/**
 * @member {Number} category
 */
ImageAttributeRequest.prototype["category"] = undefined;

/**
 * @member {Array.<Number>} results
 */
ImageAttributeRequest.prototype["results"] = undefined;

/**
 * @member {String} value
 */
ImageAttributeRequest.prototype["value"] = undefined;

export default ImageAttributeRequest;
