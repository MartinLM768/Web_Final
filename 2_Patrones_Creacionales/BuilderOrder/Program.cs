using System;

namespace BuilderOrder
{
    public class Order
    {
        public string CustomerName { get; private set; }
        public string Address { get; private set; }
        public string Product { get; private set; }
        public int Quantity { get; private set; }
        public string PaymentMethod { get; private set; }
        public bool GiftWrap { get; private set; }

        public override string ToString()
        {
            return $"Orden para: {CustomerName}\n" +
                   $"Dirección: {Address}\n" +
                   $"Producto: {Product}\n" +
                   $"Cantidad: {Quantity}\n" +
                   $"Pago: {PaymentMethod}\n" +
                   $"Empaque de regalo: {(GiftWrap ? "Sí" : "No")}";
        }

        private Order() { }

        public class Builder
        {
            private Order order = new Order();

            public Builder SetCustomerName(string name)
            {
                order.CustomerName = name;
                return this;
            }

            public Builder SetAddress(string address)
            {
                order.Address = address;
                return this;
            }

            public Builder SetProduct(string product)
            {
                order.Product = product;
                return this;
            }

            public Builder SetQuantity(int quantity)
            {
                order.Quantity = quantity;
                return this;
            }

            public Builder SetPaymentMethod(string paymentMethod)
            {
                order.PaymentMethod = paymentMethod;
                return this;
            }

            public Builder SetGiftWrap(bool giftWrap)
            {
                order.GiftWrap = giftWrap;
                return this;
            }

            public Order Build()
            {
                return order;
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            var order = new Order.Builder()
                .SetCustomerName("Juan Pérez")
                .SetAddress("Calle 123 #45-67")
                .SetProduct("Laptop")
                .SetQuantity(1)
                .SetPaymentMethod("Tarjeta de crédito")
                .SetGiftWrap(true)
                .Build();

            Console.WriteLine(order);
        }
    }
}
