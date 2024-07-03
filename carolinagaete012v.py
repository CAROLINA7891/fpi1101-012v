import os

registro=[]

# funcion resgistrar pedidos 
def registrar_datos():
    nombre=input("ingrese nombre y apellido")
    direccion=input("ingrese la direccion")
    sector=input("ingrese el sector")
    saco_5kg=input("ingrese la cantidad de saco")
    saco_10kg=input("ingrese la catidad de sacos")
    saco_20kg=input("ingrese la cantidad de sacos")

if not "nombre" or not "direccion" and "sector"<=0:
    print("los datos ingresados deben ser ingresados correctamente")
    
    registro={
    "nombre":"nombre",
    "direccion":"direccion",
    "sector": "sector",
    "saco_5kg": "saco_5kg",
    "saco_10kg":"saco_10kg",
    "saco_20kg":"saco_20kg"    
    }

    print("los datos se ingresaron correstamente")

#funcion crear lista de pedidos
def lista_pedidos():
    if not registro:
        print("no hay pedidos registrados")
    for registro in registro:
        print("ingrese su pedido")

# funcion inprimir la hojas de ruta
def hoja_ruta():
    if not registro:
        print("no hay rutas ingresadas")

    print("1.imprimir todas las rutas")
    print("2. imprimir por direccion")
    print("3. imprimir por sector")
    opcion=input ("seleccione una opcion valida")

    if opcion=="1":
        with open ("hoja_ruta.txt","r") as file:
            for registro in registro:
                file.write(f"nombre, direccion, sector, caso 5kg, saco 10kg, saco 20 kg,\n")
                print("hoja de ruta generada exitosamente")

    elif opcion=="2":
        direccion=input("hoja_ruta")
        with open(f"hoja_ruta-{direccion}.text","w") as file:
            for registro in registro:
                if registro[direccion]==direccion:
                    file.write(f"nombre, direccion, sector,caso 5kg, saco 10kg, saco 20 kg,\n")
        print("hoja de ruta se genera exitosamente")

    elif opcion=="3":
        sector=input("hoja_ruta")
        with open(f"hoja_ruta-{sector}.text","w") as file:
            for registro in registro:
                if registro[sector]==sector:
                    file.write(f"nombre, direccion, sector,caso 5kg, saco 10kg, saco 20 kg,\n")
        print("la hoja de ruta por sector se genera correctamente")

# ingresar los datos solicitados
def main():
    while True:
        print("\n menu:")
        print("1.registro de pedidos")
        print("2.listartodos los pedidos")
        print("3.imprimir hija de ruta")
        print("4.salir del programa")
        opcion=input("seleccione una opcion:")
        print("gracias por su preferencia")

    if opcion=="1":
        registro()
    elif opcion=="2":
        lista_pedidos()
    elif opcion=="3":
        hoja_ruta()
    elif opcion=="4":
        print("saliendo del programa")
        "break"
    else:
        print("opcion no valida. intente nuevamente")

"if__nombre__"=="__main__"
main()




    




