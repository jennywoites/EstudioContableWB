from PercepcionBase import *

class Anulacion(PercepcionBase):

    LONGITUDES_CAMPO = {
        FECHA: 10,
        TIPO_COMPROBANTE: 2,
        LETRA: 1,
        NUMERO_COMPROBANTE: 12,
        FECHA_ANULACION: 10,
        IMPUESTO: 15,
        CUIT: 11
    }

    def __init__(self):
        self.fecha = ""
        self.tipo = TIPO_NOTA_DE_CREDITO
        self.letra = "A"
        self.numero = ""
        self.fecha_anulacion = ""
        self.impuesto = ""
        self.cuit = ""

    def get_lista_datos(self):
        lista = []
        lista.append(completar_con_espacios(self.fecha, self.LONGITUDES_CAMPO[FECHA]))
        lista.append(completar_con_espacios(self.tipo, self.LONGITUDES_CAMPO[TIPO_COMPROBANTE]))
        lista.append(completar_con_espacios(self.letra, self.LONGITUDES_CAMPO[LETRA]))
        lista.append(completar_con_espacios(self.numero, self.LONGITUDES_CAMPO[NUMERO_COMPROBANTE]))
        lista.append(completar_con_espacios(self.fecha_anulacion, self.LONGITUDES_CAMPO[FECHA_ANULACION]))
        lista.append(completar_con_espacios(self.impuesto, self.LONGITUDES_CAMPO[IMPUESTO]))
        lista.append(completar_con_espacios(self.cuit, self.LONGITUDES_CAMPO[CUIT]))
        return lista
