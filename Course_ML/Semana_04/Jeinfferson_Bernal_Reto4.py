# Información de los cultivos guardada en un diccionario
cultivos = {
    'Tomate': {
        'Mantenimiento': 'Lunes, Jueves 4:00 pm',
        'Regado': 'Martes, Viernes 6:00 pm',
        'Abono': 'Miércoles 5:00 pm',
        'Etapas': [
            {'Nombre': 'Etapa 1 - Fase vegetativa', 'Duracion': '5 a 30 días'},
            {'Nombre': 'Etapa 2 - Fase Maduración', 'Duracion': '30 a 90 días'}
        ]
    },
    'Cebolla': {
        'Mantenimiento': 'Martes, Viernes 3:00 pm',
        'Regado': 'Lunes, Miércoles 7:00 pm',
        'Abono': 'Jueves 2:00 pm',
        'Etapas': [
            {'Nombre': 'Etapa 1 - Fase vegetativa', 'Duracion': '5 a 25 días'},
            {'Nombre': 'Etapa 2 - Fase Maduración', 'Duracion': '25 a 45 días'}
        ]
    }
}

# Funcion que retorna el nombre de los cultivos en una lista
def obtener_nombres_cultivos():
    return list(cultivos.keys())

# funcion que muestra el horario de gestion segun el cultivo dado
def mostrar_gestion_cultivo(nombre_cultivo):
    cultivo = cultivos[nombre_cultivo]
    print(f'\nCultivo: {nombre_cultivo}')
    print(f'Mantenimiento: {cultivo["Mantenimiento"]}')
    print(f'Regado: {cultivo["Regado"]}')
    print(f'Abono: {cultivo["Abono"]}')

# funcion que muestra las etapas del cultivo seleccionado
def mostrar_etapas_cultivo(nombre_cultivo):
    cultivo = cultivos[nombre_cultivo]
    print(f'\nEtapas del cultivo de {nombre_cultivo}')

    for etapa in cultivo['Etapas']:
        print(f"{etapa['Nombre']}: {etapa['Duracion']}")

# funcion que muestra la informacion contable del cultivo seleccionado
def mostrar_info_contable(nombre_cultivo):
    print('\n--- Información Contable ---')
    print('Aquí se desarrollará la funcionalidad de información contable.\n')

# funcion que muestra el menu de opciones
def menu():
    print('\n--- Menu de Gestión de Cultivos ---')
    print("1. Horario de Gestión de Cultivo")
    print("2. Etapas del Cultivo")
    print("3. Información Contable")
    print("4. Salir")   


# ciclo principal del menu 
while True:
    # mostrar menu
    menu()
    # pedir seleccion
    opcion = int(input('Seleccione una opcion: '))

    # evaluar opciones
    if opcion == 1 or opcion == 2 or opcion == 3:

        print('\nCultivos disponibles:')
        # lista con los nombres de los cultivos
        nombres_cultivos = obtener_nombres_cultivos()

        # mostrar nombre de los cultivos y su respectivo indice
        for ind, nombre in enumerate(nombres_cultivos, start=1):
            print(f'{ind}. {nombre}')

        # solicitar eleccion de cultivo
        eleccion =  int(input('Seleccione un cultivo: ')) - 1
        
        # evaluar eleccion
        if 0 <= eleccion < len(nombres_cultivos):
            cultivo_selec = nombres_cultivos[eleccion]

            if opcion == 1:
                mostrar_gestion_cultivo(cultivo_selec)
            
            elif opcion == 2:
                mostrar_etapas_cultivo(cultivo_selec)

            elif opcion == 3:
                mostrar_info_contable(cultivo_selec)

        else:
            print('Seleccion no valida')
    elif opcion == 4:
        print('Saliendo del programa...')
        break
    else:
        print('Opción no válida. Intente de nuevo.')