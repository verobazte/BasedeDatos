class Listado_proveedores:
    proveedores = []

    def agregar_proveedor(self, codigo, cod_producto, descripcion, razon_social):
        if self.consultar_proveedor(codigo):
            return False
        

        nuevo_proveedor = {
            'codigo' : codigo,
            'cod_producto' : cod_producto,
            'descripcion' : descripcion,
            ' razon_social' : razon_social
        }

        self.proveedores.append(nuevo_proveedor)
        return True

    def consultar_proveedor(self, codigo):
        for proveedor in self.proveedores:
            if proveedor['codigo'] == codigo:
                return proveedor
        return False
    
    def modificar_proveedor(self, codigo, nuevo_cod_producto,nueva_descripcion, nueva_razon_social):
        for proveedor in self.proveedores:
            if proveedor['codigo'] == codigo:
                proveedor['cod_producto'] = nuevo_cod_producto
                proveedor['descripcion'] = nueva_descripcion
                proveedor['razon_social'] = nueva_razon_social
                return True
            
    def listar_proveedores(self):
        print("*"*50)
        for proveedor in self.proveedores:
            print(f"Código.............:{proveedor['codigo']}")
            print(f"Código del producto.{proveedor['cod_producto']}")
            print(f"Descripción........:{proveedor['descripcion']}")
            print(f"Razón Social.......:{proveedor['razon_social']}")
            print("*"*50)

    def eliminar_proveedor(self,codigo):
        for proveedor in self.proveedores:
            if proveedor['codigo'] == codigo:
                self.proveedores.remove(proveedor)
                return True
        return False
    
    def mostrar_proveedor(self,codigo):
        proveedor = self.consultar_proveedor(codigo)
        if proveedor:
            print("-"*50) 
            print(f"Código..............:{proveedor['codigo']}")
            print(f"Código del producto.:{proveedor['cod_producto']}")
            print(f"Descripción.........:{proveedor['descripcion']}")
            print(f"Razón Social..... ..:{proveedor['razon_social']}")
            print("-"*50)    


        else:
            print(f"El proveedor {codigo} no existe")   
#------------------------------------
#Programa principal
#------------------------------------
print("\033[H\033[J")

listado_proveedores =  Listado_proveedores()
#Agregamos y consultamos productos


listado_proveedores.agregar_proveedor(1,22,'Auricular inhalambrico', 'TecnoS.A.') 
listado_proveedores.agregar_proveedor(1,3,'Parlante Portatil Go','Atlia S.A.')
listado_proveedores.agregar_proveedor(3,2,'Teclado Gamer con retroiluminacion Led A24','MtaR S.A.')  
listado_proveedores.agregar_proveedor(4,1,'Notebook A 16p Pro 8g ram','IDEAS S.A')


print("-----------------------")
print(listado_proveedores.consultar_proveedor(3))
print("-----------------------")
print(listado_proveedores.consultar_proveedor(15))    

listado_proveedores.listar_proveedores()      
print("-----------------------")
print('Eliminamos a un proveedor')
listado_proveedores.eliminar_proveedor(4)
listado_proveedores.listar_proveedores()

print("-----------------------")
print("-----------------------")
print("-----------------------")
listado_proveedores.mostrar_proveedor(3)
listado_proveedores.mostrar_proveedor(25)
