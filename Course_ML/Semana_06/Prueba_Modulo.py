'''
Importar las funciones de MiModulo.py
y operar con ellas
'''
import MiModulo

print(MiModulo.suma(10, 23))
print(MiModulo.resta(9,4))

'''
Importar unicamente los componentes que nos interesa
'''
from MiModulo import suma

print(suma(12, 56))

'''
Importar todos los componentes de la libreria con *
'''
from MiModulo import *
print(suma(12, 4))
print(resta(2,1))