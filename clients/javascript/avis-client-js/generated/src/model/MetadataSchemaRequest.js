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
 * The MetadataSchemaRequest model module.
 * @module model/MetadataSchemaRequest
 * @version 0.8.0
 */
class MetadataSchemaRequest {
  /**
   * Constructs a new <code>MetadataSchemaRequest</code>.
   * @alias module:model/MetadataSchemaRequest
   * @param team {Number}
   * @param json {Object}
   */
  constructor(team, json) {
    MetadataSchemaRequest.initialize(this, team, json);
  }

  /**
   * Initializes the fields of this object.
   * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
   * Only for internal use.
   */
  static initialize(obj, team, json) {
    obj["team"] = team;
    obj["json"] = json;
  }

  /**
   * Constructs a <code>MetadataSchemaRequest</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/MetadataSchemaRequest} obj Optional instance to populate.
   * @return {module:model/MetadataSchemaRequest} The populated <code>MetadataSchemaRequest</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new MetadataSchemaRequest();

      if (data.hasOwnProperty("team")) {
        obj["team"] = ApiClient.convertToType(data["team"], "Number");
      }
      if (data.hasOwnProperty("json")) {
        obj["json"] = ApiClient.convertToType(data["json"], Object);
      }
    }
    return obj;
  }

  /**
   * Validates the JSON data with respect to <code>MetadataSchemaRequest</code>.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @return {boolean} to indicate whether the JSON data is valid with respect to <code>MetadataSchemaRequest</code>.
   */
  static validateJSON(data) {
    // check to make sure all required properties are present in the JSON string
    for (const property of MetadataSchemaRequest.RequiredProperties) {
      if (!data[property]) {
        throw new Error(
          "The required field `" +
            property +
            "` is not found in the JSON data: " +
            JSON.stringify(data),
        );
      }
    }

    return true;
  }
}

MetadataSchemaRequest.RequiredProperties = ["team", "json"];

/**
 * @member {Number} team
 */
MetadataSchemaRequest.prototype["team"] = undefined;

/**
 * @member {Object} json
 */
MetadataSchemaRequest.prototype["json"] = undefined;

export default MetadataSchemaRequest;
