class Producto:
    def __init__(self, nombre, precio_unitario_con_igv, cantidad, igv=0.18):
        self.nombre = nombre
        self.precio_unitario_con_igv = precio_unitario_con_igv
        self.cantidad = cantidad
        self.igv = igv

    def precio_unitario_sin_igv(self):
        return self.precio_unitario_con_igv / (1 + self.igv)

    def subtotal_con_igv(self):
        return self.precio_unitario_con_igv * self.cantidad

    def subtotal_sin_igv(self):
        return self.precio_unitario_sin_igv() * self.cantidad

    def igv_por_producto(self):
        return self.subtotal_con_igv() - self.subtotal_sin_igv()

class Factura:
    def __init__(self, igv=0.18):
        self.productos = []
        self.igv = igv

    def agregar_producto(self, nombre, precio_unitario_con_igv, cantidad):
        self.productos.append(Producto(nombre, precio_unitario_con_igv, cantidad, self.igv))

    def mostrar_factura(self):
        print("----- FACTURA -----")
        print(f"{'Producto':20} {'Cant':>4} {'Unit c/IGV':>10} {'Unit s/IGV':>10} {'IGV':>8} {'SubTot':>10} {'Tot IGV':>10}")
        print("-" * 80)
        for p in self.productos:
            print(f"{p.nombre:20} {p.cantidad:4d} {p.precio_unitario_con_igv:10.2f} {p.precio_unitario_sin_igv():10.2f} "
                  f"{p.igv_por_producto() / p.cantidad:8.2f} {p.subtotal_sin_igv():10.2f} {p.subtotal_con_igv():10.2f}")
        print("-" * 80)
        total_sin_igv = sum(p.subtotal_sin_igv() for p in self.productos)
        total_igv = sum(p.igv_por_producto() for p in self.productos)
        total_con_igv = sum(p.subtotal_con_igv() for p in self.productos)
        print(f"{('SUBTOTAL (s/IGV): ' + f'{total_sin_igv:,.2f}').rjust(80)}")
        print(f"{('IGV TOTAL:       ' + f'{total_igv:,.2f}').rjust(80)}")
        print(f"{('TOTAL (c/IGV):   ' + f'{total_con_igv:,.2f}').rjust(80)}")

# Llenamos los datos manualmente
factura = Factura()
print("Ingresar productos. Para terminar, presione enter sin ingresar datos.")
while True:
    nombre = input("Producto: ")
    if nombre == "":
        break
    try:
        precio = float(input("Precio unitario con IGV: S/."))
        cantidad = int(input("Cantidad: "))
        factura.agregar_producto(nombre, precio, cantidad)
    except ValueError:
        print("Datos incorrectos, intenta de nuevo.")

factura.mostrar_factura()
