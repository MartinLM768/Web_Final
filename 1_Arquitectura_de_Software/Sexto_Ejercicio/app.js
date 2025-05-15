const express = require('express');
const OrderService = require('./domain/orderService');
const StripeAdapter = require('./adapters/stripeAdapter');
const InventoryAdapter = require('./adapters/inventoryAdapter');

const app = express();
app.use(express.json());

// Configurar adaptadores
const paymentAdapter = new StripeAdapter();
const inventoryAdapter = new InventoryAdapter();

// Instanciar el servicio de pedidos
const orderService = new OrderService(paymentAdapter, inventoryAdapter);

// Endpoint para procesar pedidos
app.post('/orders', async (req, res) => {
    try {
        const result = await orderService.processOrder(req.body);
        res.status(200).json(result);
    } catch (error) {
        res.status(400).json({ success: false, message: error.message });
    }
});

// Iniciar el servidor
app.listen(3000, () => {
    console.log('Servidor corriendo en http://localhost:3000');
});