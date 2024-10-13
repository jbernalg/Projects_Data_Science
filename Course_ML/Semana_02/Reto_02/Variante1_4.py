'''
Nombre: Jeinfferson Bernal
C.I: 4606424
Correo: jeinffersonbernal@gmail.com
'''

'''
	4.- Haz un programa en Python que calcule la corriente eléctrica que pasa por 
    un circuito eléctrico que tiene una resistencia. Los valores de voltaje (V) 
    están dados en voltios, la corriente (I) en amperios y la resistencia (R) 
    en ohmios. Recuerda que V=IxR. Además, los datos deben ser ingresados 
    por el usuario:

    Input: Ingrese el primer número: 120
           Ingrese el segundo número: 15
    Output: La corriente eléctrica que pasa por el circuito es de 8.0 amperios
'''

voltaje = float(input('Ingrese valor de Voltaje en voltios: '))
resistencia = float(input('Ingrese valor de Resistencia en amperios: '))
print(f'La corriente electrica que pasa por el circuito es de {voltaje/resistencia} amperios')