'''
	4.- Escribe un programa que convierta grados Celsius a grados Fahrenheit 
    sabiendo que (0°Cx9/5)+32= 32 °F y que imprima en pantalla el resultado:
    Input: Grados Celsius
    Output: Grados Fahrenheit
'''

celcius = float(input('Ingrese Grados Celcius: '))
fahr = celcius*(9/5) + 32
print(f'{fahr} Grados Fahrenheit')