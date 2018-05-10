from utils import *

ARCH_CLIENTES_CARGADOS = "CLIENTES_CARGADOS.csv"
ARCH_NUEVOS_CLIENTES = "nuevos_clientes.txt"

class GestorClientes:
    def __init__(self):
        self.clientes = {}
        self.clientes_nuevos = {}

    def cargar_clientes_previos(self):
        self.clientes = {}
        with open(ARCH_CLIENTES_CARGADOS, "r") as f_clientes:
            for linea in f_clientes:
                linea = linea.rstrip(ENTER)
                razon_social, cuit = linea.split(SEPARADOR)
                self.clientes[cuit] = razon_social

    def buscar_o_crear_cliente_actual(self, cuit, razon_social):
        if not cuit in self.clientes:
            self.clientes_nuevos[cuit] = razon_social

    def generar_linea_cliente(self, cuit, razon_social):
        LEN_RAZON_SOCIAL = 70
        LEN_CUIT = 11
        LEN_ESPACIOS_BLANCO = 140

        linea = ""
        linea += completar_con_espacios(razon_social, LEN_RAZON_SOCIAL)
        linea += completar_con_espacios(cuit, LEN_CUIT)
        linea += completar_con_espacios("", LEN_ESPACIOS_BLANCO)
        linea += ENTER        
        return linea

    def generar_archivo_clientes_nuevos(self):
        if not self.clientes_nuevos:
            return

        with open(ARCH_CLIENTES_CARGADOS, "a") as f_clientes_cargados:
            with open(ARCH_NUEVOS_CLIENTES, "w") as f_clientes_nuevos:
                for cuit in self.clientes_nuevos:
                    razon_social = self.clientes_nuevos[cuit]
                    f_clientes_cargados.write(razon_social + SEPARADOR + cuit + ENTER)
                    f_clientes_nuevos.write(self.generar_linea_cliente(cuit, razon_social))
