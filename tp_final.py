from colorama import init
from colorama import Fore, Back, Style
init()
stock = [
    {
        "id": 1,
        "nombre": "Notebook",
        "categoria": "Electrónica",
        "descripcion": "Laptop de 15.6 pulgadas con 16GB de RAM y tarjeta gráfica dedicada.",
        "precio": 1200.50,
        "cantidad": 5
    },
    {
        "id": 2,
        "nombre": "Smartphone",
        "categoria": "Electrónica",
        "descripcion": "Teléfono inteligente con pantalla OLED de 6.5 pulgadas y 128GB de almacenamiento.",
        "precio": 799.99,
        "cantidad": 12
    },
    {
        "id": 3,
        "nombre": "Tablet",
        "categoria": "Electrónica",
        "descripcion": "Tablet de 10.9 pulgadas con 64GB de almacenamiento y soporte para lápiz digital.",
        "precio": 449.00,
        "cantidad": 8
    },
    {
        "id": 4,
        "nombre": "Monitor 27 pulgadas",
        "categoria": "Electrónica",
        "descripcion": "Monitor LED 4K UHD de 27 pulgadas con panel IPS y 60Hz.",
        "precio": 329.90,
        "cantidad": 10
    },
    {
        "id": 5,
        "nombre": "Teclado mecánico",
        "categoria": "Electrónica",
        "descripcion": "Teclado mecánico retroiluminado RGB con switches rojos y diseño compacto.",
        "precio": 89.99,
        "cantidad": 25
    },
    {
        "id": 6,
        "nombre": "Mouse inalámbrico",
        "categoria": "Electrónica",
        "descripcion": "Mouse ergonómico inalámbrico con sensor óptico de 4000 DPI y batería recargable.",
        "precio": 34.50,
        "cantidad": 40
    },
    {
        "id": 7,
        "nombre": "Auriculares Bluetooth",
        "categoria": "Electrónica",
        "descripcion": "Auriculares inalámbricos con cancelación activa de ruido y 30 horas de batería.",
        "precio": 199.00,
        "cantidad": 18
    },
    {
        "id": 8,
        "nombre": "Smartwatch",
        "categoria": "Electrónica",
        "descripcion": "Reloj inteligente con GPS, monitor de frecuencia cardíaca y resistencia al agua.",
        "precio": 259.99,
        "cantidad": 14
    },
    {
        "id": 9,
        "nombre": "Cámara digital",
        "categoria": "Electrónica",
        "descripcion": "Cámara mirrorless de 24MP con grabación de video 4K y lente intercambiable.",
        "precio": 949.00,
        "cantidad": 4
    },
    {
        "id": 10,
        "nombre": "Parlante Bluetooth",
        "categoria": "Electrónica",
        "descripcion": "Parlante portátil resistente al agua con 20 horas de reproducción continua.",
        "precio": 79.90,
        "cantidad": 30
    },
    {
        "id": 11,
        "nombre": "Disco duro externo 2TB",
        "categoria": "Electrónica",
        "descripcion": "Disco duro portátil USB 3.0 con 2TB de capacidad y carcasa antigolpes.",
        "precio": 84.99,
        "cantidad": 22
    },
    {
        "id": 12,
        "nombre": "SSD NVMe 1TB",
        "categoria": "Electrónica",
        "descripcion": "Unidad de estado sólido M.2 NVMe con velocidad de lectura de hasta 3500 MB/s.",
        "precio": 109.00,
        "cantidad": 20
    },
    {
        "id": 13,
        "nombre": "Memoria USB 128GB",
        "categoria": "Electrónica",
        "descripcion": "Pendrive USB 3.1 de 128GB con velocidad de transferencia rápida.",
        "precio": 17.99,
        "cantidad": 60
    },
    {
        "id": 14,
        "nombre": "Router WiFi 6",
        "categoria": "Electrónica",
        "descripcion": "Router de doble banda WiFi 6 con velocidad de hasta 3000 Mbps y 4 antenas.",
        "precio": 139.90,
        "cantidad": 15
    },
    {
        "id": 15,
        "nombre": "Webcam Full HD",
        "categoria": "Electrónica",
        "descripcion": "Cámara web 1080p con micrófono integrado y enfoque automático.",
        "precio": 59.99,
        "cantidad": 28
    },
    {
        "id": 16,
        "nombre": "Impresora multifunción",
        "categoria": "Electrónica",
        "descripcion": "Impresora de inyección de tinta con escáner, copiadora y conexión WiFi.",
        "precio": 189.00,
        "cantidad": 9
    },
    {
        "id": 17,
        "nombre": "Consola de videojuegos",
        "categoria": "Electrónica",
        "descripcion": "Consola de última generación con 1TB de almacenamiento y soporte para 4K.",
        "precio": 499.99,
        "cantidad": 7
    },
    {
        "id": 18,
        "nombre": "Control inalámbrico",
        "categoria": "Electrónica",
        "descripcion": "Mando inalámbrico con vibración háptica y batería recargable de larga duración.",
        "precio": 69.99,
        "cantidad": 35
    },
    {
        "id": 19,
        "nombre": "Televisor Smart TV 55 pulgadas",
        "categoria": "Electrónica",
        "descripcion": "Smart TV LED 4K de 55 pulgadas con HDR y acceso a aplicaciones de streaming.",
        "precio": 579.00,
        "cantidad": 6
    },
    {
        "id": 20,
        "nombre": "Barra de sonido",
        "categoria": "Electrónica",
        "descripcion": "Barra de sonido 2.1 con subwoofer inalámbrico y conectividad Bluetooth.",
        "precio": 149.50,
        "cantidad": 11
    }
]

#colocar en los msj de alertas!
#   Style.BRIGHT
#    + Fore.WHITE
#    + Back.BLUE
def ingreso(nombreDelCampo):
    campo = input(f"{nombreDelCampo}: ").strip().title()
    while campo == "":
        print(f"{nombreDelCampo} no puede estar vacio")
        campo = input(f"{nombreDelCampo}: ").strip().title()
    return campo

opcion = "0"

while opcion != "7":
    print(Back.GREEN + Fore.WHITE + "Bienvenido al sistema")
    print(Style.RESET_ALL)
    print("""
    1. Agregar producto
    2. Mostrar productos
    3. Buscar producto
    4. Actualizar producto
    5. Eliminar producto
    6. Reporte de stock
    7. Salir
    """)
    opcion = input(Fore.LIGHTBLUE_EX + "Que queres hacer?: ")
    print(Style.RESET_ALL)
    match opcion:
        case "1":
            print(Fore.CYAN + "Agregar")

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
            print(Fore.CYAN + "Mostrar")
            print(Style.RESET_ALL)

            for item in stock:
                #se usa comilla simples dentro del f-string para evitar conflicto con las comillas dobles
                #que delimitan la cadena
                print(f"Producto: #{item['id']}")#print(f"Producto: #{item["id"]}")
                print(f"Nombre: {item['nombre']}")
                print(f"Categoria: {item['categoria']}")
                print(f"Precio: {item['precio']}")
                print("")

        case "3":
            print(Fore.CYAN + "Buscar")
            print(Style.RESET_ALL)

            busqueda = input(Fore.GREEN + "Que producto queres buscar?: ")

            encontrado = False

            for item in stock:
                if busqueda == item["nombre"]:
                    print(f"Producto: #{item['id']}")
                    print(f"Nombre: {item['nombre']}")
                    print(f"Categoria: {item['categoria']}")
                    print(f"Precio: {item['precio']}")
                    print("")
                    encontrado = True

            if encontrado == False:
                print(Style.BRIGHT + Back.RED + Fore.WHITE + "Producto no encontrado" + Style.RESET_ALL)

        case "4":
            print(Fore.CYAN + "Actualizar")
            print(Style.RESET_ALL)

            actualizar = input(Fore.GREEN + "Que producto queres actualizar?: ")

            encontrado = False

            for item in stock:
                if actualizar == item["nombre"]:
                    print(f"Producto: #{item['id']}")
                    print(f"Nombre: {item['nombre']}")
                    print(f"Categoria: {item['categoria']}")
                    print(f"Precio: {item['precio']}")
                    print("")
                    encontrado = True

                    nuevoNombre = input(Fore.GREEN + "Cual es el nuevo nombre?: ") 

                    item.update({"nombre":nuevoNombre})

                    print("Producto actualizado")
                    print(f"Producto: #{item['id']}")
                    print(f"Nombre: {item['nombre']}")
                    print(f"Categoria: {item['categoria']}")
                    print(f"Precio: {item['precio']}")
                    print("")


            if encontrado == False:
                print(Style.BRIGHT + Back.RED + Fore.WHITE + "Producto no encontrado" + Style.RESET_ALL)

        case "5":
            print(Fore.CYAN + "Eliminar")
            print(Style.RESET_ALL)

            aEliminar = input(Fore.YELLOW + "Que producto queres eliminar?: ")

            encontrado = False

            for item in stock:
                if aEliminar == item["nombre"]:
                    print(f"Producto: #{item['id']}")
                    print(f"Nombre: {item['nombre']}")
                    print(f"Categoria: {item['categoria']}")
                    print(f"Precio: {item['precio']}")
                    print("")
                    encontrado = True

                    stock.remove(item)

                    print(f"{aEliminar} eliminado")

            if encontrado == False:
                print(Style.BRIGHT + Back.RED + Fore.WHITE + "Producto no encontrado" + Style.RESET_ALL)

            
        case "6":
            print(Fore.CYAN + "Reporte de stock")
            print(Style.RESET_ALL)

            stockminimo = int(input("Que consideras stock bajo?: "))

            encontrado = False

            for item in stock:
                if stockminimo >= item["cantidad"]:
                    print("Producto con stock bajo")
                    print(f"Producto: #{item['id']}")
                    print(f"Nombre: {item['nombre']}")
                    print(f"Categoria: {item['categoria']}")
                    print(f"Precio: {item['precio']}")
                    print(f"Cantidad: {item['cantidad']}")
                    print("")
                    encontrado = True

            if encontrado == False:
                print(Style.BRIGHT + Back.RED + Fore.WHITE + "No hay productos con stock minimo" + Style.RESET_ALL)

        case "7":
            print(Fore.CYAN + "Salir")
            print(Style.RESET_ALL)
        case _:
            print(Style.BRIGHT + Back.RED + Fore.WHITE + "Opcion no valida, intenta de nuevo" + Style.RESET_ALL)
            print("")
            print("")