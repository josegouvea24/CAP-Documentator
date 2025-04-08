const cds = require("@sap/cds");
const { fetchReadme } = require("./utils/flask");

module.exports = cds.service.impl(async function () {

  /**
  * Retrieve README content for a given GitHub URL
  * @param {string} repoUrl The GitHub repository URL
  * @returns {Promise<string>} The README contents as a string
  */
  this.on("fetchReadMeFromGitHub", async (req) => {
    const repoUrl = req.data.repoUrl;
    console.log("📡 CAP Action triggered: fetchReadMeFromGitHub with url ", repoUrl);

    if (!repoUrl || !repoUrl.startsWith("http")) {
      return req.error(400, "❌ Invalid GitHub URL");
    }

    try {
      const readme = await fetchReadme(repoUrl);
      console.log("📄 README content fetched successfully: ", readme);
      return readme || "README not found.";
    } catch (err) {
      return req.error(500, err.message);
    }
  });
});
