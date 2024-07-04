productos = []

def agregar_producto(codigo, descripcion, cantidad, precio, imagen, 
proveedor):
    if consultar_producto(codigo):
        print("El producto ya existe")
        return False
    
    nuevo_producto = {
    'codigo': codigo,
    'descripcion': descripcion,
    'cantidad': cantidad,
    'precio': precio,
    'imagen': imagen,
    'proveedor': proveedor
    }
    productos.append(nuevo_producto)
    return True

def consultar_producto(codigo):
    for producto in productos:
        if producto['codigo'] == codigo:
            return producto
    return False

def modificar_producto(codigo, nueva_descripcion, nueva_cantidad, 
nuevo_precio, nueva_imagen, nuevo_proveedor):
    for producto in productos:
        if producto['codigo'] == codigo:
            producto['descripcion'] = nueva_descripcion
            producto['cantidad'] = nueva_cantidad
            producto['precio'] = nuevo_precio
            producto['imagen'] = nueva_imagen
            producto['proveedor'] = nuevo_proveedor
            return True
    return False

def  listar_productos():
    print("_"*50)
    for producto in productos:
        print(f"Código.....: {producto['codigo']}")
        print(f"Descripción: {producto['descripcion']}")
        print(f"Cantidad...: {producto['cantidad']}")
        print(f"Precio.....: {producto['precio']}")
        print(f"Imagen.....: {producto['imagen']}")
        print(f"Proveedor..: {producto['proveedor']}")
        print("_"*50)


def eliminar_producto(codigo):
    for producto in productos:
        if producto['codigo'] == codigo:
            productos.remove(producto)
            return True
    return False

#------Programa principal
print("\033[H\033[J")

#Agregamos productos
agregar_producto(1,'Parlante Portatil Go',10,24700, 'parlante.jpg',101)
agregar_producto(2,'Auricular Inhalambrico M10 Pro Superior',8,94500, 'auricular_in.jpg',102)
agregar_producto(3, 'Auricular Bluetooth de diadema M8',15, 44700,'auricular_blu.jpg',103)
agregar_producto(4, 'Teclado Gamer con retroiluminacion Led A24',10,67800,'teclado.jpg',104)
agregar_producto(5, 'Monitor Led 21,5 pulgadas marca H', 6,97500,'monitor.jpg',105)
agregar_producto(6,'Notebook A 16p Pro 8g ram',8,174300,'notebook.jpg',106)


listar_productos()

print("Vamos a eliminar un producto")
eliminar_producto(3)

listar_productos()

print("Vamos a consultar un producto")

print(consultar_producto(2))
print(consultar_producto(9))

print("Vamos a modificar un producto")
print(consultar_producto(2))
modificar_producto(2,'Auricular Inhalambrico M16 Pro Superior',9,97200,'auricular_in.jpg',102)
print("-------------")
print(consultar_producto(2))

#------Programa principal
print("\033[H\033[J")

#Agregamos productos
agregar_producto(1,'Parlante Portatil Go',10,24700, 'parlante.jpg',101)
agregar_producto(2,'Auricular Inhalambrico M10 Pro Superior',8,94500, 'auricular_in.jpg',102)
agregar_producto(3, 'Auricular Bluetooth de diadema M8',15, 44700,'auricular_blu.jpg',103)
agregar_producto(4, 'Teclado Gamer con retroiluminacion Led A24',10,67800,'teclado.jpg',104)
agregar_producto(5, 'Monitor Led 21,5 pulgadas marca H', 6,97500,'minitor.jpg',105)

listar_productos()

print("Vamos a eliminar un producto")
eliminar_producto(3)

listar_productos()

print("Vamos a consultar un producto")

print(consultar_producto(2))
print(consultar_producto(9))

print("Vamos a modificar un producto")
print(consultar_producto(2))
modificar_producto(2,'Auricular Inhalambrico M16 Pro Superior',9,97200,'auricular_in.jpg',102)
print("-------------")
print(consultar_producto(2))



#---CLIENTE

#PROVEEDOR