productos = [] # lista vacía para almacenar los productos

# funcion para leer el archivo y divirlo en lineas
with open("base.txt","r") as archivo:
    productos = archivo.read().splitlines() 

# funcion que permite escribir sobre el archivo de texto
def escribir():
    with open("base.txt","w") as base:
        for producto in productos:
            base.write(f"{producto}\n")

# condición que nos permite crear el menú con opciones
while True:
    print("")
    print(" MENÚ PRINCIPAL ".center(40, "*"))   # título
    print("1) Agregar producto")                # sumar producto
    print("2) Borrar producto")                 # eliminar producto
    print("3) Salir")                           # terminar el programa
    print("4) Mostrar productos")               # visualizar productos en el archivo de texto
    print("5) Buscar productos")                # buscar producto en específico
    usuario = input("Ingrese una opción: ").strip()      # acción que permite al usuario elegir
    print("*" * 40)

    match usuario:
        case "3":   # este caso permite salir del programa
            print("\n📦 Gracias por usar el gestor de productos. ¡Hasta luego!")
            break 

        case "1":   # pedimos al usuario que ingrese un producto nuevo
            new_product = input("Ingrese el nombre del producto: ").strip().lower()
            productos.append(new_product)
            print(f"✅ Producto {new_product} agregado.")
            escribir()

        case "2":   # el usuario puede borrar un producto
            bye_product = input("Ingrese el nombre del producto a borrar: ").strip().lower()
            if bye_product in productos:
                productos.remove(bye_product)
                print(f"🗑️ Producto {bye_product} borrado.")    # si está, se borra
                escribir()
            else:
                print(f"❌ El producto {bye_product} no se encontró en la lista.")  # se imprime si no se encuentra el producto

        case "4":   # devuelve la lista de productos de forma escalonada, uno en una nueva línea
            print("\n📋 Productos en stock:")
            for producto in productos:
                print(f"- {producto}")

        case "5":   # permite buscar un producto dentro del archivo de texto
            find_product = input("Ingrese el nombre del producto a buscar: ").strip().lower()
            if find_product in productos:
                print(f"🔎 Producto {find_product} en stock.")  # producto existente en el archivo de texto
            else:
                print(f"❌ Producto {find_product} no encontrado.") # el producto no esta en el archivo de texto

        case _:     # se imprime al elegir opciones que no estan en el menú
            print("⚠️ Opción no valida, por favor intenta nuevamente.") # 

# se imprime al salir del programa
print("Lista de productos:",productos)
print("")
print("*" * 40)