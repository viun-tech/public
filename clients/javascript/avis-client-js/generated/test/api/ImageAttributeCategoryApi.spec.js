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
    instance = new Avis.ImageAttributeCategoryApi();
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

  describe("ImageAttributeCategoryApi", function () {
    describe("imageAttributeCategoryCreate", function () {
      it("should call imageAttributeCategoryCreate successfully", function (done) {
        //uncomment below and update the code to test imageAttributeCategoryCreate
        //instance.imageAttributeCategoryCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe("imageAttributeCategoryDestroy", function () {
      it("should call imageAttributeCategoryDestroy successfully", function (done) {
        //uncomment below and update the code to test imageAttributeCategoryDestroy
        //instance.imageAttributeCategoryDestroy(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe("imageAttributeCategoryList", function () {
      it("should call imageAttributeCategoryList successfully", function (done) {
        //uncomment below and update the code to test imageAttributeCategoryList
        //instance.imageAttributeCategoryList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe("imageAttributeCategoryPartialUpdate", function () {
      it("should call imageAttributeCategoryPartialUpdate successfully", function (done) {
        //uncomment below and update the code to test imageAttributeCategoryPartialUpdate
        //instance.imageAttributeCategoryPartialUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe("imageAttributeCategoryRetrieve", function () {
      it("should call imageAttributeCategoryRetrieve successfully", function (done) {
        //uncomment below and update the code to test imageAttributeCategoryRetrieve
        //instance.imageAttributeCategoryRetrieve(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe("imageAttributeCategoryUpdate", function () {
      it("should call imageAttributeCategoryUpdate successfully", function (done) {
        //uncomment below and update the code to test imageAttributeCategoryUpdate
        //instance.imageAttributeCategoryUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });
});