clientes = []

def agregar_cliente(codigo, apeynom, domcalle, domnro, domciudad, dompcia, email,tel):
    if consultar_cliente(codigo):
        print("El cliente ya existe")
        return False
    
    nuevo_cliente = {
    'codigo': codigo,
    'apeynom': apeynom,
    'domcalle': domcalle,
    'domnro': domnro,
    'domciudad': domciudad,
    'dompcia': dompcia,
    'email' : email,
    'tel' : tel
    }
    clientes.append(nuevo_cliente)
    return True

def consultar_cliente(codigo):
    for cliente in clientes:
        if cliente['codigo'] == codigo:
            return cliente
    return False

def modificar_cliente(codigo, nuevo_apeynom, nuevo_domcalle, nuevo_domnro, nuevo_domciudad, 
                      nueva_dompcia, nuevo_email, nuevo_tel):
    for cliente in clientes:
        if cliente['codigo'] == codigo:
            cliente['apeynom'] = nuevo_apeynom
            cliente['domcalle'] = nuevo_domcalle
            cliente['domnro'] = nuevo_domnro
            cliente['domciudad'] = nuevo_domciudad
            cliente['dompcia'] = nueva_dompcia
            cliente['email'] = nuevo_email
            cliente['tel'] = nuevo_tel
            return True
    return False

def  listar_clientes():
    print("_"*50)
    for cliente in clientes:
        print(f"Código...........: {cliente['codigo']}")
        print(f"Apellido y Nombre: {cliente['apeynom']}")
        print(f"Calle............: {cliente['domcalle']}")
        print(f"Número...........: {cliente['domnro']}")
        print(f"Ciudad...........: {cliente['domciudad']}")
        print(f"Provincia........: {cliente['dompcia']}")        
        print(f"Email............: {cliente['email']}")
        print(f"Teléfono.........: {cliente['tel']}")
        print("_"*50)


def eliminar_cliente(codigo):
    for cliente in clientes:
        if cliente['codigo'] == codigo:
            clientes.remove(cliente)
            return True
    return False

#------Programa principal
print("\033[H\033[J")

#Agregamos clientes
agregar_cliente(1,'Martinez Valeria','Vieytes', 2574,'Buenos Aires','jrod@gmail.com',777778878)
agregar_cliente(2,'Sica Ana', 'Rodriguez', 776,'Oran', 'Salta', 'anasica@gmail.com',333333355)
agregar_cliente(3, 'Paz Federico', 'Av Balcarce', 6654, 'Mendoza', 'Mendoza', 'fedepaz@gmail.com',334434)
agregar_cliente(4,'Lunati Julio', 'San Martín', 6656, 'Tandil', 'Buenos Aires', 'jl@gmail.com', 7777665)
agregar_cliente(5,'Lima Rocio','Libertad',1343,'La Falda','Cordoba', 'rolima@gmail.com',7779978)
agregar_cliente(6,'Benitez Juan', 'Balcace', 1122,'Viedma','Rio Negro', 'jbenitez@gmail.com',88764)

#listar_clientes()

#print("Vamos a eliminar a un cliente")
#eliminar_cliente(3)

#listar_clientes()

#print("Vamos a consultar un cliente")

print(consultar_cliente(2))
#print(consultar_cliente(9))

#print("Vamos a modificar a un cliente")
#print(consultar_cliente(2))
#modificar_cliente(2,'Auricular Inhalambrico M16 Pro Superior',9,97200,'auricular_in.jpg',102)
#print("-------------")
#print(consultar_cliente(2))




