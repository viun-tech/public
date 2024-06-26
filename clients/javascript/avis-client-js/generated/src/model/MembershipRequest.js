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
 * The MembershipRequest model module.
 * @module model/MembershipRequest
 * @version 0.8.0
 */
class MembershipRequest {
  /**
   * Constructs a new <code>MembershipRequest</code>.
   * @alias module:model/MembershipRequest
   * @param role {String}
   */
  constructor(role) {
    MembershipRequest.initialize(this, role);
  }

  /**
   * Initializes the fields of this object.
   * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
   * Only for internal use.
   */
  static initialize(obj, role) {
    obj["role"] = role;
  }

  /**
   * Constructs a <code>MembershipRequest</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/MembershipRequest} obj Optional instance to populate.
   * @return {module:model/MembershipRequest} The populated <code>MembershipRequest</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new MembershipRequest();

      if (data.hasOwnProperty("role")) {
        obj["role"] = ApiClient.convertToType(data["role"], "String");
      }
    }
    return obj;
  }

  /**
   * Validates the JSON data with respect to <code>MembershipRequest</code>.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @return {boolean} to indicate whether the JSON data is valid with respect to <code>MembershipRequest</code>.
   */
  static validateJSON(data) {
    // check to make sure all required properties are present in the JSON string
    for (const property of MembershipRequest.RequiredProperties) {
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
      data["role"] &&
      !(typeof data["role"] === "string" || data["role"] instanceof String)
    ) {
      throw new Error(
        "Expected the field `role` to be a primitive type in the JSON string but got " +
          data["role"],
      );
    }

    return true;
  }
}

MembershipRequest.RequiredProperties = ["role"];

/**
 * @member {String} role
 */
MembershipRequest.prototype["role"] = undefined;

export default MembershipRequest;
