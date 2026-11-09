edad=int(input('Ingrese su edad: '))

if edad <0:
 print('Edad no permitida. No puede ser negativa')
elif edad<12:
 print('Categoria: Niño')
elif edad<=17:
 print('Categoria: Adolescente')
elif edad<=64:
 print('Categoria: Adulto')
else:
 print('Categoria: Adulto mayor')