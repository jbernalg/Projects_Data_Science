'''
Administrador de Notas
'''

BD_estudiantes = {123: {'Nombre': 'Jose',
                        'Correo': 'xxxx',
                        'Telefono': 2033334,
                        'Fecha_Nacimiento': '30-11',
                        'Nota1': 12,
                        'Nota2': 18,
                        'nota3': 16,
                        'nota4': 20
                        }}

print(BD_estudiantes[123]['Nombre'])

BD_estudiantes[123]['Salud'] = 'buena'

print(BD_estudiantes)

BD_estudiantes[124] = {'Nombre': 'Miguel',
                       'Correo': 'xxxx',
                       'Telefono': 23922123,
                       'Fecha_Nacimiento': '20-08',
                       }

print(BD_estudiantes[124])


# ---------------- funciones ---------------------

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

agregar()
print(BD_estudiantes)
