'''
    2.	Escribe un programa en Python que pregunte el nombre del usuario, su edad y su 
    correo electrónico y que luego imprima el siguiente mensaje en pantalla:

    Input: Digite su nombre: Pedro
	       Digite su edad: 30
	       Digite su correo electrónico: p3dr1t0_12345@gmail.com
    Output: Bienvenido al sistema Pedro, su correo electrónico es p3dr1t0_12345@gmail.com 
    y tiene 30 años de edad
'''

nombre = input('Digite su nombre: ')
edad = input('Digite su edad: ')
correo = input('Digite su correo electrónico: ')
print(f'Bienvenido al sistema {nombre}, su correo electrónico es {correo} y tiene {edad} años de edad')