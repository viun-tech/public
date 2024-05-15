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
 * The UserAPIKeyCreate model module.
 * @module model/UserAPIKeyCreate
 * @version 0.8.0
 */
class UserAPIKeyCreate {
  /**
   * Constructs a new <code>UserAPIKeyCreate</code>.
   * @alias module:model/UserAPIKeyCreate
   * @param key {String}
   * @param created {Date}
   * @param expiryDate {Date} Once API key expires, clients cannot use it anymore.
   * @param revoked {Boolean}
   * @param message {String}
   */
  constructor(key, created, expiryDate, revoked, message) {
    UserAPIKeyCreate.initialize(
      this,
      key,
      created,
      expiryDate,
      revoked,
      message,
    );
  }

  /**
   * Initializes the fields of this object.
   * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
   * Only for internal use.
   */
  static initialize(obj, key, created, expiryDate, revoked, message) {
    obj["key"] = key;
    obj["created"] = created;
    obj["expiry_date"] = expiryDate;
    obj["revoked"] = revoked;
    obj["message"] = message;
  }

  /**
   * Constructs a <code>UserAPIKeyCreate</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/UserAPIKeyCreate} obj Optional instance to populate.
   * @return {module:model/UserAPIKeyCreate} The populated <code>UserAPIKeyCreate</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new UserAPIKeyCreate();

      if (data.hasOwnProperty("key")) {
        obj["key"] = ApiClient.convertToType(data["key"], "String");
      }
      if (data.hasOwnProperty("created")) {
        obj["created"] = ApiClient.convertToType(data["created"], "Date");
      }
      if (data.hasOwnProperty("name")) {
        obj["name"] = ApiClient.convertToType(data["name"], "String");
      }
      if (data.hasOwnProperty("expiry_date")) {
        obj["expiry_date"] = ApiClient.convertToType(
          data["expiry_date"],
          "Date",
        );
      }
      if (data.hasOwnProperty("revoked")) {
        obj["revoked"] = ApiClient.convertToType(data["revoked"], "Boolean");
      }
      if (data.hasOwnProperty("message")) {
        obj["message"] = ApiClient.convertToType(data["message"], "String");
      }
    }
    return obj;
  }

  /**
   * Validates the JSON data with respect to <code>UserAPIKeyCreate</code>.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UserAPIKeyCreate</code>.
   */
  static validateJSON(data) {
    // check to make sure all required properties are present in the JSON string
    for (const property of UserAPIKeyCreate.RequiredProperties) {
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
      data["key"] &&
      !(typeof data["key"] === "string" || data["key"] instanceof String)
    ) {
      throw new Error(
        "Expected the field `key` to be a primitive type in the JSON string but got " +
          data["key"],
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
      data["message"] &&
      !(
        typeof data["message"] === "string" || data["message"] instanceof String
      )
    ) {
      throw new Error(
        "Expected the field `message` to be a primitive type in the JSON string but got " +
          data["message"],
      );
    }

    return true;
  }
}

UserAPIKeyCreate.RequiredProperties = [
  "key",
  "created",
  "expiry_date",
  "revoked",
  "message",
];

/**
 * @member {String} key
 */
UserAPIKeyCreate.prototype["key"] = undefined;

/**
 * @member {Date} created
 */
UserAPIKeyCreate.prototype["created"] = undefined;

/**
 * A free-form name for the API key. Need not be unique. 50 characters max.
 * @member {String} name
 */
UserAPIKeyCreate.prototype["name"] = undefined;

/**
 * Once API key expires, clients cannot use it anymore.
 * @member {Date} expiry_date
 */
UserAPIKeyCreate.prototype["expiry_date"] = undefined;

/**
 * @member {Boolean} revoked
 */
UserAPIKeyCreate.prototype["revoked"] = undefined;

/**
 * @member {String} message
 */
UserAPIKeyCreate.prototype["message"] = undefined;

export default UserAPIKeyCreate;
