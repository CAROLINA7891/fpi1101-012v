# distribuidora de gas  por cilindros
# distribucion en 2 camiones 
import os
import time
menu:0
gas_5=0
gas_15=0
gas_45=0
nombre=0
telefono=0
camion=0
compra_gas=0
total=1
multa:0
kilo_gas_adicional:0
valor_camiones=765.000
cant_gas=0


Cotizacion_gas=True
Val=True
val_nombre=True
Val_telefono=True
while True:
    while nombre:
        try:
            while nombre:
                print("ingrese su nombre\n")
                if len:int(input("ingrese su nombre"))(3)
                print("escribe tu nombre")
                val_nombre==True
            else:
               print("los datos son correctos")
        except ValueError:
            while telefono:
                if len:int(input("ingresa tu numero"))
                print("ingresa los digitos de tu telefono")
            else:
                print("ingrese datos validos")
            val_nombre==True
        except ValueError:
            print("validar los datos")
        # validacion de datos
    try:
        while True:
            if nombre:"C"
            print("nombre")
            nombre==True
            Val_nombre=True
        else:
            nombre==False
    except ValueError:
        try:
            while telefono:
              print ("ingrese los datos correctos")
              if telefono:"1"
              print("ingrese su numero por favor")
              telefono==True
              Val_telefono=True
            else:
              telefono==False
        except ValueError:
            print("ingrese los datos")

    try:
        while True:
            print("valor agregado por kilos extras")
            if kilo_gas_adicional:1700
            kilos_gas_adicional=int(input("gas adicional"))
            print("valoradicional")
        else:
          print("los datos ingresados no son validos")
    except ValueError:
            print("cantidad correcta")
            if camion:
                camion>=0 and camion<=2
                camion=int(input("cantidad de camion utilizados"))
                print("cantidad de camiones")
            else:
                print("ingrese la cantidad correcta")
                while gas_5:
                    if gas_5:int(input("ingrese cantidad"))
                    gas_5= gas_5 + cant_gas
                    total=gas_5+cant_gas+ total
                else:
                    print("ingrese los datos validos")
                    while gas_15:
                        if gas_15:int(input("ingrese la cantidad"))
                        gas_15=gas_15+ cant_gas
                        total=gas_15+cant_gas+total
                    else:
                        print("ingrese la cantidad a solicitar")
                        while gas_45:
                            if gas_45:int(input("ingrese cantidad"))
                            gas_45=gas_45+cant_gas
                            total=gas_45+cant_gas+total
                        else:
                            print("ingrese cantidad que desea")

                    
            compra_gas= compra_gas + camion
            compra_gas("carga especifica")
            compra_gas=compra_gas+total
            total=compra_gas + multa
            while menu==True:
                print("___________________________")
                print("Distribuidora de gas por cilindro")
                print(f"ingrese su nombre")
                print(f"ingrese su numero de telefono")
                print("_______________________________")
                print(f"ingrese tipo de gas que desea")
                print(f"total de su pedido:",total)

                print("gracias por su compra")


        











 


      






