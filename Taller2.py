#Daniel Esteban Sanchez Castaño, Daniel Alejandro Parra, Jeronimo Diaz Rozo, Juan Esteban Gualtero
def exponencial(arreglo, numero):
    for i in range(numero):
        arreglo[i] = arreglo[i]**numero
    return arreglo
#Punto 1
arr = []
for i in range(15):
    arr.append(float(input(f"Digite el valor {i+1}: ")))
print(f"El arreglo es {arr}")
print(f"El cuadrado de cada numero es {exponencial(arr,2)}")
print(f"El cubo de cada numero es {exponencial(arr,3)}")

#Punto 2
cantiEstudiantes = 5
cantiMaterias = 5
estudiantes = {}
dic = {}
promedio = []
for i in range(cantiEstudiantes):
    nombre = ""
    nombre = input(f"Digite el nombre y apellido del estudiante {i+1}: ")
    for i in range(2):
        matNot = ["0" , 0]
        matNot[0] = input(f"Digite el nombre de la clase {i+1}: ")
        matNot[1] = input(f"Digite su nota en esta clase: ")
        dic[matNot[0]] = matNot[1]
    estudiantes[nombre] = dic
    dic = {}
suma = 0
sumaTotal = 0
promedioEstudiantes = []
for i in estudiantes:
    for x in estudiantes[i]:
        suma += estudiantes[i][x]
    estudiantes[i]["Promedio de notas"] = suma/cantiMaterias
    sumaTotal += estudiantes[i]["Promedio de notas"]
    promedioEstudiantes.append(estudiantes[i]["Promedio de notas"])
    suma = 0
for i in estudiantes:
    print(f'El promedio de {i} es {estudiantes[i]["Promedio de notas"]}')
print(f"Promedio de todos los estudiantes es {sumaTotal/cantiEstudiantes}")

#Punto 3
palabra = input("Ingrese una palabra: ")
letra = input("Ingrese una letra para buscar: ")
conta = 0
for i in palabra.lower():
    if letra == i:
        conta += 1
print(f"La letra {letra} se repite {conta}")