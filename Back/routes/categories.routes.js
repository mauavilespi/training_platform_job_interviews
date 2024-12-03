const express = require('express');
const { listCategories, addCategory, deleteCategory } = require('../app/controller/categories.controller');

const router = express.Router();

router.get('/', listCategories);
router.post('/', addCategory);
router.delete('/:id', deleteCategory);

module.exports = router;