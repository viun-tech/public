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
import ConfigurationType from "./ConfigurationType";

/**
 * The PaginatedConfigurationTypeList model module.
 * @module model/PaginatedConfigurationTypeList
 * @version 0.8.0
 */
class PaginatedConfigurationTypeList {
  /**
   * Constructs a new <code>PaginatedConfigurationTypeList</code>.
   * @alias module:model/PaginatedConfigurationTypeList
   * @param count {Number}
   * @param results {Array.<module:model/ConfigurationType>}
   */
  constructor(count, results) {
    PaginatedConfigurationTypeList.initialize(this, count, results);
  }

  /**
   * Initializes the fields of this object.
   * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
   * Only for internal use.
   */
  static initialize(obj, count, results) {
    obj["count"] = count;
    obj["results"] = results;
  }

  /**
   * Constructs a <code>PaginatedConfigurationTypeList</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/PaginatedConfigurationTypeList} obj Optional instance to populate.
   * @return {module:model/PaginatedConfigurationTypeList} The populated <code>PaginatedConfigurationTypeList</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new PaginatedConfigurationTypeList();

      if (data.hasOwnProperty("count")) {
        obj["count"] = ApiClient.convertToType(data["count"], "Number");
      }
      if (data.hasOwnProperty("next")) {
        obj["next"] = ApiClient.convertToType(data["next"], "String");
      }
      if (data.hasOwnProperty("previous")) {
        obj["previous"] = ApiClient.convertToType(data["previous"], "String");
      }
      if (data.hasOwnProperty("results")) {
        obj["results"] = ApiClient.convertToType(data["results"], [
          ConfigurationType,
        ]);
      }
    }
    return obj;
  }

  /**
   * Validates the JSON data with respect to <code>PaginatedConfigurationTypeList</code>.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PaginatedConfigurationTypeList</code>.
   */
  static validateJSON(data) {
    // check to make sure all required properties are present in the JSON string
    for (const property of PaginatedConfigurationTypeList.RequiredProperties) {
      if (!data[property]) {
        throw new Error(
          "The required field `" +
            property +
            "` is not found in the JSON data: " +
            JSON.stringify(data),
        );
      }
    }
    // ensure the json data is a string
    if (
      data["next"] &&
      !(typeof data["next"] === "string" || data["next"] instanceof String)
    ) {
      throw new Error(
        "Expected the field `next` to be a primitive type in the JSON string but got " +
          data["next"],
      );
    }
    // ensure the json data is a string
    if (
      data["previous"] &&
      !(
        typeof data["previous"] === "string" ||
        data["previous"] instanceof String
      )
    ) {
      throw new Error(
        "Expected the field `previous` to be a primitive type in the JSON string but got " +
          data["previous"],
      );
    }
    if (data["results"]) {
      // data not null
      // ensure the json data is an array
      if (!Array.isArray(data["results"])) {
        throw new Error(
          "Expected the field `results` to be an array in the JSON data but got " +
            data["results"],
        );
      }
      // validate the optional field `results` (array)
      for (const item of data["results"]) {
        ConfigurationType.validateJSON(item);
      }
    }

    return true;
  }
}

PaginatedConfigurationTypeList.RequiredProperties = ["count", "results"];

/**
 * @member {Number} count
 */
PaginatedConfigurationTypeList.prototype["count"] = undefined;

/**
 * @member {String} next
 */
PaginatedConfigurationTypeList.prototype["next"] = undefined;

/**
 * @member {String} previous
 */
PaginatedConfigurationTypeList.prototype["previous"] = undefined;

/**
 * @member {Array.<module:model/ConfigurationType>} results
 */
PaginatedConfigurationTypeList.prototype["results"] = undefined;

export default PaginatedConfigurationTypeList;
