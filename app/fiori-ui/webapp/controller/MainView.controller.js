sap.ui.define([
  "./BaseController",
  "sap/m/MessageBox"

], function (BaseController, MessageBox) {
  "use strict";

  return BaseController.extend("sap.capdocumentator.fioriui.controller.MainView", {

    onInit: function () {
      // Optional: Initialize models, check user roles, etc.
    },

    /**
     * Add a new repository to the DB.
     */
    onAddRepository: function () {
      const oInput = this.getView().byId("repoUrlInput");
      const sUrl = oInput.getValue();

      // Validate Repository URL
      if (!sUrl?.startsWith("http")) {
        this.showMessage("Please enter a valid GitHub URL.");
        return;
      }

      // Extract name from URL (e.g., https://github.com/user/repo → repo)
      const aParts = sUrl.split("/");
      const sName = aParts[aParts.length - 1] || "Unknown";

      // Add repository to DB via OData
      this.getModel().create("/Repositories", {
        name: sName,
        url: sUrl
      }, {
        success: () => {
          this.showMessage("Repository added.");
          oInput.setValue(""); // Clear input
        },
        error: this.handleServiceError.bind(this)
      });
    },

    onFetchReadme: function () {
      const sUrl = this.getView().byId("repoUrlInput").getValue();
      const oModel = this.getModel();
      const oAction = oModel.bindContext("/fetchReadMeFromGitHub(...)");

      console.log("Fetching README from URL:", sUrl);

      // Validate Repository URL
      if (!sUrl?.startsWith("http")) {
        this.showMessage("Please enter a valid GitHub URL.");
        return;
      }

      oAction.setParameter("repoUrl", sUrl);

      oAction.execute().then(() => {
        const oContext = oAction.getBoundContext();
        const sReadme = oContext?.getObject().value || "No content returned.";

        // Display README content in a MessageBox
        MessageBox.show(sReadme, {
          icon: sap.m.MessageBox.Icon.INFORMATION,
          title: "README Content",
          actions: [sap.m.MessageBox.Action.OK],
          onClose: function () {
            // Optional: Handle close action
          }
        });
      })
      .catch(this.handleServiceError.bind(this));
    },
  });
});
