const axios = require("axios");
require("dotenv").config();

/**
 * Call Flask backend to fetch the README content for a given GitHub URL
 * @param {string} repoUrl The GitHub repository URL
 * @returns {Promise<string>} The README contents as a string
 */
async function fetchReadme(repoUrl) {
  const flaskBase = process.env.FLASK_BASE_URL;

  if (!flaskBase) {
    console.error("❌ Missing FLASK_BASE_URL in environment.");
    throw new Error("Flask backend URL is not configured.");
  }

  const endpoint = `${flaskBase}/readme`;

  console.log("📡 Calling Flask backend at:", endpoint);

  try {
    const response = await axios.post(endpoint, { url: repoUrl });
    return response.data.readme;
  } catch (err) {
    console.error("❌ Error calling Flask backend:", err.message);
    throw new Error("Failed to fetch README from backend.");
  }
}

module.exports = {
  fetchReadme
};