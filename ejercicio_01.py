num1=float(input('Ingrese el primer numero: '))
num2=float(input('Ingrese el segundo numero: '))

suma=num1+num2
resta=num1-num2
multiplicacion=num1*num2
print('La suma es: ',suma)
print('La resta es: ',resta)
print('La multiplicacion es: ',multiplicacion)

if num2==0:
    print('No se puede dividir entre 0')
else:
    division=num1/num2
    print('La division es: ',division)