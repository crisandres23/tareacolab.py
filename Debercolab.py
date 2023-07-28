#FOrmula de la suma de numeros los N numeros
print("Ingrese el valor final (N)")
a = int(input())
b=0
for i in range(1 , a+1):
    print(i)
    b=b+i
    print("la suma es:" ,b)
