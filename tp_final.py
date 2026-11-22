stock = [
    {
        "id": 1,
        "nombre": "Laptop",
        "categoria": "Electrónica",
        "descripcion": "Laptop de 15.6 pulgadas con 16GB de RAM y tarjeta gráfica dedicada.",
        "precio": 1200.50,
        "cantidad": 5
    },
    {
        "id": 2,
        "nombre": "Mouse",
        "categoria": "Accesorios",
        "descripcion": "Mouse óptico ergonómico con conexión Bluetooth y receptor USB.",
        "precio": 25.99,
        "cantidad": 30
    },
    {
        "id": 3,
        "nombre": "Teclado",
        "categoria": "Accesorios",
        "descripcion": "Teclado mecánico retroiluminado con switches blue.",
        "precio": 75.00,
        "cantidad": 12
    }
]

def ingreso(nombreDelCampo):
    campo = input(f"{nombreDelCampo}: ").strip().title()
    while campo == "":
        print(f"{nombreDelCampo} no puede estar vacio")
        campo = input(f"{nombreDelCampo}: ").strip().title()
    return campo

opcion = "0"

while opcion != "7":
    print("Bienvenido al sistema")
    print("""
    1. Agregar producto
    2. Mostrar productos
    3. Buscar producto
    4. Actualizar producto
    5. Eliminar producto
    6. Reporte de stock
    7. Salir
    """)
    opcion = input("Que queres hacer?: ")

    match opcion:
        case "1":
            print("Agregar")
            print("")

            id = ingreso("id") 

            nombre = ingreso("nombre") 
            
            categoria =ingreso("categoria") 

            descripcion = ingreso("descripcion") 

            cantidad = ingreso("cantidad") 
        
            precio = ingreso("precio") 

            producto = {}
            producto.update({"id":id})
            producto.update({"nombre":nombre})
            producto.update({"categoria":categoria})
            producto.update({"descripcion":descripcion})
            producto.update({"cantidad":cantidad})
            producto.update({"precio":precio})
            print(producto)
            stock.append(producto)


        case "2":
            print("Mostrar")
            print("")

            for item in stock:
                print(f"Producto: #{item['id']}")#print(f"Producto: #{item["id"]}")
                print(f"Nombre: {item["nombre"]}")
                print(f"Categoria: {item["categoria"]}")
                print(f"Precio: {item["precio"]}")
                print("")

        case "3":
            print("Buscar")
            print("")

            busqueda = input("Que producto queres buscar?: ")

            encontrado = False

            for item in stock:
                if busqueda == item["nombre"]:
                    print(f"Producto: #{item["id"]}")
                    print(f"Nombre: {item["nombre"]}")
                    print(f"Categoria: {item["categoria"]}")
                    print(f"Precio: {item["precio"]}")
                    print("")
                    encontrado = True

            if encontrado == False:
                print("Producto no encontrado")

        case "4":
            print("Actualizar")
            print("")

            actualizar = input("Que producto queres actualizar?: ")

            encontrado = False

            for item in stock:
                if actualizar == item["nombre"]:
                    print(f"Producto: #{item["id"]}")
                    print(f"Nombre: {item["nombre"]}")
                    print(f"Categoria: {item["categoria"]}")
                    print(f"Precio: {item["precio"]}")
                    print("")
                    encontrado = True

                    nuevoNombre = input("Cual es el nuevo nombre?: ") 

                    item.update({"nombre":nuevoNombre})

                    print("Producto actualizado")
                    print(f"Producto: #{item["id"]}")
                    print(f"Nombre: {item["nombre"]}")
                    print(f"Categoria: {item["categoria"]}")
                    print(f"Precio: {item["precio"]}")
                    print("")


            if encontrado == False:
                print("Producto no encontrado")

        case "5":
            print("Eliminar")
            print("")

            aEliminar = input("Que producto queres eliminar?: ")

            encontrado = False

            for item in stock:
                if aEliminar == item["nombre"]:
                    print(f"Producto: #{item["id"]}")
                    print(f"Nombre: {item["nombre"]}")
                    print(f"Categoria: {item["categoria"]}")
                    print(f"Precio: {item["precio"]}")
                    print("")
                    encontrado = True

                    stock.remove(item)

                    print(f"{aEliminar} eliminado")

            if encontrado == False:
                print("Producto no encontrado")

            
        case "6":
            print("Reporte de stock")
            print("")

            stockminimo = int(input("Que consideras stock bajo?: "))

            encontrado = False

            for item in stock:
                if stockminimo >= item["cantidad"]:
                    print("Producto con stock bajo")
                    print(f"Producto: #{item["id"]}")
                    print(f"Nombre: {item["nombre"]}")
                    print(f"Categoria: {item["categoria"]}")
                    print(f"Precio: {item["precio"]}")
                    print(f"Cantidad: {item["cantidad"]}")
                    print("")
                    encontrado = True

            if encontrado == False:
                print("No hay productos con stock minimo")

        case "7":
            print("Gracias por usar el sistema")
        case _:
            print("Opcion no valida, intenta de nuevo")