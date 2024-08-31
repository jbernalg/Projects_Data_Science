 # Guardar información de los cultivos en diccionarios
cultivos = {
    'Arroz': {
        'Mantenimiento': 'Lunes, Jueves 4:00 pm',
        'Regado': 'Martes, Viernes 6:00 pm',
        'Abono': 'Miércoles 5:00 pm',
        'Etapas': [
            {'Nombre': 'Etapa 1 - Fase vegetativa', 'Duracion': '5 a 30 días'},
            {'Nombre': 'Etapa 2 - Fase maduración', 'Duracion': '30 a 90 días'}
        ]
    }
}

# Datos para la opción de información contable
gastos_mensuales = []
costos_fijos_mensuales = []
produccion_arroz = {}

# Ciclo Principal del menú
while True:
    print('\n--- Menú de Gestión de Cultivos ---')
    print("1. Horario de Gestión de Cultivo")
    print("2. Etapas del Cultivo")
    print("3. Información Contable")
    print("4. Salir")   

    opcion = input('Seleccione una opción: ')

    # --- Gestión de Cultivo ---
    if opcion == '1':
        print('\nCultivos disponibles: ')
        
        i = 1
        for cultivo in cultivos.keys():
            print(f'{i}. {cultivo}')
            i += 1

        # Selección del cultivo
        eleccion = int(input('Seleccione un cultivo: ')) - 1

        # Validación de la selección del cultivo
        if eleccion >= 0 and eleccion < len(cultivos):
            cultivo_seleccionado = list(cultivos.keys())[eleccion]
            print(f'\nCultivo: {cultivo_seleccionado}')
            print(f'Mantenimiento: {cultivos[cultivo_seleccionado]["Mantenimiento"]}')
            print(f'Regado: {cultivos[cultivo_seleccionado]["Regado"]}')
            print(f'Abono: {cultivos[cultivo_seleccionado]["Abono"]}')
        else:
            print('Selección no válida')

    # --- Etapas del Cultivo ---
    elif opcion == '2':
        print('\nCultivos disponibles:')
        
        i = 1
        for cultivo in cultivos.keys():
            print(f'{i}. {cultivo}')
            i += 1

        # Selección del cultivo
        eleccion = int(input('Seleccione un cultivo: ')) - 1

        # Validación de la selección del cultivo
        if eleccion >= 0 and eleccion < len(cultivos):
            cultivo_seleccionado = list(cultivos.keys())[eleccion]
            print(f'\nEtapas del Cultivo: {cultivo_seleccionado}')
            for etapa in cultivos[cultivo_seleccionado]['Etapas']:
                print(f'{etapa["Nombre"]}: {etapa["Duracion"]}')
            print()
        else:
            print('Selección no válida')

    # --- Información Contable ---
    elif opcion == '3':
        print('\n--- Información Contable ---')

        # Ingreso de gastos mensuales
        for mes in range(1, 6):
            print(f'\n--- Mes {mes} ---')
            medicamentos = float(input('Ingrese el valor de Medicamentos: '))
            imprevistos = float(input('Ingrese el valor de Imprevistos: '))
            gastos_mensuales.append({'Medicamentos': medicamentos, 'Imprevistos': imprevistos})

        # Ingreso de costos fijos mensuales
        for mes in range(1, 6):
            print(f'\n--- Mes {mes} ---')
            mano_de_obra = float(input('Ingrese el valor de Mano de Obra: '))
            abono = float(input('Ingrese el valor de Abono: '))
            agua = float(input('Ingrese el valor de Agua: '))
            mantenimiento = float(input('Ingrese el valor de Mantenimiento: '))
            costos_fijos_mensuales.append({'Mano de Obra': mano_de_obra, 'Abono': abono, 'Agua': agua, 'Mantenimiento': mantenimiento})

        # Ingreso de producción
        valor_arroba = float(input('\nIngrese el valor de la arroba (12.5 kg) de arroz: '))
        kilos_recolectados = float(input('Ingrese la cantidad de kilos recolectados: '))
        produccion_arroz = {'Valor Arroba': valor_arroba, 'Kilos Recolectados': kilos_recolectados}

        # --- Cálculos y Resultados ---
        total_gastos = sum([sum(gasto.values()) for gasto in gastos_mensuales])
        total_costos_fijos = sum([sum(costo.values()) for costo in costos_fijos_mensuales])

        # a. Costos totales del cultivo por mes
        print('\n--- Costos Totales por Mes ---')
        for mes in range(5):
            total_mes = sum(gastos_mensuales[mes].values()) + sum(costos_fijos_mensuales[mes].values())
            print(f'Mes {mes + 1}: {total_mes:.2f}')

        # b. Costos totales de mano de obra
        total_mano_obra = sum([costo['Mano de Obra'] for costo in costos_fijos_mensuales])
        print(f'\nCostos Totales de Mano de Obra: {total_mano_obra:.2f}')

        # c. Meses en los cuales no hubo gastos
        meses_sin_gastos = [mes + 1 for mes in range(5) if sum(gastos_mensuales[mes].values()) == 0]
        print(f'\nMeses sin Gastos: {meses_sin_gastos}')

        # d. Meses en los cuales el gasto fue menor a 100.000
        meses_gasto_menor = [mes + 1 for mes in range(5) if sum(gastos_mensuales[mes].values()) < 100000]
        print(f'\nMeses con Gasto Menor a 100.000: {meses_gasto_menor}')

        # e. Meses en los cuales el costo total del mes fue mayor al gasto total del mes
        meses_costo_mayor = [mes + 1 for mes in range(5) if sum(costos_fijos_mensuales[mes].values()) > sum(gastos_mensuales[mes].values())]
        print(f'\nMeses donde Costo Total es Mayor que Gasto Total: {meses_costo_mayor}')

        # f. Valor promedio de costos Fijos y costos variables
        promedio_costos_fijos = total_costos_fijos / 5
        promedio_gastos = total_gastos / 5
        print(f'\nPromedio de Costos Fijos: {promedio_costos_fijos:.2f}')
        print(f'Promedio de Gastos: {promedio_gastos:.2f}')

        # g. ¿Hubo ganancia? SI o NO
        valor_total_produccion = (produccion_arroz['Kilos Recolectados'] / 12.5) * produccion_arroz['Valor Arroba']
        ganancia = valor_total_produccion - (total_costos_fijos + total_gastos)
        if ganancia > 0:
            print(f'\nHubo Ganancia: Sí, Ganancia de: {ganancia:.2f}')
        else:
            print(f'\nHubo Ganancia: No')

        # h. Ganancia con incremento del 37% en el precio del arroz
        valor_arroba_incrementado = produccion_arroz['Valor Arroba'] * 1.37
        ganancia_incrementada = (produccion_arroz['Kilos Recolectados'] / 12.5) * valor_arroba_incrementado - (total_costos_fijos + total_gastos)
        print(f'\nGanancia con Incremento del 37% en el precio del arroz: {ganancia_incrementada:.2f}')

        # i. Ganancia con reducción del 5% en costos y gastos, y 63% en la producción
        costos_reducidos = (total_costos_fijos + total_gastos) * 0.95
        produccion_reducida = produccion_arroz['Kilos Recolectados'] * 0.37
        ganancia_reducida = (produccion_reducida / 12.5) * produccion_arroz['Valor Arroba'] - costos_reducidos
        print(f'\nGanancia con Reducción de Costos y Producción: {ganancia_reducida:.2f}')

    # --- Salir del Programa ---
    elif opcion == '4':
        print('Saliendo del programa')
        break

    else:
        print('Opción no válida. Ingrese una opción correcta')
