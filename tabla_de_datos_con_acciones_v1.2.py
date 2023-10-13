
# Antes de usarlo debes installar "Prettytable" package desde consola
# Comando a continuación:

# pip install prettytable

from prettytable import PrettyTable

Productos = {1:'Pantalones', 2:'Camisas', 3:'Corbatas', 4:'Casacas'}
Precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
Stock = {1:50, 2:45, 3:30, 4:15}

def mostrar_diccionarios():
    table = PrettyTable()
    table.field_names = ["ID", "Producto", "Precio", "Stock"]
    for uid in Productos:
        table.add_row([uid, Productos[uid], Precios[uid], Stock[uid]])
    print(table)

def agregar_producto():
    while True:
        nuevo_producto = input("Volver al menú principal [back]\nNombre del nuevo producto:\n ")
        if nuevo_producto.lower() == 'back':
            return
        
        # Validar que el nombre del producto no esté vacío
        if nuevo_producto.strip(): 
            # Nombre del nuevo producto: 30 caracteres o menos
            if len(nuevo_producto) <= 30:
                break
            else:
                print("\nEl nombre del producto debe tener 30 caracteres o menos. Introduce un valor válido.\n")
        else: 
            print("\nEl nombre del producto no puede estar vacío. Introduce un valor válido.\n")
    
    while True:
        nuevo_precio = input("Volver al menú principal [back] \nPrecio del nuevo producto: \n ")
        if nuevo_precio.lower() == 'back':
            return
        try:
            nuevo_precio = float(nuevo_precio)
            if nuevo_precio < 0:
                print("\nEl precio no puede ser negativo. Introduce un valor válido.\n")
            else:
                break
        except ValueError:
            print("\nPrecio incorrecto. Ingresa un valor numérico válido.\n")

    while True:
        nuevo_stock = input("Volver al menú principal [back] \nCantidad en stock del nuevo producto: \n ")
        if nuevo_stock.lower() == 'back':
            return
        try:
            nuevo_stock = int(nuevo_stock)
            if nuevo_stock < 0:
                print("\nEl stock no puede ser negativo. Introduce un valor válido.\n")
            else:
                break
        except ValueError:
            print("\nStock incorrecto. Ingresa un valor numérico válido.\n")

    # Una ves los campos fueron correctamente ingresados se crea el nuevo ID y se añaden los nuevos valores a los campos respectivos
    nuevo_id = len(Productos) + 1
    Productos[nuevo_id] = nuevo_producto
    Precios[nuevo_id] = nuevo_precio
    Stock[nuevo_id] = nuevo_stock
    print(f"Producto '{nuevo_producto}' agregado con éxito.")

def eliminar_producto():
    while True:
        producto_id = input("Volver al menú principal [back] \nID del producto a eliminar: \n ")
        if producto_id.lower() == 'back':
            return
        
        if producto_id.isdigit():
            producto_id = int(producto_id)
            if producto_id in Productos:
                del Productos[producto_id]
                del Precios[producto_id]
                del Stock[producto_id]
                print("\nProducto eliminado con éxito.")
                break
            else:
                print("\nEl ID ingresado no existe en la base de datos. No se ha eliminado ningún producto.\n")
        else:
            print("\nPor favor, ingrese un ID de producto válido (número entero).\n")


def actualizar_producto():
    while True:
        producto_id = input("Volver al menú principal [back] \nID del producto a actualizar: \n ")
        if producto_id.lower() == 'back':
            return
        
        if producto_id.isdigit():
            producto_id = int(producto_id)
            if producto_id in Productos: 

                while True:
                    nuevo_producto = input("Volver al menú principal [back] \nNuevo nombre del producto: \n ")
                    if nuevo_producto.lower() == 'back':
                        return
                    
                    # Validar que el nombre del producto no esté vacío
                    if nuevo_producto.strip():  
                        # Nombre del nuevo producto: 30 caracteres o menos
                        if len(nuevo_producto) <= 30:
                            break
                        else:
                            print("\nEl nombre del producto debe tener 30 caracteres o menos. Introduce un valor válido.\n")
                    else: 
                        print("\nEl nombre del producto no puede estar vacío. Introduce un valor válido.\n")

                while True:
                    nuevo_precio = input("Precio del nuevo producto: \nVolver al menú principal [back] \n ")
                    if nuevo_precio.lower() == 'back':
                        return
                    try:
                        nuevo_precio = float(nuevo_precio)
                        if nuevo_precio < 0:
                            print("\nEl precio no puede ser negativo. Introduce un valor válido.\n")
                        else:
                            break
                    except ValueError:
                        print("\nPrecio incorrecto. Ingresa un valor numérico válido.\n")

                while True:
                    nuevo_stock = input("Volver al menú principal [back] \nCantidad en stock del nuevo producto: \n ")
                    if nuevo_stock.lower() == 'back':
                        return
                    try:
                        nuevo_stock = int(nuevo_stock)
                        if nuevo_stock < 0:
                            print("\nEl stock no puede ser negativo. Introduce un valor válido.\n")
                        else:
                            break
                    except ValueError:
                        print("\nStock incorrecto. Ingresa un valor numérico válido.\n")
            
                # Una ves los campos fueron correctamente ingresados, Entonces actualizamos
                Productos[producto_id] = nuevo_producto
                Precios[producto_id] = nuevo_precio
                Stock[producto_id] = nuevo_stock
                print("Producto actualizado con éxito.")
                break
            else:
                print("\nEl ID ingresado no existe en la base de datos. No se ha actualizado ningún producto.\n")
        else:
            print("\nPor favor, ingrese un ID de producto válido (número entero).\n")

while True:
    mostrar_diccionarios()
    print("[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir")
    opcion = input("Elija opción: ")
    if opcion == '1':
        agregar_producto()
    elif opcion == '2':
        eliminar_producto()
    elif opcion == '3':
        actualizar_producto()
    elif opcion == '4':
        break
    else:
        print("\nOpción no válida. Por favor, elija una opción válida.\n")
