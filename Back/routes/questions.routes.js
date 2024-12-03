const express = require('express');
const { listQuestions, addQuestion, deleteQuestion, listQuestionsByCategory } = require('../app/controller/questions.controller');

const router = express.Router();

router.get('/', listQuestions);
router.post('/', addQuestion);
router.delete('/:id', deleteQuestion);
router.get('/category/:categoryId/:limit', listQuestionsByCategory);

module.exports = router;