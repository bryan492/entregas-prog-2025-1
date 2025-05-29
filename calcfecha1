#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ejercicio: Calculadora de fechas

Autor : Bryan Cadena Agudelo
Correo: bcadena32@gmail.com
Fecha : 28/05/2025
"""

from datetime import datetime, timedelta

def pedir_float_positivo(mensaje: str) -> float:
    """Solicita un número flotante positivo al usuario, validando entrada."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("> Por favor ingrese un número positivo.")
                continue
            return valor
        except ValueError:
            print("> Entrada inválida. Por favor, escriba un número válido.")

def mostrar_fecha(fecha: datetime, titulo: str = "Fecha") -> None:
    """Muestra la fecha en un formato legible."""
    print(f"> {titulo}: {fecha.strftime('%Y-%m-%d %H:%M:%S')}")

def menu_principal():
    """Despliega el menú principal de opciones."""
    print("\n> Seleccione una opción:")
    print("  1. Sumar segundos a la fecha actual")
    print("  2. Sumar días a la fecha actual")
    print("  3. Salir")

def main():
    while True:
        fecha_actual = datetime.now()
        mostrar_fecha(fecha_actual, "Fecha actual")

        menu_principal()
        opcion = input("< ").strip()

        if opcion == "1":
            segundos = pedir_float_positivo("> Ingrese la cantidad de segundos: ")
            nueva_fecha = fecha_actual + timedelta(seconds=segundos)
            mostrar_fecha(nueva_fecha, "Nueva fecha")

        elif opcion == "2":
            dias = pedir_float_positivo("> Ingrese la cantidad de días: ")
            nueva_fecha = fecha_actual + timedelta(days=dias)
            mostrar_fecha(nueva_fecha, "Nueva fecha")

        elif opcion == "3":
            print("> ¡Gracias por usar la calculadora de fechas!")
            break

        else:
            print("> Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
