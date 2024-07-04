class Listado_clientes:
    clientes = []
    

    def agregar_cliente(self, codigo, apeynom, domcalle, domnro, domciudad, dompcia, email, tel):
        if self.consultar_cliente(codigo):
            return False
        

        nuevo_cliente = {
            'codigo': codigo,
            'apeynom': apeynom,
            'domcalle': domcalle,
            'domnro': domnro,
            'domciudad': domciudad,
            'dompcia': dompcia,
            'email': email,
            'tel' :tel
        }
        self.clientes.append(nuevo_cliente)
        return True
    
    
    def consultar_cliente(self, codigo):
        for cliente in self.clientes:
            if cliente['codigo'] == codigo:
                return cliente
        return False
    
    def modificar_cliente(self,codigo, nuevo_apeynom, nuevo_domcalle, nuevo_domnro, nuevo_domciudad, nuevo_dompcia, nuevo_email, nuevo_tel):
        for cliente in self.clientes:
            if cliente['codigo'] == codigo:
                cliente['apeynom'] = nuevo_apeynom
                cliente['doncalle'] = nuevo_domcalle
                cliente['domnro'] = nuevo_domnro
                cliente['domciudad'] = nuevo_domciudad
                cliente['dompcia'] = nuevo_dompcia
                cliente['email'] = nuevo_email
                cliente['tel'] = nuevo_tel
                return True
        return False   
    
    def listar_clientes(self):
        print("-"*50)
        for cliente in self.clientes:
            print(f"Código............:{cliente['codigo']}")
            print(f"Apellido y Nombre.:{cliente['apeynom']}")
            print(f"Domicilio-Calle...:{cliente['domcalle']}")
            print(f"Domilio-Número....:{cliente['domnro']}")
            print(f"Domicilio-Ciudad..:{cliente['domciudad']}")
            print(f"Provincia.........:{cliente['dompcia']}")
            print(f"Email.............:{cliente['email']}")
            print(f"Teléfono..........:{cliente['tel']}")
            print("-"*50)

    def eliminar_cliente(self,codigo):
        for cliente in self.clientes:
            if cliente['codigo'] == codigo:
                self.clientes.remove(cliente)
                return True
        return False

    def mostrar_cliente(self,codigo):
        cliente = self.consultar_cliente(codigo)
        if cliente:
            print("*"*50)
            print(f"Código............:{cliente['codigo']}")
            print(f"Apellido y Nombre.:{cliente['apeynom']}")
            print(f"Domicilio-Calle...:{cliente['domcalle']}")
            print(f"Domilio-Número....:{cliente['domnro']}")
            print(f"Domicilio-Ciudad..:{cliente['domciudad']}")
            print(f"Provincia.........:{cliente['dompcia']}")
            print(f"Email.............:{cliente['email']}")
            print(f"Teléfono..........:{cliente['tel']}")
            print("*"*50)

        else:
            print(f"El cliente {codigo} no existe")

#------------------------------------
#Programa principal
#------------------------------------
print("\033[H\033[J")

listado_clientes =  Listado_clientes()
#Agregamos y consultamos productos


listado_clientes.agregar_cliente(1,'Ruiz, Juan','Dorrego', 2434,'Bahia Blanca', 'Buenos Aires',
                                'juanr@gmail.com',' 02254777')   

print("-----------------------")
print(listado_clientes.consultar_cliente(3))
print("-----------------------")
print(listado_clientes.consultar_cliente(15))    

listado_clientes.listar_clientes()      
print("-----------------------")
print('Eliminamos a un cliente')
listado_clientes.eliminar_cliente(4)
listado_clientes.listar_clientes()

print("-----------------------")
print("-----------------------")
print("-----------------------")
listado_clientes.mostrar_cliente(3)
listado_clientes.mostrar_cliente(25)