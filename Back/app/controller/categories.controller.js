const { Category } = require('../model');

const listCategories = async (req, res) => {
  try {
    const categories = await Category.findAll({ where: { active: true } });
    res.json(categories);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

const addCategory = async (req, res) => {
  try {
    const { category } = req.body;
    const newCategory = await Category.create({ category });
    res.json(newCategory);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

const deleteCategory = async (req, res) => {
  try {
    const { id } = req.params;
    await Category.update({ active: false }, { where: { id } });
    res.send("Category deleted (logical)");
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

module.exports = { listCategories, addCategory, deleteCategory };