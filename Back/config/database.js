require('dotenv').config(); // Importar dotenv para cargar las variables

const { Sequelize } = require('sequelize');

// Configuración de la conexión a la base de datos usando variables de entorno
const sequelize = new Sequelize(
  process.env.DB_NAME,       // Nombre de la base de datos
  process.env.DB_USER,       // Usuario de la base de datos
  process.env.DB_PASSWORD,   // Contraseña de la base de datos
  {
    host: process.env.DB_HOST, // Host de la base de datos
    port: process.env.DB_PORT, // Puerto de la base de datos
    dialect: 'postgres',       // Tipo de base de datos
  }
);

module.exports = sequelize;