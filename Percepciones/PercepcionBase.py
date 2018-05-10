from Percepciones.DescripcionesPercepciones import *
from utils import completar_con_espacios, SEPARADOR

class PercepcionBase:
    def get_linea_para_txt(self):
        return "".join(self.get_lista_datos())

    def get_linea_para_csv(self):
        linea = ""
        for dato in self.get_lista_datos():
            dato = dato.rstrip()
            if SEPARADOR in dato:
                dato = '"' + dato + '"'
            linea += dato + SEPARADOR
        return linea

    def __str__(self):
        return self.get_linea_para_txt()
