const express = require('express');
const app = express();

app.use(express.json());

// Rutas
app.post('/', (req, res) => {
  // Lógica para crear un pedido
  res.send('Pedido creado');
});

app.get('/:id', (req, res) => {
  // Lógica para obtener un pedido
  res.send(`Detalles del pedido ${req.params.id}`);
});

app.listen(3002, () => {
  console.log('Servicio de Pedidos corriendo en http://localhost:3002');
});