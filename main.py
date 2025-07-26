def contar_destinos_recursivo(lista_de_listas):
    if not lista_de_listas:
        return 0
    primero, *resto = lista_de_listas
    return len(primero) + contar_destinos_recursivo(resto)

def contar_numeros(cant_numeros):
    if not cant_numeros:
        return 0
    return len(cant_numeros)

def suma_enteros(sumatoria):
    if not sumatoria:
        return 0
    primero, *resto=sumatoria
    return


 def mostrar_menu(self):
            while True:
                print("\n MENÚ PRINCIPAL ")
                print("1. Invertir una cadena de texto")
                print("2. Calcular la suma de los primeros N números naturales")
                print("3. Imprimir una cuenta regresiva desde N hasta 1")
                print("4.  Sumar los dígitos de un número")
                print("5. Contar cuántos dígitos tiene un número")
                print("6. Salir")

                opcion = input("Seleccione una opción (1-6): ")

                if opcion == '1':
                    self.invertir_cadena()
                elif opcion == '2':
                    self.suma_naturales()
                elif opcion == '3':
                    self.cuenta_regresiva()
                elif opcion == '4':
                    self.suma_digitos()
                elif opcion == '5':
                    print("👋 Saliendo del sistema.")
                    exit()
                else:
                    print("No ha ingresado una opción incorrecta. Intente nuevamente")
