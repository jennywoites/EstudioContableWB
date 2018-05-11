import os
from Percepciones.CargadorDatosProveedorBAS import CargadorDatosProveedorBAS
from Percepciones.GeneradorArchivosPercepciones import GeneradorArchivosPercepciones
from Percepciones.GestorClientes import GestorClientes

ARCH_ENTRADA_PERCEPCIONES = "listado_percepciones.csv"
ARCH_PERCEPCIONES = "percepciones"
ARCH_ANULACIONES = "anulaciones"

ARCH_CLIENTES_CARGADOS = "CLIENTES_CARGADOS.csv"
ARCH_NUEVOS_CLIENTES = "nuevos_clientes.txt"

CLIENTES = [
    "Regresar al menu anterior",
    "OTAMENDI",
    "EDER"
]

def elegir_cliente():
    opcion = -1
    while(opcion != 0):
        pass

def obtener_nombres_de_archivos():
    print("Elija el cliente para el cual va a generar los datos")
    for num, cliente in enumerate(CLIENTES):
        print("{}: {}".fromat(num, cliente))
    opcion_elegida = input("Cliente: ")
    if not opcion_elegida.isdigit() or int(opcion_elegida) >= len(CLIENTES):
        print("Opción no válida")
        return -1
    return int(opcion_elegida)

def generar_archivos_percepciones():    
    gestor_clientes = GestorClientes(ARCH_CLIENTES_CARGADOS, ARCH_NUEVOS_CLIENTES)
    gestor_clientes.cargar_clientes_previos()

    percepciones = []
    anulaciones = []

    cargadorBAS = CargadorDatosProveedorBAS()
    cargadorBAS.cargar_datos_proveedor_bas(ARCH_ENTRADA_PERCEPCIONES, percepciones, anulaciones, gestor_clientes)

    generador_archivos = GeneradorArchivosPercepciones()
    generador_archivos.generar_archivos(ARCH_PERCEPCIONES, percepciones)
    generador_archivos.generar_archivos(ARCH_ANULACIONES, anulaciones)

    gestor_clientes.generar_archivo_clientes_nuevos()