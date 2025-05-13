const express = require('express');
const app = express();

app.use(express.json());

// Rutas
app.post('/registro', (req, res) => {
  // Lógica para registrar un repartidor
  res.send('Repartidor registrado');
});

app.put('/:id/estado', (req, res) => {
  // Lógica para actualizar el estado del repartidor
  res.send(`Estado del repartidor ${req.params.id} actualizado`);
});

app.listen(3003, () => {
  console.log('Servicio de Repartidores corriendo en http://localhost:3003');
});