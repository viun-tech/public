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
 * The Inspection model module.
 * @module model/Inspection
 * @version 0.8.0
 */
class Inspection {
  /**
   * Constructs a new <code>Inspection</code>.
   * @alias module:model/Inspection
   * @param id {Number}
   * @param team {Number}
   * @param createdAt {Date}
   * @param updatedAt {Date}
   * @param openDatetime {Date}
   */
  constructor(id, team, createdAt, updatedAt, openDatetime) {
    Inspection.initialize(this, id, team, createdAt, updatedAt, openDatetime);
  }

  /**
   * Initializes the fields of this object.
   * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
   * Only for internal use.
   */
  static initialize(obj, id, team, createdAt, updatedAt, openDatetime) {
    obj["id"] = id;
    obj["team"] = team;
    obj["created_at"] = createdAt;
    obj["updated_at"] = updatedAt;
    obj["open_datetime"] = openDatetime;
  }

  /**
   * Constructs a <code>Inspection</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/Inspection} obj Optional instance to populate.
   * @return {module:model/Inspection} The populated <code>Inspection</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new Inspection();

      if (data.hasOwnProperty("id")) {
        obj["id"] = ApiClient.convertToType(data["id"], "Number");
      }
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
      if (data.hasOwnProperty("created_at")) {
        obj["created_at"] = ApiClient.convertToType(data["created_at"], "Date");
      }
      if (data.hasOwnProperty("updated_at")) {
        obj["updated_at"] = ApiClient.convertToType(data["updated_at"], "Date");
      }
      if (data.hasOwnProperty("open_datetime")) {
        obj["open_datetime"] = ApiClient.convertToType(
          data["open_datetime"],
          "Date",
        );
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
   * Validates the JSON data with respect to <code>Inspection</code>.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Inspection</code>.
   */
  static validateJSON(data) {
    // check to make sure all required properties are present in the JSON string
    for (const property of Inspection.RequiredProperties) {
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
    if (!Array.isArray(data["images"])) {
      throw new Error(
        "Expected the field `images` to be an array in the JSON data but got " +
          data["images"],
      );
    }

    return true;
  }
}

Inspection.RequiredProperties = [
  "id",
  "team",
  "created_at",
  "updated_at",
  "open_datetime",
];

/**
 * @member {Number} id
 */
Inspection.prototype["id"] = undefined;

/**
 * @member {Number} team
 */
Inspection.prototype["team"] = undefined;

/**
 * @member {Number} product
 */
Inspection.prototype["product"] = undefined;

/**
 * @member {Number} opened_by
 */
Inspection.prototype["opened_by"] = undefined;

/**
 * @member {Number} closed_by
 */
Inspection.prototype["closed_by"] = undefined;

/**
 * @member {Array.<Number>} images
 */
Inspection.prototype["images"] = undefined;

/**
 * @member {Date} created_at
 */
Inspection.prototype["created_at"] = undefined;

/**
 * @member {Date} updated_at
 */
Inspection.prototype["updated_at"] = undefined;

/**
 * @member {Date} open_datetime
 */
Inspection.prototype["open_datetime"] = undefined;

/**
 * @member {Date} close_datetime
 */
Inspection.prototype["close_datetime"] = undefined;

/**
 * @member {Number} configuration
 */
Inspection.prototype["configuration"] = undefined;

/**
 * @member {Number} metadata
 */
Inspection.prototype["metadata"] = undefined;

export default Inspection;