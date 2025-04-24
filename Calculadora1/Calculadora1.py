#ejercicio 1= calculadora basica
#autor: Bryan Cadena Agudelo
#correo: bcadena32@gmail.com
#fecha: 03/03/25

class Operacion:
    def calcular(self, num1, num2):
        pass

class Suma(Operacion):
    def calcular(self, num1, num2):
        return num1 + num2

class Resta(Operacion):
    def calcular(self, num1, num2):
        return num1 - num2

class Multiplicacion(Operacion):
    def calcular(self, num1, num2):
        return num1 * num2

class Division(Operacion):
    def calcular(self, num1, num2):
        if num2 == 0:
            return "Error: No se puede dividir por cero"
        return num1 / num2

operaciones = {
    "suma": Suma(),
    "resta": Resta(),
    "multiplicacion": Multiplicacion(),
    "division": Division()
}

print("Calculadora con Operaciones como Objetos")
print("Operaciones disponibles: suma, resta, multiplicacion, division")

while True:
    operacion_nombre = input("Introduce la operación (o 'salir' para terminar): ").lower()
    if operacion_nombre == "salir":
        break

    if operacion_nombre not in operaciones:
        print("Operación no válida. Por favor, elige una de las operaciones disponibles.")
        continue

    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
    except ValueError:
        print("Entrada inválida. Por favor, introduce números.")
        continue

    operacion = operaciones[operacion_nombre]
    resultado = operacion.calcular(num1, num2)
    print("Resultado:", resultado)