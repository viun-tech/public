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
 * The ProductCategory model module.
 * @module model/ProductCategory
 * @version 0.8.0
 */
class ProductCategory {
  /**
   * Constructs a new <code>ProductCategory</code>.
   * @alias module:model/ProductCategory
   * @param id {Number}
   * @param team {Number}
   * @param createdAt {Date}
   * @param updatedAt {Date}
   */
  constructor(id, team, createdAt, updatedAt) {
    ProductCategory.initialize(this, id, team, createdAt, updatedAt);
  }

  /**
   * Initializes the fields of this object.
   * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
   * Only for internal use.
   */
  static initialize(obj, id, team, createdAt, updatedAt) {
    obj["id"] = id;
    obj["team"] = team;
    obj["created_at"] = createdAt;
    obj["updated_at"] = updatedAt;
  }

  /**
   * Constructs a <code>ProductCategory</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/ProductCategory} obj Optional instance to populate.
   * @return {module:model/ProductCategory} The populated <code>ProductCategory</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new ProductCategory();

      if (data.hasOwnProperty("id")) {
        obj["id"] = ApiClient.convertToType(data["id"], "Number");
      }
      if (data.hasOwnProperty("team")) {
        obj["team"] = ApiClient.convertToType(data["team"], "Number");
      }
      if (data.hasOwnProperty("instances")) {
        obj["instances"] = ApiClient.convertToType(data["instances"], [
          "Number",
        ]);
      }
      if (data.hasOwnProperty("created_at")) {
        obj["created_at"] = ApiClient.convertToType(data["created_at"], "Date");
      }
      if (data.hasOwnProperty("updated_at")) {
        obj["updated_at"] = ApiClient.convertToType(data["updated_at"], "Date");
      }
      if (data.hasOwnProperty("name")) {
        obj["name"] = ApiClient.convertToType(data["name"], "String");
      }
      if (data.hasOwnProperty("display_name")) {
        obj["display_name"] = ApiClient.convertToType(
          data["display_name"],
          "String",
        );
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
   * Validates the JSON data with respect to <code>ProductCategory</code>.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ProductCategory</code>.
   */
  static validateJSON(data) {
    // check to make sure all required properties are present in the JSON string
    for (const property of ProductCategory.RequiredProperties) {
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
    if (!Array.isArray(data["instances"])) {
      throw new Error(
        "Expected the field `instances` to be an array in the JSON data but got " +
          data["instances"],
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
      data["display_name"] &&
      !(
        typeof data["display_name"] === "string" ||
        data["display_name"] instanceof String
      )
    ) {
      throw new Error(
        "Expected the field `display_name` to be a primitive type in the JSON string but got " +
          data["display_name"],
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

ProductCategory.RequiredProperties = ["id", "team", "created_at", "updated_at"];

/**
 * @member {Number} id
 */
ProductCategory.prototype["id"] = undefined;

/**
 * @member {Number} team
 */
ProductCategory.prototype["team"] = undefined;

/**
 * @member {Array.<Number>} instances
 */
ProductCategory.prototype["instances"] = undefined;

/**
 * @member {Date} created_at
 */
ProductCategory.prototype["created_at"] = undefined;

/**
 * @member {Date} updated_at
 */
ProductCategory.prototype["updated_at"] = undefined;

/**
 * @member {String} name
 */
ProductCategory.prototype["name"] = undefined;

/**
 * @member {String} display_name
 */
ProductCategory.prototype["display_name"] = undefined;

/**
 * @member {String} description
 */
ProductCategory.prototype["description"] = undefined;

export default ProductCategory;
