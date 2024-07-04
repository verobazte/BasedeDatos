class Catalogo:
    productos = []


    def agregar_producto(self,codigo, descripcion, cantidad, precio, imagen, 
proveedor):
        if self.consultar_producto(codigo):
            return False
        
        nuevo_producto = {
            'codigo': codigo,
            'descripcion': descripcion,
            'cantidad': cantidad,
            'precio': precio,
            'imagen': imagen,
            'proveedor': proveedor
        }
        
        self.productos.append(nuevo_producto)
        return True
    

    def consultar_producto(self, codigo):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                return producto
        return False
    
    def modificar_producto(self,codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, 
nuevo_proveedor):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                producto['descripcion'] = nueva_descripcion
                producto['cantidad'] = nueva_cantidad
                producto['precio'] = nuevo_precio
                producto['imagen'] = nueva_imagen
                producto['proveedor'] = nuevo_proveedor
                return True
        return False  


    def listar_productos(self):
        print("*"*50)
        for producto in self.productos:
            print(f"Código.....: {producto['codigo']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Cantidad...: {producto['cantidad']}")
            print(f"Precio.....: {producto['precio']}")
            print(f"Imagen.....: {producto['imagen']}")
            print(f"Proveedor..: {producto['proveedor']}")
            print("*"*50)

    def eliminar_producto(self,codigo):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                self.productos.remove(producto)
                return True
        return False
        
    def mostrar_producto(self,codigo):
        producto = self.consultar_producto(codigo)
        if producto:
            print("-"*50)
            print(f"Código.....: {producto['codigo']}")
            print(f"Descripción: {producto['descripcion']}")
            print(f"Cantidad...: {producto['cantidad']}")
            print(f"Precio.....: {producto['precio']}")
            print(f"Imagen.....: {producto['imagen']}")
            print(f"Proveedor..: {producto['proveedor']}")
            print("-"*50)

        else:
            print(f"El producto {codigo} no existe")



#------------------------------------
#Programa principal
#------------------------------------
print("\033[H\033[J")

catalogo = Catalogo()
#Agregamos y consultamos productos

catalogo.agregar_producto(1,'Parlante Portatil Go',10,24700, 'parlante.jpg',101)
catalogo.agregar_producto(2,'Auricular Inhalambrico M10 Pro Superior',8,94500, 'auricular_in.jpg',102)
catalogo.agregar_producto(3, 'Auricular Bluetooth de diadema M8',15, 44700,'auricular_blu.jpg',103)
catalogo.agregar_producto(4, 'Teclado Gamer con retroiluminacion Led A24',10,67800,'teclado.jpg',104)
catalogo.agregar_producto(5, 'Monitor Led 21,5 pulgadas marca H', 6,97500,'minitor.jpg',105)
catalogo.agregar_producto(6,'Notebook A 16p Pro 8g ram',8,174300,'notebook.jpg',106)

print("-----------------------")
print(catalogo.consultar_producto(3))
print("-----------------------")
print(catalogo.consultar_producto(15))

catalogo.listar_productos()      
print("-----------------------")
print("Eliminamos un producto")
catalogo.eliminar_producto(4)
catalogo.listar_productos()

print("-----------------------")
print("-----------------------")
print("-----------------------")
catalogo.mostrar_producto(3)
catalogo.mostrar_producto(25)