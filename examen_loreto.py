# EXAMEN 

productos = {
    'M001': ['Alimento Premium', 'comida', 'DogPlus', 10, True, False],
    'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False, False],
    'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
    'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
    'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
    'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False, False]
}

stock = {
    'M001': [32990, 12],
    'M002': [9990, 0],
    'M003': [5490, 25],
    'M004': [7990, 5],
    'M005': [11990, 7],
    'M006': [24990, 3]
}




def validar_codigo(codigo):
    codigo = codigo.strip().upper()
    if codigo == "":
        return False
    
    if codigo in productos:
        return False
    return True


def validar_texto(texto):
    if texto.strip() == "":
        return False
    return True


def validar_peso(peso):
    return peso > 0


def validar_importado(valor):
    valor = valor.strip().lower()
    return valor == "s" or valor == "n"


def validar_cachorro(valor):
    valor = valor.strip().lower()
    return valor == "s" or valor == "n"


def validar_precio(precio):
    return precio > 0


def validar_unidades(unidades):
    return unidades >= 0


def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe ingresar un número entero")




def buscar_codigo(codigo):
    # Corrección: Asegura consistencia buscando siempre en mayúsculas
    return codigo.upper() in productos


def unidades_categoria(productos, stock, categoria):
    total = 0
    for codigo in productos:
        if productos[codigo][1].lower() == categoria.lower():
            total += stock[codigo][1]
    print("El total de unidades disponibles es:", total)


def busqueda_precio(productos, stock, p_min, p_max):
    lista = []
    for codigo in stock:
        precio = stock[codigo][0]
        unidades = stock[codigo][1]

        if p_min <= precio <= p_max and unidades > 0:
            nombre = productos[codigo][0]
            lista.append(nombre + "--" + codigo)

    if len(lista) == 0:
        print("No hay productos en ese rango de precios.")
    else:
        lista.sort()
        print("Los productos encontrados son:")
        for elemento in lista:
            print(f"- {elemento}")


def actualizar_precio(productos, stock, codigo, nuevo_precio):
    codigo = codigo.upper()
    if buscar_codigo(codigo):
        stock[codigo][0] = nuevo_precio  # Corrección: Ahora 'codigo' sí está en mayúsculas garantizado
        return True
    return False


def agregar_producto(productos, stock, codigo, nombre,
                     categoria, marca, peso, importado,
                     cachorro, precio, unidades):
    codigo = codigo.upper()
    
    # Si pasa los filtros del menú, se añade directamente de forma segura
    productos[codigo] = [nombre, categoria, marca, peso, importado, cachorro]
    stock[codigo] = [precio, unidades]
    return True


def eliminar_producto(productos, stock, codigo):
    codigo = codigo.upper()
    if buscar_codigo(codigo):
        del productos[codigo]
        del stock[codigo]
        return True
    return False



opcion = 0

while opcion != 6:
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("====================================")

    opcion = leer_opcion()

   
    if opcion == 1:
        categoria = input("Ingrese categoría a consultar: ")
        unidades_categoria(productos, stock, categoria)

    
    elif opcion == 2:
        while True:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))

                if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                    break
                print("Debe ingresar un rango válido")
            except ValueError:
                print("Debe ingresar valores enteros")
        busqueda_precio(productos, stock, p_min, p_max)

  
    elif opcion == 3:
        seguir = "s"
        while seguir.lower() == "s":
            codigo = input("Ingrese código del producto: ").upper()

            while True:
                try:
                    nuevo_precio = int(input("Ingrese nuevo precio: "))
                    if nuevo_precio > 0:
                        break
                    print("El precio debe ser mayor que cero")
                except ValueError:
                    print("Debe ingresar un número entero")

            if actualizar_precio(productos, stock, codigo, nuevo_precio):
                print("Precio actualizado")
            else:
                print("El código no existe")

            seguir = input("¿Desea actualizar otro precio (s/n)?: ")

  
    elif opcion == 4:
        codigo = input("Ingrese código: ").upper()
        nombre = input("Ingrese nombre: ")
        categoria = input("Ingrese categoría: ")
        marca = input("Ingrese marca: ")

        try:
            peso = float(input("Ingrese peso (kg): "))
        except ValueError:
            peso = -1

        importado = input("¿Es importado? (s/n): ").lower()
        cachorro = input("¿Es para cachorro? (s/n): ").lower()

        try:
            precio = int(input("Ingrese precio: "))
        except ValueError:
            precio = -1

        try:
            unidades = int(input("Ingrese unidades: "))
        except ValueError:
            unidades = -1

        # Validaciones en orden estricto
        if not validar_codigo(codigo):
            print("Código inválido o ya existe")
        elif not validar_texto(nombre):
            print("Nombre inválido")
        elif not validar_texto(categoria):
            print("Categoría inválida")
        elif not validar_texto(marca):
            print("Marca inválida")
        elif not validar_peso(peso):
            print("Peso inválido")
        elif not validar_importado(importado):
            print("Debe ingresar s o n")
        elif not validar_cachorro(cachorro):
            print("Debe ingresar s o n")
        elif not validar_precio(precio):
            print("Precio inválido")
        elif not validar_unidades(unidades):
            print("Unidades inválidas")
        else:
            # Transformación a booleanos para mantener consistencia con los datos semilla
            importado_bool = (importado == "s")
            cachorro_bool = (cachorro == "s")

            if agregar_producto(productos, stock, codigo, nombre, categoria, 
                                marca, peso, importado_bool, cachorro_bool, precio, unidades):
                print("Producto agregado con éxito.")
            else:
                print("Error inesperado al agregar el producto.")

   
    elif opcion == 5:
        codigo = input("Ingrese código del producto: ").upper()
        if eliminar_producto(productos, stock, codigo):
            print("Producto eliminado")
        else:
            print("El código no existe")

print("Programa finalizado.")