const { DataTypes } = require('sequelize');
const sequelize = require('../../config/database');
const Question = require('./question.model');
const Category = require('./category.model');

const BelongTo = sequelize.define('BelongTo', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
});

Question.belongsToMany(Category, { through: BelongTo });
Category.belongsToMany(Question, { through: BelongTo });

module.exports = BelongTo;