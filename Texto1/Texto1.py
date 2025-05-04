
def mostrar_menu():
    print("\nEscriba una opción:")
    print("1 para pasar a minúsculas,")
    print("2 para pasar a mayúsculas,")
    print("3 para invertir mayúsculas y minúsculas")
    print("4 para pasar a capitalización.")
    print("5 para pasar a titulación.")
    print("6 para reemplazar espacios por guiones bajos.")
    print("7 para salir.")

def main():
    texto = input("Ingrese la línea de texto:\n> ")
    
    while True:
        mostrar_menu()
        opcion = input("\n> ")

        if opcion == "1":
            texto = texto.lower()
        elif opcion == "2":
            texto = texto.upper()
        elif opcion == "3":
            texto = texto.swapcase()
        elif opcion == "4":
            texto = texto.capitalize()
        elif opcion == "5":
            texto = texto.title()
        elif opcion == "6":
            texto = texto.lower().replace(" ", "_")  # <- modificación aquí
        elif opcion == "7":
            print("> Gracias!")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")
            continue

        print(f"\n> Resultado: {texto}")

if __name__ == "__main__":
    main()
