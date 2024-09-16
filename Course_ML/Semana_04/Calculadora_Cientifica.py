'''
Desarrolle una calculadora científica que permita realizar las siguientes operaciones.

•	Operaciones aritméticas básicas:  Las operaciones aritméticas básicas son Suma, resta, multiplicación, división.
•	Operaciones aritméticas extendidas: son la división entera, el residuo, la exponenciación a la n de número, 
    Raíz n (n puede ser 2,3,4,5) de un número, Logaritmo en base 10, Logaritmo, Valor absoluto, 1/numero, Factorial.
•	Operaciones Trigonométricas:  al menos dos, por ejemplo, seno(x), tangente(x).
•	Operaciones estadísticas Básicas:  Promedio, media, mediana, moda.  

'''
 # libreria de operaciones matematicas
import math 

# funcion suma
def operaciones_dosNumeros(num1, num2, opc):
    
    #suma
    if opc == 1:
        return num1 + num2
    # resta
    elif opc == 2:
        return num1 - num2
    # multiplicacion
    elif opc == 3:
        return num1*num2
    # division
    elif opc == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return 'Division por cero no es posible! Ingrese un divisor correcto'
    # division entera
    elif opc == 5:
        if num2 != 0:
            return num1 // num2
        else:
            return 'Division por cero no es posible! Ingrese un divisor correcto'
    # residuo
    elif opc == 6:
        if num2 != 0:
            return num1 // num2
        else:
            return 'Division por cero no es posible! Ingrese un divisor correcto'
             

# funcion exponenciacion: opc = 7
def exponenciacion(base, exp):
    if base >= 0:
        return math.pow(base, exp)
    else:
        return 'La operacion no esta definida para una base negativa'


# funcion raiz opc = 8
def raiz(num, root):
    if num < 0:
        if root%2 != 0:
            return math.pow(num, 1/root)
        else:
            return 'raiz no definida para valores negativos'
    else:
        return math.pow(num, 1/root)


# operaciones aplicadas a solo un numero
def operaciones_unNumero(num, opc):

    if num == 0 and (opc == 9 or opc == 10 or opc == 11):
        return 'Operacion no disponible para el numero cero'
    else:
        # logaritmo base 10
        if opc == 9:
            if num > 0:
                return math.log10(num)
            else:
                return 'operacion no definida para valores negativos o cero'
        
        # logaritmo natural
        elif opc == 10:
            if num > 0:
                return math.log(num)
            else:
                return 'operacion no definida para valores negativos o cero'
        
        # inversa de un numero
        elif opc == 11:
            if num != 0:
                return 1/num
            else:
                return 'la inversa de cero no esta definida'
        
        # valor absoluto
        elif opc == 12:
            return math.fabs(num)
        
        # factorial
        elif opc == 13:
            if num >=0 and type(num) == int:
                return math.factorial(num)
            else:
                return 'Solo existe el factorial para numero enteros positivos'
        
        # sen(x)
        elif opc == 14:
            return math.sin(num)
        
        # tangente(x)
        elif opc == 15:
            return math.tan(num)

# estadistica    
def promedio():
    
    lista = []
    while True:
        num = input('Ingrese numero o seleccione "=" para obtener el promedio de los numeros dados: ')

        if num == '=':
            if len(lista) > 0:
                print(sum(lista)/len(lista))
                break
            else:
                print('Ingrese al menos un numero para promediarlo!')
        elif num.isdigit() == True:
            lista.append(float(num))


def menu():
    print('\n--- Ingrese operacion a realizar ---')
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Division entera")
    print("6. Residuo de una division")
    print("7. Exponenciacion")
    print("8. Raiz de un numero")
    print("9. Logaritmo de base 10")
    print("10. Logaritmo natural")
    print("11. Inversa de un numero")
    print("12. Valor absoluto")
    print("13. Factorial")
    print("14. Seno de un numero")
    print("15. Tangente de un numero")
    print("16. Promedio")
    print("17. Salir de la calculadora")
    print("")


#Ciclo
while True:
    menu()
    opcion = int(input('Seleccione una operacion: '))

    if opcion == 17:
        print('Saliendo del la calculadora!...')
        break
    
    elif opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5 or opcion == 6:
            
        num1 = float(input('ingrese primer valor: '))
        num2 = float(input('ingrese segundo valor: '))

        if opcion == 1:
            print(operaciones_dosNumeros(num1, num2, 1))
        elif opcion == 2:
            print(operaciones_dosNumeros(num1, num2, 2))
        elif opcion == 3:
            print(operaciones_dosNumeros(num1, num2, 3))
        elif opcion == 4:
            print(operaciones_dosNumeros(num1, num2, 4))
        elif opcion == 5:
            print(operaciones_dosNumeros(num1, num2, 5))
        else:
            print(operaciones_dosNumeros(num1, num2, 6))
        
    elif opcion == 7:
        base = float(input('Ingrese la base: '))
        exp = float(input('Ingresa el exponente: '))
        print(exponenciacion(base, exp))

    elif opcion == 8:
        num = float(input('Ingrese numero: '))
        root = float(input('Ingrese valor de raiz deseada: '))
        print(raiz(num, root))

    elif opcion >= 9 and opcion < 16:
        num = float(input('Ingrese el numero: '))
        
        if opcion == 9:
            if num > 0:
                print(operaciones_unNumero(num, 9))
            else:
                print('La operacion no admite valores negativos')
        elif opcion == 10:
            if num > 0:
                print(operaciones_unNumero(num, 10))
            else:
                print('La operacion no admite valores negativos')
        elif opcion == 11:
            print(operaciones_unNumero(num, 11))
        elif opcion == 12:
            print(operaciones_unNumero(num, 12))
        elif opcion == 13:
            print(operaciones_unNumero(num, 13))
        elif opcion == 14:
            print(operaciones_unNumero(num, 14))
        elif opcion == 15:
            print(operaciones_unNumero(num, 15))

    elif opcion == 16:
        promedio()
    else:
        print('Ingrese una opcion correcta!')



