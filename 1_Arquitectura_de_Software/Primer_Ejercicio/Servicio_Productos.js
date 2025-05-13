const express = require('express');
const app = express();

app.use(express.json());

// Rutas
app.get('/', (req, res) => {
  // Lógica para listar productos
  res.send('Lista de productos');
});

app.post('/', (req, res) => {
  // Lógica para crear un producto
  res.send('Producto creado');
});

app.listen(3004, () => {
  console.log('Servicio de Productos corriendo en http://localhost:3004');
});