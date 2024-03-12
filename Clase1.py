n=int(input("ingresa un numero -> "))
a=2
b=0
while a<n:
    if n%a==0:
        print("no es primo")
        b=1
        break
    a=a+1
if b==0:
    print("es primo")


         

              

  