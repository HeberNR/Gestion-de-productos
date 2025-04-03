"""
    Crea un programa en Python que haga lo siguiente:

    ✅ Permita al usuario agregar productos a un diccionario, donde cada producto tenga:

    Nombre (clave del diccionario)

    Precio (float)

    Cantidad en stock (int)

    ✅ El programa debe ofrecer un menú con opciones:
    1 - Agregar producto
    2 - Listar productos
    3 - Actualizar stock
    4 - Eliminar producto
    5 - Salir
"""


productos = {}

def mostrar_menu():
    print("\n1. Agregar producto")
    print("2. Listar productos")
    print("3. Actualizar stock")
    print("4. Eliminar producto")
    print("5. Salir")

while True:

    mostrar_menu()
    
    try:
        seleccion = int(input("Elige una opción: "))
    except ValueError:
        print("Error: Ingresa un número válido.")
        continue

    if seleccion == 1:
        nombre = input("Ingrese el nombre del producto: ")

        if nombre in productos:
            print("El producto que desea ingresar ya está registrado. Usa la opción de actualizar stock.")
            continue
        try:
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Cantidad a ingresar: "))
        except ValueError:
            print("Debe ingresar números válidos.")
            continue
        
        productos[nombre] = {"precio": precio, "stock": cantidad}
        print(f"Producto '{nombre}' fue agregado con éxito.")

    elif seleccion == 2:
        if not productos:
            print("No hay productos registrados.")
        else:
            print("\nLista de productos:")
            for nombre, datos in productos.items():
                print(f"- {nombre}: ${datos['precio']} | Stock: {datos['stock']}")

    elif seleccion == 3:
        nombre = input("Ingrese el nombre del stock a actualizar: ")
        if nombre not in productos:
            print("No hay productos con ese nombre registrados.")
        else:
            opcion = input("¿Agregar o quitar cantidad?").strip().lower()
            if opcion == "agregar":
                try:
                    sumar = int(input("Ingrese la cantidad a agregar: "))
                    productos[nombre]["stock"] += sumar
                    print(f"Se agrego '{sumar}' unidades. Nuevo stock de {nombre}: {productos[nombre]['stock']}")
                except ValueError:
                    print("Debe ingresar un valor válido.")
            elif opcion == "quitar":
                try:
                    restar = int(input("Ingrese la cantidad a quitar: "))
                    if productos[nombre]['stock'] - restar < 0:
                        print("Error: no puedes tener stock en negativo.")
                    else: 
                        productos[nombre]['stock'] -= restar
                        print(f"Se quitaron {restar} cantidad. Nuevo stock de {nombre}: {productos[nombre]['stock']}")
                except ValueError:
                    print("Debe ingresar un valor válido.")
            else:
                print("Debes escribir agregar o quitar.")

    elif seleccion == 4:
        nombre = input("Ingrese el nombre del producto a eliminar: ").strip()

        if nombre not in productos:
            print(f"El producto '{nombre}' no se encuentra en existencia.")
        else:
            productos.pop(nombre)
        print(f"Se eliminó el producto '{nombre}' de la lista de productos.")

    elif seleccion == 5:
        print("👋 Saliendo del programa...")
        break

    else:
        print("Opción inválida. Ingresa un número del 1 al 5.")
