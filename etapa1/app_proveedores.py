proveedores = []

def agregar_proveedor(codigo, cod_producto, descripcion, razon_social):
    if consultar_proveedor(codigo):
        print("El proveedor ya existe")
        return False
    nuevo_proveedor = {
    'codigo': codigo,
    'cod_producto': cod_producto,    
    'descripcion': descripcion,
    'razon_social': razon_social
    
    }
    proveedores.append(nuevo_proveedor)
    return True

def consultar_proveedor(codigo):
    for proveedor in proveedores:
        if proveedor['codigo'] == codigo:
            return proveedor
    return False

def modificar_proveedor(codigo, nuevo_cod_producto, nueva_descripcion, nueva_razon_social):
    for proveedor in proveedores:
        if proveedor['codigo'] == codigo:
            proveedor['producto'] = nuevo_cod_producto
            proveedor['descripcion'] = nueva_descripcion
            proveedor['razon_social'] = nueva_razon_social
            
            return True
    return False
def  listar_proveedores():
    print("_"*50)
    for proveedor in proveedores:
        print(f"Código.............: {proveedor['codigo']}")
        print(f"Códido del producto: {proveedor['descripcion']}")
        print(f"Descripción:.......: {proveedor['descripcion']}")
        print(f"Razón Social.......: {proveedor['razon_social']}")
        print("_"*50)
        
def eliminar_proveedor(codigo):
    for proveedor in proveedores:
        if proveedor['codigo'] == codigo:
            proveedores.remove(proveedor)
            return True
    return False

#------Programa principal
print("\033[H\033[J")

#Agregamos proveedores
agregar_proveedor(1,3,'Parlante Portatil Go','Atlia S.A.')
agregar_proveedor(2,22,'Auricular inhalambrico', 'TecnoS.A.')
agregar_proveedor(3,2,'Teclado Gamer con retroiluminacion Led A24','MtaR S.A.')
agregar_proveedor(4,1,'Notebook A 16p Pro 8g ram','IDEAS S.A')

listar_proveedores()

print("Vamos a eliminar a un proveedor")
eliminar_proveedor(3)

listar_proveedores()

print("Vamos a consultar un proveedor")

print(consultar_proveedor(2))
print(consultar_proveedor(9))

print("Vamos a modificar un proveedor")
print(consultar_proveedor(2))
modificar_proveedor(2,3,'Auricular Inhalambrico M16 Pro Superior')
print("-------------")
print(consultar_proveedor(2))
