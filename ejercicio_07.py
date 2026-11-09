# Función para registrar productos
def registrar_productos():
    productos = []
    subtotal = 0

    cantidad = int(input("¿Cuántos productos desea registrar?: "))

    for i in range(cantidad):
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio: "))
        unidades = int(input("Ingrese la cantidad: "))

        if precio > 0 and unidades > 0:
            total = precio * unidades
            subtotal = subtotal + total

            productos.append([nombre, precio, unidades, total])

        else:
            print("Precio o cantidad inválidos.")
            return

    mostrar_venta(productos, subtotal)


def mostrar_venta(productos, subtotal):
    print("\n===== RESUMEN DE VENTA =====")

    for producto in productos:
        print("Producto:", producto[0])
        print("Precio:", producto[1])
        print("Cantidad:", producto[2])
        print("Total:", producto[3])

    if subtotal > 100:
        descuento = subtotal * 0.10
    else:
        descuento = 0

    total = subtotal - descuento

    print("--------------------------")
    print("Subtotal: $", subtotal)
    print("Descuento: $", descuento)
    print("Total a pagar: $", total)


registrar_productos()