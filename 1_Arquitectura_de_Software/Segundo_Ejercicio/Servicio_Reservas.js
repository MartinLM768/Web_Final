const express = require('express');
const app = express();
app.use(express.json());

// Mock database
const reservas = [];

// Crear una reserva
app.post('/reservas', (req, res) => {
    const reserva = { id: reservas.length + 1, ...req.body };
    reservas.push(reserva);
    res.status(201).send(reserva);
});

// Obtener todas las reservas
app.get('/reservas', (req, res) => {
    res.send(reservas);
});

// Iniciar el servicio
app.listen(3001, () => {
    console.log('Servicio de Reservas corriendo en el puerto 3001');
});