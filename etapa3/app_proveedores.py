import mysql.connector

class Listado_proveedores:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database ) 
        
        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS proveedores (
codigo INT AUTO_INCREMENT PRIMARY KEY,
cod_producto INT(20) NOT NULL,
descripcion VARCHAR(255) NOT NULL,
razon_social VARCHAR(20) NOT NULL
)''')

        self.conn.commit()

    def agregar_proveedor(self,cod_producto, descripcion, razon_social):
        sql = "INSERT INTO proveedores(cod_producto, descripcion, razon_social) VALUES (%s,%s,%s)"
        valores =(cod_producto, descripcion,razon_social)

        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.lastrowid
    
    def consultar_proveedor(self, codigo):
        self.cursor.execute(f"SELECT * FROM proveedores WHERE codigo = {codigo}")
        return self.cursor.fetchone()
    
    def modificar_proveedor(self, codigo,nuevo_cod_producto, nueva_descripcion, nueva_razon_social):
        sql = "UPDATE proveedores SET cod_producto = %s,descripcion = %s, razon_social = %s WHERE codigo = %s"
        valores = (nuevo_cod_producto, nueva_descripcion, nueva_razon_social, codigo)

        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def mostrar_proveedor(self, codigo):
        proveedor = self.consultar_proveedor(codigo)
        if proveedor:
            print("-" * 40)
            print(f"Código...............:{proveedor['codigo']}")
            print(f"Código del producto..:{proveedor['cod_producto']}")
            print(f"Descripción..........:{proveedor['descripcion']}")
            print(f"Razón Social.........:{proveedor['razon_social']}")
            print("-" * 40)
        else:
            print("Proveedor no encontrado")  

    def listar_proveedor(self):
        self.cursor.execute('SELECT * FROM proveedores')
        proveedores = self.cursor.fetchall()
        return proveedores   

    def eliminar_proveedor(self, codigo):
        self.cursor.execute(f'DELETE FROM proveedores WHERE codigo = {codigo}')
        self.conn.commit()
        return self.cursor.rowcount > 0 




#-----------------------------------------------------
#Programa Principal


listado_proveedores = Listado_proveedores(host='localhost',user='root',password='',database='CodeCrafters')

#listado_proveedores.agregar_proveedor(22,'Auricular inhalambrico', 'TecnoS.A.')
#listado_proveedores.agregar_proveedor(3,'Parlante Portatil Go','Atlia S.A')
#listado_proveedores.agregar_proveedor(2,'Teclado Gamer con retroiluminacion Led A24','MtaR S.A.')
#listado_proveedores.agregar_proveedor(1,'Notebook A 16p Pro 8g ram','IDEAS S.A')

# Consultar un proveedor y mostrar
#cod_proved = int(input("Ingrese el codigo del proveedor: ")) 
#proveedor = listado_proveedores.consultar_proveedor(cod_proved)    
#if proveedor:
    #print(f"Proveedor encontrado: {proveedor['codigo']} = {proveedor['descripcion']}")  
#else:
    #print(f"Proveedor {cod_proved} no encontrado")

#Modificar un  proveedor
#listado_proveedores.mostrar_producto(2)
#listado_proveedores.modificar_proveedor(2,22, 'Parlante Portatil Inhalambrico Go', 'Atlia S.A')
#listado_proveedores.mostrar_proveedor(2)

#Listar proveedores
#proveedores = listado_proveedores.listar_proveedor()
#for proveedor in proveedores:
    #print(proveedor)

#Eliminar proveedor
#listado_proveedores.eliminar_proveedor(7)
#proveedores = listado_proveedores.listar_producto()
#for proveedor in proveedores:
    #print(proveedor)