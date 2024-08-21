'''
menú para llevar a cabo la gestión de recolección y mantenimiento de los cultivos de la 
huerta escolar.
'''

# Guardar informacion de los cultivos en diccionarios
cultivos = {
    'Tomate': {
        'Mantenimiento': 'Lunes, Jueves 4:00 pm',
        'Regado': 'Martes, Viernes 6:00 pm',
        'Abono': 'Miercoles 5:00 pm',
        'Etapas': [
            {'Nombre': 'Etapa 1 - Fase vegetativa', 'Duracion': '5 a 30 dias'},
            {'Nombre': 'Etapa 2 - Fase Maduracion', 'Duracion': '30 a 90 dias'}
        ]
    },
    'Cebolla': {
        'Mantenimiento': 'Martes, Viernes 3:00 pm',
        'Regado': 'Lunes, Miercoles 7:00 pm',
        'Abono': 'Jueves 2:00 pm',
        'Etapas': [
            {'Nombre': 'Etapa 1 - Fase vegetativa', 'Duracion': '5 a 25 dias'},
            {'Nombre': 'Etapa 2 - Fase Maduracion', 'Duracion': '25 a 45 dias'}
        ]
    }
}


# Ciclo Principal del menu
while True:
    print('\n--- Menu de Gestion de Cultivos ---')
    print("1. Horario de Gestion de Cultivo")
    print("2. Etapas del Cultivo")
    print("3. Informacion Contable")
    print("4. Salir")   

    opcion = input('Seleccione una opcion: ')

    # opcion para horarios de gestion
    if opcion == '1':
        print('\nCultivos disponibles: ')
        
        i = 1
        for cultivo in cultivos.keys():
            print(f'{i}. {cultivo}')
            i += 1

        # seleccion del cultivo
        eleccion = int(input('Seleccione un cultivo: ')) - 1

        if eleccion >= 0 and eleccion < len(cultivos):
            cultivo_seleccionado = list(cultivos.keys())[eleccion]
            print(f'\nCultivo:{cultivo_seleccionado}')
            print(f"Mantenimiento: {cultivos[cultivo_seleccionado]['Mantenimiento']}")
            print(f"Regado: {cultivos[cultivo_seleccionado]['Regado']}")
            print(f"Abono: {cultivos[cultivo_seleccionado]['Abono']}")
        else:
            print('Seleccion no valida')

    # opcion para ver etapas del cultivo
    elif opcion == '2':
        print('\nCultivos disponibles:')
        
        i = 1
        for cultivo in cultivos.keys():
            print(f'{i}. {cultivo}')
            i += 1

        # seleccion de cultivo
        eleccion = int(input("Seleccione un cultivo: ")) - 1

        if eleccion >= 0 and eleccion < len(cultivos):
            cultivo_seleccionado = list(cultivos.keys())[eleccion]
            print(f'\nEtapas del Cultivo: {cultivo_seleccionado}')
            for etapa in cultivos[cultivo_seleccionado]['Etapas']:
                print(f"{etapa['Nombre']}: {etapa['Duracion']}")
            print()
        else:
            print('Seleccion no valida')

        
    # opcion de informacion contable
    elif opcion == '3':
        print('\n--- Informacion Contable ---')
        continue

    # opcion para salir del programa
    elif opcion == '4':
        print('Saliendo del programa')
        break

    else:
        print('Opcion no valida. Ingrese una opcion correcta')
