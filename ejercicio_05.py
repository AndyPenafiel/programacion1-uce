notas = []
aprobados = 0

for i in range(5):
    nota = float(input("Ingrese la calificación: "))

    if nota >= 0 and nota <= 20:
        notas.append(nota)

        if nota >= 14:
            aprobados = aprobados + 1

    else:
        print("Nota inválida. Debe estar entre 0 y 20.")
        break

if len(notas) == 5:
    promedio = sum(notas) / 5

    print("Notas:", notas)
    print("Promedio:", promedio)
    print("Nota mayor:", max(notas))
    print("Nota menor:", min(notas))
    print("Estudiantes aprobados:", aprobados)