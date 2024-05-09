# dilevery de sushi
# 1 pikachu roll $ 4500
# otaku roll $ 5000
# pulpo venenoso roll $ 5200
# anguila electrica roll $ 4800

import os
import time
def limpiar_pantalla():
    print("La pantalla se limpiara en segundos...")
    time.sleep(2)
    os.system('cls')
pikachu_roll= 4500
otaku_roll= 5000
pulpo_venenosa_roll=5200
anguila_eléctrica_roll=4800

s=True
pikachu_roll= 4500
otaku_roll= 5000
pulpo_venenosa_roll=5200
anguila_eléctrica_roll=4800

print("bienvenidos a sushi 4 menus")
print("****************************")

pikachu_roll=int(input("ingrese la cantidad pikachu_roll:"))
otaku_roll=int(input("ingrese la cantidad otaku_roll:"))
pulpo_venenoso_roll=int(input("ingrese la cantidad pulpo_venenoso_roll:"))
anguila_electrica_roll=int(input("ingrese la cantidad anguila_electrica_roll:"))

os.system('cls')
while (s==True):
    print("bienvenidos a dilebery sushi de 4 menus\n")
    print("nuestro menus de 4 servivio","pikachu_roll $ 4500","otaku_roll$5000","pulpo_venenos_roll$5200","anguila_electrica_roll$4800", sep="\n")
    Total= pikachu_roll*4500 + otaku_roll*5000 + pulpo_venenoso_roll*5200 + anguila_electrica_roll*4800
    print("cancelar el valor de su pedido es:",Total)
   
    precio=float(input()) 
    contraseña=input("ingrese contraseña:")
    if contraseña=="soyotaku":
        print("es correcto")
    else:
        print("es incorrecta:")
     
    descuento=precio * 0.10
    Total_final=Total-descuento

    print("***************************************")
  
    print(f"el precio final a pagar es de ${Total_final:}")
            
    print("gracias por preferir sushi 4 menus")
    print("__________________________________")
          
  

