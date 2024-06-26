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
    instance = new Avis.InspectionApi();
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

  describe("InspectionApi", function () {
    describe("inspectionCreate", function () {
      it("should call inspectionCreate successfully", function (done) {
        //uncomment below and update the code to test inspectionCreate
        //instance.inspectionCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe("inspectionDestroy", function () {
      it("should call inspectionDestroy successfully", function (done) {
        //uncomment below and update the code to test inspectionDestroy
        //instance.inspectionDestroy(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe("inspectionList", function () {
      it("should call inspectionList successfully", function (done) {
        //uncomment below and update the code to test inspectionList
        //instance.inspectionList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe("inspectionPartialUpdate", function () {
      it("should call inspectionPartialUpdate successfully", function (done) {
        //uncomment below and update the code to test inspectionPartialUpdate
        //instance.inspectionPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe("inspectionRetrieve", function () {
      it("should call inspectionRetrieve successfully", function (done) {
        //uncomment below and update the code to test inspectionRetrieve
        //instance.inspectionRetrieve(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe("inspectionSendValidationEmailRetrieve", function () {
      it("should call inspectionSendValidationEmailRetrieve successfully", function (done) {
        //uncomment below and update the code to test inspectionSendValidationEmailRetrieve
        //instance.inspectionSendValidationEmailRetrieve(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe("inspectionUpdate", function () {
      it("should call inspectionUpdate successfully", function (done) {
        //uncomment below and update the code to test inspectionUpdate
        //instance.inspectionUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe("inspectionValidationStatusList", function () {
      it("should call inspectionValidationStatusList successfully", function (done) {
        //uncomment below and update the code to test inspectionValidationStatusList
        //instance.inspectionValidationStatusList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });
});
