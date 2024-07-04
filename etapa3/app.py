import mysql.connector

class Catalogo:
    def __init__(self,host, user, password, database ):
        self.conn = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
            ) 
        
        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute(('''CREATE TABLE IF NOT EXISTS productos (
            codigo INT AUTO_INCREMENT PRIMARY KEY,
            descripcion VARCHAR(255) NOT NULL,
            cantidad INT NOT NULL,
            precio DECIMAL(10, 2) NOT NULL,
            imagen_url VARCHAR(255),
            proveedor INT(4))'''))
        self.conn.commit()

    def agregar_producto(self,descripcion, cantidad, precio, imagen_url,proveedor):
        sql = "INSERT INTO productos(descripcion, cantidad, precio, imagen_url, proveedor) VALUES (%s,%s,%s,%s,%s)"
        valores =(descripcion, cantidad, precio, imagen_url, proveedor)

        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.lastrowid
    
    def consultar_producto(self, codigo):
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {codigo}")
        return self.cursor.fetchone()
    
    def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen_url, nuevo_proveedor):
        sql = "UPDATE productos SET descripcion = %s, cantidad = %s, precio = %s, imagen_url = %s, proveedor = %s WHERE codigo = %s"
        valores = (nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen_url, nuevo_proveedor, codigo)

        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def mostrar_producto(self, codigo):
        producto = self.consultar_producto(codigo)
        if producto:
            print("-" * 40)
            print(f"Código.......:{producto['codigo']}")
            print(f"Descripción...{producto['descripcion']}")
            print(f"Cantidad.....:{producto['cantidad']}")
            print(f"Precio.......:{producto['precio']}")
            print(f"Imagen.......:{producto['imagen_url']}")
            print(f"Proveedor....:{producto['proveedor']}")
            print("-" * 40)

        else:
            print("Producto no encontrado")
            
    def listar_producto(self):
        self.cursor.execute('SELECT * FROM productos')
        productos = self.cursor.fetchall()
        return productos
    
    def eliminar_productos(self, codigo):
        self.cursor.execute(f'DELETE FROM productos WHERE codigo = {codigo}')
        self.conn.commit()
        return self.cursor.rowcount > 0


#-----------------------------------------------------
#Programa Principal

catalogo = Catalogo(host='localhost',user='root',password='',database='CodeCrafters')


#catalogo.agregar_producto('Parlante Portatil Go',10,24700,'parlante.jpg',101)
#catalogo.agregar_producto('Auricular Inhalambrico M10 Pro Superior',8,94500, 'auricular_in.jpg',102)
#catalogo.agregar_producto('Auricular Bluetooth de diadema M8',15, 44700,'auricular_blu.jpg',103)
#catalogo.agregar_producto('Teclado Gamer con retroiluminacion Led A24',10,67800,'teclado.jpg',104)
#catalogo.agregar_producto('Monitor Led 21,5 pulgadas marca H', 6,97500,'minitor.jpg',105)
#catalogo.agregar_producto('Notebook A 16p Pro 8g ram',8,174300,'notebook.jpg',106)

# Consultar un producto y mostrar
#cod_prod = int(input("Ingrese el codigo del producto: ")) 
#producto = catalogo.consultar_producto(cod_prod)    
#if producto:
    #print(f"Producto encontrado: {producto['codigo']} = {producto['descripcion']}")  
#else:
    #print(f"Producto {cod_prod} no encontrado")

#Modificar un  producto
#catalogo.mostrar_producto(2)
#catalogo.modificar_producto(2, 'Parlante Portatil Inhalambrico Go', 15,25300, 'parlante.jpg', 110)
#catalogo.mostrar_producto(2)

#Listar productos
#productos = catalogo.listar_producto()
#for producto in productos:
    #print(producto)

#Eliminar producto
#catalogo.eliminar_productos(7)
#productos = catalogo.listar_producto()
#for producto in productos:
    #print(producto)
