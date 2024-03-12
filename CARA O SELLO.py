import random 
c=input("ingrese su nombre jugador 1 -> ")
m=input("ingrese su nombre jugador 2 -> ")
Puntaje_J1=0
Puntaje_J2=0

while Puntaje_J1<5 and Puntaje_J2<5:
    b=random.randint(0,1)
    if b==0:
        print("salio cara", c, "ganó")
        Puntaje_J1+=1
    if b==1:
        print("salio sello", m, "ganó")
        Puntaje_J2+=1
    
if Puntaje_J1>Puntaje_J2:
    print("HA GANADO LA PARTIDA",c,"CON UN PUNTAJE TOTAL DE:",Puntaje_J1,"-",Puntaje_J2)
else:
    print("HA GANADO LA PARTIDA",m,"CON UN PUNTAJE TOTAL DE:",Puntaje_J2,"-",Puntaje_J1)
