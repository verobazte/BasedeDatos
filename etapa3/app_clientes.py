import mysql.connector

class Listado_clientes:
    def __init__(self, host, user, password,database):
        self.conn = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
        )
        self.cursor = self.conn.cursor(dictionary=True)

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
            codigo INT AUTO_INCREMENT PRIMARY KEY,
            apeynom VARCHAR(255) NOT NULL,
            domcalle VARCHAR(130) NULL,
            domnro int(10) NOT NULL,
            domciudad VARCHAR(50) NOT NULL,
            dompcia VARCHAR(50) NOT NULL,
            email VARCHAR(40)  NOT NULL,                        
            tel int (15) NOT NULL)''')
        
        self.conn.commit()

    def agregar_cliente(self,apeynom, domcalle, domnro, domciudad, dompcia, email, tel):
        sql = "INSERT INTO clientes(apeynom, domcalle, domnro, domciudad, dompcia, email, tel) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        valores =(apeynom, domcalle, domnro, domciudad, dompcia, email, tel)

        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.lastrowid
    
    def consultar_cliente(self, codigo):
        self.cursor.execute(f"SELECT * FROM clientes WHERE codigo = {codigo}")
        return self.cursor.fetchone()
    
    def modificar_cliente(self, codigo, nuevo_apeynom, nuevo_domcalle, nuevo_domnro, nuevo_domciudad, nuevo_dompcia, nuevo_email, nuevo_tel):
        sql = "UPDATE clientes SET apeynom = %s, domcalle= %s, domnro = %s, domciudad = %s, dompcia = %s, email= %s, tel = %s WHERE codigo = %s"
        valores = (nuevo_apeynom, nuevo_domcalle, nuevo_domnro, nuevo_domciudad, nuevo_dompcia, nuevo_email, nuevo_tel, codigo)

        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def mostrar_cliente(self, codigo):
        cliente = self.consultar_cliente(codigo)
        if cliente:
            print("-" * 40)
            print(f"Código...............:{cliente['codigo']}")
            print(f"Apellido y nombre....:{cliente['apeynom']}")
            print(f"Domicilio- calle.....:{cliente['domcalle']}")
            print(f"Domicilio- numero....:{cliente['domnro']}")
            print(f"Domicilio- ciudad....:{cliente['domciudad']}")
            print(f"Domicilio- provincia: {cliente['dompcia']}")
            print(f"Email................:{cliente['email']}")
            print(f"Teléfono.............:{cliente['tel']}")
            print("-" * 40)
        else:
            print("Cliente no encontrado")

    def listar_clientes(self):
        self.cursor.execute('SELECT * FROM clientes')
        clientes = self.cursor.fetchall()
        return clientes
    
    def eliminar_clientes(self, codigo):
        self.cursor.execute(f'DELETE FROM clientes WHERE codigo = {codigo}')
        self.conn.commit()
        return self.cursor.rowcount > 0
#-----------------------------------------------------
#Programa Principal


listado_clientes = Listado_clientes(host='localhost',user='root',password='',database='CodeCrafters')
                                    
#listado_clientes.agregar_cliente('Ruiz Juan','Dorrego',2434,'Bahia Blanca','Buenos Aires','juanr@gmail.com', 22547779) 
#listado_clientes.agregar_cliente('Sica Ana', 'Rodriguez', 776,'Oran', 'Salta', 'anasica@gmail.com',3333355)
#listado_clientes.agregar_cliente('Paz Federico', 'Av Balcarce', 6654, 'Mendoza', 'Mendoza', 'fedepaz@gmail.com',334434)
#listado_clientes.agregar_cliente('Lunati Julio', 'San Martín', 6656, 'Tandil', 'Buenos Aires', 'jl@gmail.com', 7777665)
#listado_clientes.agregar_cliente('Lima Rocio','Libertad',1343,'La Falda','Cordoba', 'rolima@gmail.com',7779978)
#listado_clientes.agregar_cliente('Benitez Juan', 'Balcace', 1122,'Viedma','Rio Negro', 'jbenitez@gmail.com',88764099)

# Consultar un cliente y mostrar
#cod_cliente= int(input("Ingrese el codigo del cliente: ")) 
#cliente = listado_clientes.consultar_cliente(cod_cliente)    
#if cliente:
    #print(f"Cliente encontrado: {cliente['codigo']} = {cliente['descripcion']}")  
#else:
    #print(f"Cliente {cod_cliente} no encontrado")

#Modificar un  cliente
#listado_clientes.mostrar_cliente(2)
#listado_clientes.modificar_cliente(2, 'Sica, Ana', 'Vieytes', 1234,'Oran', 'Salta', 'anasica@gmail.com',3333355)
#listado_clientes.mostrar_cliente(2)

#Listar clientes
#clientes = listado_clientes.listar_clientes()
#for cliente in clientes:
    #print(cliente)

#Eliminar cliente
#listado_clientes.eliminar_clientes(3)
#clientes = listado_clientes.listar_clientes()
#for cliente in clientes:
    #print(cliente)

