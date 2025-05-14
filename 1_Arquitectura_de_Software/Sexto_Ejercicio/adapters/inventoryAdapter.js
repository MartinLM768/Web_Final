const InventoryPort = require('../ports/inventoryPort');

class InventoryAdapter extends InventoryPort {
    async checkInventory(items) {
        // Simula una verificación de inventario
        console.log('Verificando inventario...');
        return true; // Siempre disponible en este ejemplo
    }
}

module.exports = InventoryAdapter;