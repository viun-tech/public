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
    instance = new Avis.ImageApi();
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

  describe("ImageApi", function () {
    describe("imageCreate", function () {
      it("should call imageCreate successfully", function (done) {
        //uncomment below and update the code to test imageCreate
        //instance.imageCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe("imageDestroy", function () {
      it("should call imageDestroy successfully", function (done) {
        //uncomment below and update the code to test imageDestroy
        //instance.imageDestroy(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe("imageList", function () {
      it("should call imageList successfully", function (done) {
        //uncomment below and update the code to test imageList
        //instance.imageList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe("imagePartialUpdate", function () {
      it("should call imagePartialUpdate successfully", function (done) {
        //uncomment below and update the code to test imagePartialUpdate
        //instance.imagePartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe("imageQualityList", function () {
      it("should call imageQualityList successfully", function (done) {
        //uncomment below and update the code to test imageQualityList
        //instance.imageQualityList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe("imageRetrieve", function () {
      it("should call imageRetrieve successfully", function (done) {
        //uncomment below and update the code to test imageRetrieve
        //instance.imageRetrieve(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe("imageUpdate", function () {
      it("should call imageUpdate successfully", function (done) {
        //uncomment below and update the code to test imageUpdate
        //instance.imageUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });
});
