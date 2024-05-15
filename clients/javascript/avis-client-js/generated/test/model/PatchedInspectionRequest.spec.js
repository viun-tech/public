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
    instance = new Avis.PatchedInspectionRequest();
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

  describe("PatchedInspectionRequest", function () {
    it("should create an instance of PatchedInspectionRequest", function () {
      // uncomment below and update the code to test PatchedInspectionRequest
      //var instance = new Avis.PatchedInspectionRequest();
      //expect(instance).to.be.a(Avis.PatchedInspectionRequest);
    });

    it('should have the property team (base name: "team")', function () {
      // uncomment below and update the code to test the property team
      //var instance = new Avis.PatchedInspectionRequest();
      //expect(instance).to.be();
    });

    it('should have the property product (base name: "product")', function () {
      // uncomment below and update the code to test the property product
      //var instance = new Avis.PatchedInspectionRequest();
      //expect(instance).to.be();
    });

    it('should have the property openedBy (base name: "opened_by")', function () {
      // uncomment below and update the code to test the property openedBy
      //var instance = new Avis.PatchedInspectionRequest();
      //expect(instance).to.be();
    });

    it('should have the property closedBy (base name: "closed_by")', function () {
      // uncomment below and update the code to test the property closedBy
      //var instance = new Avis.PatchedInspectionRequest();
      //expect(instance).to.be();
    });

    it('should have the property images (base name: "images")', function () {
      // uncomment below and update the code to test the property images
      //var instance = new Avis.PatchedInspectionRequest();
      //expect(instance).to.be();
    });

    it('should have the property closeDatetime (base name: "close_datetime")', function () {
      // uncomment below and update the code to test the property closeDatetime
      //var instance = new Avis.PatchedInspectionRequest();
      //expect(instance).to.be();
    });

    it('should have the property configuration (base name: "configuration")', function () {
      // uncomment below and update the code to test the property configuration
      //var instance = new Avis.PatchedInspectionRequest();
      //expect(instance).to.be();
    });

    it('should have the property metadata (base name: "metadata")', function () {
      // uncomment below and update the code to test the property metadata
      //var instance = new Avis.PatchedInspectionRequest();
      //expect(instance).to.be();
    });
  });
});