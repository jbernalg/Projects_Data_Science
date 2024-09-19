'''
Administrador de Notas

Iniciamos la base de datos llamada "BD_estudiantes" con 2 estudiantes agregados
'''

# Estudiante con ID = 123
BD_estudiantes = {123: {'Nombre': 'Jose',
                        'Correo': 'xxxx',
                        'Telefono': 2033334,
                        'Fecha_Nacimiento': '30-11',
                        'Notas': [12, 14, 18, 9.5]
                        }}


# estudiante con ID = 124
BD_estudiantes[124] = {'Nombre': 'Miguel',
                        'Correo': 'xxxx',
                        'Telefono': 2012334,
                        'Fecha_Nacimiento': '30-11',
                        'Notas': [16.6, 12.2, 18, 14]
                        }


# ---------------- funciones ---------------------

# importamos libreria para calculos estadisticos
import numpy as np

# funcion que agrega nuevos estudiantes a la BD
def agregar():

    while True:

        ID = int(input('Ingrese ID del nuevo estudiante: '))
        
        if (ID in BD_estudiantes) == False:    
            nombre = input('Ingrese Nombre: ')
            correo = input('Ingrese el correo: ')
            telefono = int(input('Ingrese numero de telefono: '))
            fecha_na = input('Ingrese fecha de nacimiento: ')
            n1 = float(input('Ingrese Nota 1: '))
            n2 = float(input('Ingrese Nota 2: '))
            n3 = float(input('Ingrese Nota 3: '))
            n4 = float(input('Ingrese Nota 4: '))

            BD_estudiantes[ID] = {
            'Nombre': nombre,
            'Correo': correo,
            'Telefono': telefono,
            'Fecha_Nacimiento': fecha_na,
            'Notas': [n1, n2, n3, n4]
            }

            print('')
            print('Estudiante guardado exitosamente!')
        else:
            print('El ID ingresado ya existe. Ingrese un ID diferente!')    

        print('')
        cond = input('Presione "y" para agregar otro estudiante. \nCualquier otro caracter para ir al Menu principal: ')
        
        if cond != 'y':
            break


# funcion que verifica si un estudiante esta en la BD
def buscar(ID, BD = BD_estudiantes):

    if ID in BD:
        return True
    else:
        return False   


# Funcion que permite modificar la nota de un estudiante a partir de su ID
def modificar(ID):
    
    if buscar(ID) == True:
        new_n1 = int(input('Ingrese nueva nota 1: '))
        new_n2 = int(input('Ingrese nueva nota 2: '))
        new_n3 = int(input('Ingrese nueva nota 3: '))
        new_n4 = int(input('Ingrese nueva nota 4: '))

        BD_estudiantes[ID]['Notas'] = [new_n1, new_n2, new_n3, new_n4]
        print(f'Notas del estudiante {ID} han sido modificadas correctamente!')

    else:
        print('El ID ingresado no existe. Ingrese un ID correcto!')


# Funcion que permite eliminar un estudiante de la BD a partir de su ID
def cancelacion(ID):

    if buscar(ID) == True:
        BD_estudiantes.pop(ID)
        print('Eliminacion Exitosa!')
    else:
        print('Ingrese el ID correcto del estudiante que desea eliminar')


# Funcion que muestra las notas de los resultados de un estudiante a partir de su ID
def resultados(ID):

    if buscar(ID) == True:
        
        print('')
        print(f'#### Resultados del estudiante {ID} ####')
        # nota final
        notaF = nota_final(ID)
        print(f'Nota Final del estudiante: {notaF}')
        
        # nota promedio del grupo
        p_grupo = prom_grupo()
        print(f'Nota Promedio del grupo: {p_grupo}')

        # Verificar si esta por arriba o por debajo del promedio general
        if notaF > p_grupo:
            print('La nota final del estudiante esta por encima de promedio del grupo')
        elif notaF < p_grupo:
            print('La nota final del estudiante esta por debajo del promedio del grupo')
        else:
            print('La nota final del estudiante es igual al promedio del grupo')
    else:
        print('Ingrese un ID de estudiante valido')


# Funcion que devuelve el promedio del grupo
def prom_grupo(BD=BD_estudiantes):

    keys = BD.keys()
    sumaG = 0

    for i in keys:
        prom_ind = sum(BD[i]['Notas'])/4
        sumaG += prom_ind
    
    promG = sumaG/len(keys)

    return promG

# Funcion que devuelve la nota promedio del estudiante
def nota_final(ID, BD=BD_estudiantes):

    notaF = sum(BD[ID]['Notas'])/4
    return notaF


# Funcion que muestra la estadistica de cada estudiante y del grupo en general
def informe(BD=BD_estudiantes):

    keys = BD.keys()
    nf_estudiantes = []
    print('######## INFORME GENERAL DE TODOS LOS ESTUDIANTES ########')
    print('')

    print('#### Nota Final por estudiante ####')
    for i in keys:
        notaF = nota_final(i)
        print(f'Nota Final Estudiante {i}: {notaF}')
        nf_estudiantes.append(notaF)

    print('')
    print('#### Nota Promedio del Grupo ####')
    promedio_grupo = prom_grupo()
    print(f'Nota Promedio {promedio_grupo}')


    print('')
    sup, inf, equal = 0, 0, 0
    for i in nf_estudiantes:
        if i > promedio_grupo:
            sup += 1
        elif i < promedio_grupo:
            inf += 1
        else:
            equal += 1
    
    print('#### Cantidad de estudiantes por encima del promedio general ####')
    print('Total: ',sup)
    print('')
    print('#### Cantidad de estudiantes por debajo del promedio general ####')
    print('Total: ',inf)
    print('')
    print('#### Cantidad de estudiantes con promedio igual al general ####')
    print('Total: ',equal)
    
    print('')
    print('#### Moda de las notas ####')
    moda = np.bincount(nf_estudiantes).argmax()
    print('Moda: ', moda)

    print('')
    print('#### Mediana de las notas ####')
    mediana = np.median(nf_estudiantes) 
    print('Mediana: ', mediana)

    print('')
    print('#### Desviacion estandar de las notas ####')
    std = np.std(nf_estudiantes)
    print('Desviacion Estandar: ', std)

    print('')
    print('#### Distribucion de estudiante por percentil')
    pct_25 = np.percentile(nf_estudiantes, 25)
    pct_50 = np.percentile(nf_estudiantes, 50)  # Este es equivalente a la mediana
    pct_75 = np.percentile(nf_estudiantes, 75)

    cant_25, cant_50, cant_75, cant_100 = 0, 0, 0, 0
    for i in nf_estudiantes:
        if i <= pct_25:
            cant_25 += 1
        elif i > pct_25 and i <= pct_50:
            cant_50 += 1
        elif i > pct_50 and i <= pct_75:
            cant_75 += 1
        else:
            cant_100 += 1

    print(f'Cantidad estudiantes en Percentil 25: {cant_25}')
    print(f'Cantidad estudiantes en Percentil 50: {cant_50}')
    print(f'Cantidad estudiantes en Percentil 75: {cant_75}')
    print(f'Cantidad estudiantes en Percentil 100: {cant_100}')


# funcion que muestra el menu
def menu():

    while True:
        print('')
        print('#### Administrador de Notas ####')
        print('')
        print('1. Agregar')
        print('2. Buscar')
        print('3. Modificar')
        print('4. Cancelacion de materia')
        print('5. Resultados por estudiante')
        print('6. Informe del grupo')
        print('0. Salir')
        print('')
        opcion = input('Seleccione una opcion: ')

        if opcion.isdigit() == True and (int(opcion) >= 0 and int(opcion) < 7):
            return int(opcion)
        else:
            print('Ingrese una opcion correcta')


# ----------------------- inicio del programa -------------------------------
while True:
    
        opc = menu()

        if opc == 0:
            print('Cerrando Programa ...')
            break
        
        elif opc == 1:
            agregar()
        
        elif opc == 2:
            ID = input('Ingrese ID del estudiante: ')

            if ID.isdigit() == True:    
                ID = int(ID)
                if buscar(ID) == True:
                    print('')
                    print(f'#### Datos del Estudiante {ID} ####')
                    print('Nombre: ', BD_estudiantes[ID]['Nombre'])
                    print('Correo', BD_estudiantes[ID]['Correo'])
                    print('Telefono: ', BD_estudiantes[ID]['Telefono'])
                    print('Fecha de Nacimiento: ', BD_estudiantes[ID]['Fecha_Nacimiento'])
                    print('Nota 1: ', BD_estudiantes[ID]['Notas'][0])
                    print('Nota 2: ', BD_estudiantes[ID]['Notas'][1])
                    print('Nota 3: ', BD_estudiantes[ID]['Notas'][2])
                    print('Nota 4: ', BD_estudiantes[ID]['Notas'][3])
                    print('###############################')
                    print('')

                else:
                    print('El estudiante con ID ingresado no existe. Ingrese un ID correcto')
            
            else:
                print('Los ID son numericos. Ingrese un ID correcto!')

        elif opc == 3:
            ID = input('Ingrese el ID del estudiante a modificar notas: ')
            if ID.isdigit() == True:
                modificar(int(ID))
            else:
                print('los IDs son numericos. Ingrese un ID correcto!')

        elif opc == 4:
            ID = input('Ingrese el ID del estudiante a eliminar de la BD: ')
            if ID.isdigit() == True:
                cancelacion(int(ID))
            else:
                print('Los IDs son numericos. Ingrese un ID correcto!')

        elif opc == 5:
            ID = input('Ingrese el ID del estudiante: ')
            if ID.isdigit() == True:
                resultados(int(ID))
            else:
                print('El ID ingresado no existe. Ingrese un ID correcto')
        
        elif opc == 6:
            informe()