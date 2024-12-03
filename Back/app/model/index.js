const sequelize = require('../../config/database');
const Question = require('./question.model');
const Category = require('./category.model');
const BelongTo = require('./belong_to.model');

// Sincronizar modelos
(async () => {
  await sequelize.sync({ force: false }); // Cambia a `force: true` solo para desarrollo (esto elimina y recrea tablas)
  console.log('Database synced');
})();

module.exports = { sequelize, Question, Category, BelongTo };