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
    instance = new Avis.PatchedResultRequest();
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

  describe("PatchedResultRequest", function () {
    it("should create an instance of PatchedResultRequest", function () {
      // uncomment below and update the code to test PatchedResultRequest
      //var instance = new Avis.PatchedResultRequest();
      //expect(instance).to.be.a(Avis.PatchedResultRequest);
    });

    it('should have the property team (base name: "team")', function () {
      // uncomment below and update the code to test the property team
      //var instance = new Avis.PatchedResultRequest();
      //expect(instance).to.be();
    });

    it('should have the property reportedBy (base name: "reported_by")', function () {
      // uncomment below and update the code to test the property reportedBy
      //var instance = new Avis.PatchedResultRequest();
      //expect(instance).to.be();
    });

    it('should have the property inferredBy (base name: "inferred_by")', function () {
      // uncomment below and update the code to test the property inferredBy
      //var instance = new Avis.PatchedResultRequest();
      //expect(instance).to.be();
    });

    it('should have the property image (base name: "image")', function () {
      // uncomment below and update the code to test the property image
      //var instance = new Avis.PatchedResultRequest();
      //expect(instance).to.be();
    });

    it('should have the property imageAttributes (base name: "image_attributes")', function () {
      // uncomment below and update the code to test the property imageAttributes
      //var instance = new Avis.PatchedResultRequest();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function () {
      // uncomment below and update the code to test the property status
      //var instance = new Avis.PatchedResultRequest();
      //expect(instance).to.be();
    });

    it('should have the property failureReason (base name: "failure_reason")', function () {
      // uncomment below and update the code to test the property failureReason
      //var instance = new Avis.PatchedResultRequest();
      //expect(instance).to.be();
    });

    it('should have the property comment (base name: "comment")', function () {
      // uncomment below and update the code to test the property comment
      //var instance = new Avis.PatchedResultRequest();
      //expect(instance).to.be();
    });
  });
});
