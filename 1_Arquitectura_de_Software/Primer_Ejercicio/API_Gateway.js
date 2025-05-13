const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');

const app = express();

// Rutas hacia los microservicios
app.use('/usuarios', createProxyMiddleware({ target: 'http://localhost:3001', changeOrigin: true }));
app.use('/pedidos', createProxyMiddleware({ target: 'http://localhost:3002', changeOrigin: true }));
app.use('/repartidores', createProxyMiddleware({ target: 'http://localhost:3003', changeOrigin: true }));
app.use('/productos', createProxyMiddleware({ target: 'http://localhost:3004', changeOrigin: true }));

app.listen(3000, () => {
  console.log('API Gateway corriendo en http://localhost:3000');
});