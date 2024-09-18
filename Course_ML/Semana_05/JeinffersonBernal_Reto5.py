'''
Administrador de Notas
'''

BD_estudiantes = {123: {'Nombre': 'Jose',
                        'Correo': 'xxxx',
                        'Telefono': 2033334,
                        'Fecha_Nacimiento': '30-11',
                        'Nota1': 12,
                        'Nota2': 18,
                        'Nota3': 16,
                        'Nota4': 20
                        }}

print(BD_estudiantes[123]['Nombre'])


BD_estudiantes[124] = {'Nombre': 'Miguel',
                        'Correo': 'xxxx',
                        'Telefono': 2012334,
                        'Fecha_Nacimiento': '30-11',
                        'Nota1': 10,
                        'Nota2': 11,
                        'Nota3': 14,
                        'Nota4': 18
                        }

print(BD_estudiantes)
print(BD_estudiantes.keys())


# ---------------- funciones ---------------------

# importamos libreria para calculos estadisticos
import numpy as np

# funcion que agrega nuevos estudiantes a la BD
def agregar():

    while True:

        id = int(input('Ingrese ID del nuevo estudiante: '))
        nombre = input('Ingrese Nombre: ')
        correo = input('Ingrese el correo: ')
        telefono = int(input('Ingrese numero de telefono: '))
        fecha_na = input('Ingrese fecha de nacimiento: ')
        n1 = float(input('Ingrese Nota 1: '))
        n2 = float(input('Ingrese Nota 2: '))
        n3 = float(input('Ingrese Nota 3: '))
        n4 = float(input('Ingrese Nota 4: '))    

        BD_estudiantes[id] = {
            'Nombre': nombre,
            'Correo': correo,
            'Telefono': telefono,
            'Fecha_Nacimiento': fecha_na,
            'Nota1': n1,
            'Nota2': n2,
            'nota3': n3,
            'nota4': n4
        }

        print('')
        print('Estudiante guardado exitosamente!')
        cond = input('Presione "y" para agregar otro estudiante. \nCualquier otro caracter para ir al Menu principal: ')
        print('')
        print(' ')
        if cond != 'y':
            break

#agregar()
#print(BD_estudiantes)

# funcion que verifica si un estudiante esta en la BD
def buscar(id, BD = BD_estudiantes):

    if id in BD:
        return True
    else:
        return False
    

    
'''
id_est = int(input('Ingrese el ID del estudiante a buscar: '))

if buscar(id_est) == True:
    print('')
    print('#### Datos del Estudiante ####')
    print('Nombre: ', BD_estudiantes[id_est]['Nombre'])
    print('Correo', BD_estudiantes[id_est]['Correo'])
    print('Telefono: ', BD_estudiantes[id_est]['Telefono'])
    print('Fecha de Nacimiento: ', BD_estudiantes[id_est]['Fecha_Nacimiento'])
    print('Nota 1: ', BD_estudiantes[id_est]['Nota1'])
    print('Nota 2: ', BD_estudiantes[id_est]['Nota2'])
    print('Nota 3: ', BD_estudiantes[id_est]['Nota3'])
    print('Nota 4: ', BD_estudiantes[id_est]['Nota4'])
    print('###############################')
    print('')

else:
    print('El estudiante con ID ingresado no existe. Ingrese un Id correcto')
'''

def modificar(ID):
    
    if buscar(ID) == True:
        new_n1 = int(input('Ingrese nueva nota 1: '))
        new_n2 = int(input('Ingrese nueva nota 2: '))
        new_n3 = int(input('Ingrese nueva nota 3: '))
        new_n4 = int(input('Ingrese nueva nota 4: '))

        BD_estudiantes[ID]['Nota1'] = new_n1
        BD_estudiantes[ID]['Nota2'] = new_n2
        BD_estudiantes[ID]['Nota3'] = new_n3
        BD_estudiantes[ID]['Nota4'] = new_n4

    else:
        print('Ingrese in ID correcto para modificar las notas del estudiante correspondiente')


#modificar(123)
#print(BD_estudiantes)

def cancelacion(ID):

    if buscar(ID) == True:
        BD_estudiantes.pop(ID)
    else:
        print('Ingrese el ID correcto del estudiante que desea eliminar')

#cancelacion(124)
#print(BD_estudiantes)

def resultados(ID):

    if buscar(ID) == True:

        # nota final
        notaF = nota_final(ID)
        print(notaF)

        # nota promedio del grupo
        p_grupo = prom_grupo()

        # Verificar si esta por arria o por debajo del
        # promedio general
        if notaF > p_grupo:
            print('La nota final del estudiante esta por encima de promedio del grupo')
        elif notaF < p_grupo:
            print('La nota final del estudiante esta por debajo del promedio del grupo')
        else:
            print('La nota final del estudiante es igual al promedio del grupo')
    else:
        print('Ingrese un ID de estudiante valido')


# promedio del grupo
def prom_grupo(BD=BD_estudiantes):

    keys = BD.keys()
    sumaG = 0

    for i in keys:
        prom_ind = (BD[i]['Nota1'] + BD[i]['Nota2'] + BD[i]['Nota3'] + BD[i]['Nota4'])/4
        sumaG += prom_ind
    
    promG = sumaG/len(keys)

    return promG

# nota promedio del estudiante
def nota_final(ID, BD=BD_estudiantes):

    notaF = (BD[ID]['Nota1'] + BD[ID]['Nota2'] + BD[ID]['Nota3'] + BD[ID]['Nota4'])/4
    return notaF


#resultados(124)

def informe(BD=BD_estudiantes):

    keys = BD.keys()
    nf_estudiantes = []

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
    sup, inf, equal = 0
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
    print(f'Percentil 25: {pct_25}')
    print(f'Percentil 50: {pct_50}')
    print(f'Percentil 75: {pct_75}')

informe()
        


