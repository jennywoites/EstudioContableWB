from CargadorDatosProveedorBAS import CargadorDatosProveedorBAS
from GeneradorArchivosPercepciones import GeneradorArchivosPercepciones
from GestorClientes import GestorClientes

ARCH_ENTRADA_PERCEPCIONES = "listado_percepciones.csv"
ARCH_PERCEPCIONES = "percepciones"
ARCH_ANULACIONES = "anulaciones"

def generar_archivos_percepciones():    
    gestor_clientes = GestorClientes()
    gestor_clientes.cargar_clientes_previos()

    percepciones = []
    anulaciones = []

    cargadorBAS = CargadorDatosProveedorBAS()
    cargadorBAS.cargar_datos_proveedor_bas(ARCH_ENTRADA_PERCEPCIONES, percepciones, anulaciones, gestor_clientes)

    generador_archivos = GeneradorArchivosPercepciones()
    generador_archivos.generar_archivos(ARCH_PERCEPCIONES, percepciones)
    generador_archivos.generar_archivos(ARCH_ANULACIONES, anulaciones)

    gestor_clientes.generar_archivo_clientes_nuevos()

generar_archivos_percepciones()