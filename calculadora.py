def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

def calculadora():
    print("Calculadora Básica")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    operacion = input("Selecciona una operación (1/2/3/4): ")

    if operacion in ['1', '2', '3', '4']:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if operacion == '1':
            print(f"Resultado: {num1} + {num2} = {suma(num1, num2)}")
        elif operacion == '2':
            print(f"Resultado: {num1} - {num2} = {resta(num1, num2)}")
        elif operacion == '3':
            print(f"Resultado: {num1} * {num2} = {multiplicacion(num1, num2)}")
        elif operacion == '4':
            print(f"Resultado: {num1} / {num2} = {division(num1, num2)}")
    else:
        print("Operación no válida")

if __name__ == "__main__":
    calculadora()