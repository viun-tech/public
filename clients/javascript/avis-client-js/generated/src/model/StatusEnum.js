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
 * Enum class StatusEnum.
 * @enum {}
 * @readonly
 */
export default class StatusEnum {
  /**
   * value: "PENDING"
   * @const
   */
  PENDING = "PENDING";

  /**
   * value: "FAILED"
   * @const
   */
  FAILED = "FAILED";

  /**
   * value: "SUCCESS"
   * @const
   */
  SUCCESS = "SUCCESS";

  /**
   * Returns a <code>StatusEnum</code> enum value from a Javascript object name.
   * @param {Object} data The plain JavaScript object containing the name of the enum value.
   * @return {module:model/StatusEnum} The enum <code>StatusEnum</code> value.
   */
  static constructFromObject(object) {
    return object;
  }
}
