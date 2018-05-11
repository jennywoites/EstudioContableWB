from Percepciones.percepciones_desde_bas import generar_archivos_percepciones

SALIR = 0

POS_TEXTO = 0
POS_FUNCION = 1

OPCIONES = [
    ("Salir", ""),
    ("Generar archivos de percepciones", generar_archivos_percepciones)
]

def mostrar_menu():
    for numero, opcion in enumerate(OPCIONES):
        print("{}: {}".format(numero, opcion[POS_TEXTO]))    

def elegir_opcion():
    print("Ingrese el número de opción y presione ENTER")
    mostrar_menu()
    opcion_elegida = input("Opción: ")
    if not opcion_elegida.isdigit() or int(opcion_elegida) >= len(OPCIONES):
        print("Opción no válida")
        return -1
    return int(opcion_elegida)

def main():
    opcion = -1
    while(opcion != SALIR):
        print()
        opcion = elegir_opcion()
        if opcion > 0:
            func_accion = OPCIONES[opcion][POS_FUNCION]
            func_accion()
    print("Adiós!! =)")

main()