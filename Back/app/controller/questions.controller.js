const { Question, BelongTo, Category } = require('../model');

const listQuestions = async (req, res) => {
  try {
    const questions = await Question.findAll({ where: { active: true } });
    res.json(questions);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

const addQuestion = async (req, res) => {
  try {
    const { question } = req.body;
    const newQuestion = await Question.create({ question });
    res.json(newQuestion);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

const deleteQuestion = async (req, res) => {
  try {
    const { id } = req.params;
    await Question.update({ active: false }, { where: { id } });
    res.send("Question deleted (logical)");
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

const listQuestionsByCategory = async (req, res) => {
  try {
    const { categoryId, limit } = req.params;
    const questions = await Question.findAll({
      include: {
        model: Category,
        where: { id: categoryId },
        through: { attributes: [] },
      },
      where: { active: true },
      limit: parseInt(limit, 10),
    });
    res.json(questions);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
};

module.exports = { listQuestions, addQuestion, deleteQuestion, listQuestionsByCategory };