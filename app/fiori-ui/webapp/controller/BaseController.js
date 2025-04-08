// @ts-nocheck
sap.ui.define([
    "sap/ui/core/mvc/Controller",
    "sap/m/MessageToast"
  ], function (Controller, MessageToast) {
    "use strict";
  
    /**
     * Base controller for CAP Documentator UI5 views.
     * Provides utility methods for model handling, routing, i18n, and messaging.
     */
    return Controller.extend("sap.capdocumentator.fioriui.controller.BaseController", {
  
      /**
       * Get a model instance by name (or default).
       * @param {string} [sName] Model name (optional)
       * @returns {sap.ui.model.Model}
       */
      getModel: function (sName) {
        return this.getView().getModel(sName);
      },
  
      /**
       * Set a model instance to the view.
       * @param {sap.ui.model.Model} oModel Model instance
       * @param {string} [sName] Model name (optional)
       * @returns {sap.ui.core.mvc.View}
       */
      setModel: function (oModel, sName) {
        return this.getView().setModel(oModel, sName);
      },
  
      /**
       * Get the router instance for this controller.
       * Used for navigation.
       * @returns {sap.ui.core.routing.Router}
       */
      getRouter: function () {
        return sap.ui.core.UIComponent.getRouterFor(this);
      },
  
      /**
       * Get the i18n resource bundle from the i18n model.
       * @returns {sap.base.i18n.ResourceBundle}
       */
      getResourceBundle: function () {
        return this.getOwnerComponent().getModel("i18n").getResourceBundle();
      },
  
      /**
       * Shortcut for fetching a translated i18n string.
       * @param {string} sKey i18n key
       * @param {Array} [aArgs] Arguments for placeholders
       * @returns {string}
       */
      getText: function (sKey, aArgs) {
        return this.getResourceBundle().getText(sKey, aArgs);
      },
  
      /**
       * Central place to show a toast message.
       * @param {string} sMessage Text to show
       */
      showMessage: function (sMessage) {
        MessageToast.show(sMessage);
      },
  
      /**
       * Optional: Handle OData or backend errors in a consistent way.
       * Can be extended to show MessageBox or toast.
       * @param {object} oError Error response
       */
      handleServiceError: function (oError) {
        const sMsg = oError?.responseText || "An unexpected error occurred.";
        this.showMessage(sMsg);
        console.error("Service Error:", oError);
      }
  
    });
  });  