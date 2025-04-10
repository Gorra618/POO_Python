class Tools:
    def __init__(self, nombre, marca, precio, cantidad):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.cantidad = cantidad

    def show_data(self):
        print(f" Tool: {self.nombre} \n Brand: {self.marca} \n Price: {self.precio} \n Quantity: {self.cantidad}")
        print("-----------")

tool_1 = Tools("Martillo", "Pepe", 1200, 8)
tool_2 = Tools("Serrucho", "Tooletes", 5000, 12)
tool_3 = Tools("Linterna", "Lucecita", 500, 24)

print("-----------")
tool_1.show_data()
tool_2.show_data()
tool_3.show_data()
