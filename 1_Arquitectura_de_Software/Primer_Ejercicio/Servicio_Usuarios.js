const express = require('express');
const app = express();

app.use(express.json());

// Rutas
app.post('/registro', (req, res) => {
  // Lógica para registrar un usuario
  res.send('Usuario registrado');
});

app.post('/login', (req, res) => {
  // Lógica para autenticar un usuario
  res.send('Usuario autenticado');
});

app.listen(3001, () => {
  console.log('Servicio de Usuarios corriendo en http://localhost:3001');
});