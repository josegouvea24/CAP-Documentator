const cds = require('@sap/cds');

module.exports = cds.server;

cds.on('served', async () => {
  console.log("📡 Starting custom service logic...");
  await require('./documentation-service');
});