class OrderService {
    constructor(paymentPort, inventoryPort) {
        this.paymentPort = paymentPort; // Puerto de salida para pagos
        this.inventoryPort = inventoryPort; // Puerto de salida para inventarios
    }

    async processOrder(order) {
        // Validar inventario
        const isAvailable = await this.inventoryPort.checkInventory(order.items);
        if (!isAvailable) {
            throw new Error('Inventario insuficiente');
        }

        // Procesar pago
        const paymentResult = await this.paymentPort.processPayment(order.paymentDetails);
        if (!paymentResult.success) {
            throw new Error('El pago falló');
        }

        // Confirmar pedido
        return { success: true, message: 'Pedido procesado exitosamente' };
    }
}

module.exports = OrderService;