'''
Modulo con una funcion y varias sentencias a ejecutar
'''

def pow(a):
    return a*a

def abs (b):
    return -b

# linea de codigo agregada para que al importar el
# modulo no lleve las sentencias contenidas
if (__name__ == '__main__'):
    potencia = pow(3)
    v_absoluto = abs(-234)
    print(potencia, v_absoluto)