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

(function (root, factory) {
  if (typeof define === "function" && define.amd) {
    // AMD.
    define(["expect.js", process.cwd() + "/src/index"], factory);
  } else if (typeof module === "object" && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require("expect.js"), require(process.cwd() + "/src/index"));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.Avis);
  }
})(this, function (expect, Avis) {
  "use strict";

  var instance;

  beforeEach(function () {
    instance = new Avis.Metadata();
  });

  var getProperty = function (object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === "function") return object[getter]();
    else return object[property];
  };

  var setProperty = function (object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === "function") object[setter](value);
    else object[property] = value;
  };

  describe("Metadata", function () {
    it("should create an instance of Metadata", function () {
      // uncomment below and update the code to test Metadata
      //var instance = new Avis.Metadata();
      //expect(instance).to.be.a(Avis.Metadata);
    });

    it('should have the property id (base name: "id")', function () {
      // uncomment below and update the code to test the property id
      //var instance = new Avis.Metadata();
      //expect(instance).to.be();
    });

    it('should have the property team (base name: "team")', function () {
      // uncomment below and update the code to test the property team
      //var instance = new Avis.Metadata();
      //expect(instance).to.be();
    });

    it('should have the property configurations (base name: "configurations")', function () {
      // uncomment below and update the code to test the property configurations
      //var instance = new Avis.Metadata();
      //expect(instance).to.be();
    });

    it('should have the property schema (base name: "schema")', function () {
      // uncomment below and update the code to test the property schema
      //var instance = new Avis.Metadata();
      //expect(instance).to.be();
    });

    it('should have the property data (base name: "data")', function () {
      // uncomment below and update the code to test the property data
      //var instance = new Avis.Metadata();
      //expect(instance).to.be();
    });

    it('should have the property createdAt (base name: "created_at")', function () {
      // uncomment below and update the code to test the property createdAt
      //var instance = new Avis.Metadata();
      //expect(instance).to.be();
    });

    it('should have the property updatedAt (base name: "updated_at")', function () {
      // uncomment below and update the code to test the property updatedAt
      //var instance = new Avis.Metadata();
      //expect(instance).to.be();
    });
  });
});
