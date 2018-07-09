from utils import *
import os

class GestorClientes:
    def __init__(self, arch_clientes_cargados, arch_nuevos_clientes):
        self.clientes = {}
        self.arch_clientes_cargados = arch_clientes_cargados

        self.clientes_nuevos = {}
        self.arch_nuevos_clientes = arch_nuevos_clientes

    def cargar_clientes_previos(self):
        self.clientes = {}
        if not os.path.exists(self.arch_clientes_cargados):
            with open(self.arch_clientes_cargados, 'w') as f:
                pass
            return self.clientes

        with open(self.arch_clientes_cargados, "r") as f_clientes:
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

        with open(self.arch_clientes_cargados, "a", encoding="latin1") as f_clientes_cargados:
            with open(self.arch_nuevos_clientes, "w", encoding="latin1") as f_clientes_nuevos:
                for cuit in self.clientes_nuevos:
                    razon_social = self.clientes_nuevos[cuit]
                    f_clientes_cargados.write(razon_social + SEPARADOR + cuit + ENTER)
                    f_clientes_nuevos.write(self.generar_linea_cliente(cuit, razon_social))
