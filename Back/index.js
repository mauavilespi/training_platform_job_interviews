const express = require('express');
const bodyParser = require('body-parser');
const questionsRoutes = require('./routes/questions.routes');
const categoriesRoutes = require('./routes/categories.routes');

const app = express();
const port = 3000;

app.use(bodyParser.json());

// Rutas
app.use('/questions', questionsRoutes);
app.use('/categories', categoriesRoutes);

// Servidor escuchando
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});