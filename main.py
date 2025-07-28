def invertir_cadena(cadena):
    if len(cadena) == 0:
        return ""
    else:
        return invertir_cadena(cadena[1:]) + cadena[0]

def suma_n_numeros(n):
    if n == 1:
        return 1
    else:
        return n + suma_n_numeros(n - 1)

def cuenta_regresiva(n):
    if n == 0:
        return
    else:
        print(n)
        cuenta_regresiva(n - 1)

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)

def contar_digitos(n):
    n = abs(n)
    if n < 10:
        return 1
    else:
        return 1 + contar_digitos(n // 10)

while True:
    print("\n==== MENÚ ====")
    print("1. Invertir una cadena de texto")
    print("2. Calcular la suma de los primeros N números naturales")
    print("3. Imprimir una cuenta regresiva desde N hasta 1")
    print("4. Sumar los dígitos de un número")
    print("5. Contar cuántos dígitos tiene un número")
    print("6. Salir")
    
    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":
        cadena = input("Ingrese una palabra o frase: ")
        print("Cadena invertida:", invertir_cadena(cadena))

    elif opcion == "2":
        n = int(input("Ingrese un número entero positivo: "))
        if n > 0:
            print("Suma:", suma_n_numeros(n))
        else:
            print("Debe ser un número positivo.")

    elif opcion == "3":
        n = int(input("Ingrese un número: "))
        print("Cuenta regresiva:")
        cuenta_regresiva(n)

    elif opcion == "4":
        n = int(input("Ingrese un número entero positivo: "))
        if n >= 0:
            print("Suma de los dígitos:", suma_digitos(n))
        else:
            print("Debe ser un número positivo.")

    elif opcion == "5":
        n = int(input("Ingrese un número entero: "))
        print("Cantidad de dígitos:", contar_digitos(n))

    elif opcion == "6":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intente de nuevo.")

