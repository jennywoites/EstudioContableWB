from PercepcionBase import *

class Percepcion(PercepcionBase):

    LONGITUDES_CAMPO = {
        CONCEPTO: 2,
        FECHA: 10,
        TIPO_COMPROBANTE: 2,
        LETRA: 1,
        PREFIJO: 4,
        NUMERO_COMPROBANTE: 8,
        CUIT: 11,
        BASE_SUJETA: 15,
        ALICUOTA: 5,
        IMPUESTO: 15    
    }

    def __init__(self):
        self.concepto = "1"
        self.fecha = ""
        self.tipo = TIPO_FACTURA
        self.letra = "A"
        self.prefijo = ""
        self.comprobante = ""
        self.cuit = ""
        self.base_sujeta = ""
        self.alicuota = "1,5"
        self.impuesto = ""

    def get_lista_datos(self):
        lista = []
        lista.append(completar_con_espacios(self.concepto, self.LONGITUDES_CAMPO[CONCEPTO]))
        lista.append(completar_con_espacios(self.fecha, self.LONGITUDES_CAMPO[FECHA]))
        lista.append(completar_con_espacios(self.tipo, self.LONGITUDES_CAMPO[TIPO_COMPROBANTE]))
        lista.append(completar_con_espacios(self.letra, self.LONGITUDES_CAMPO[LETRA]))
        lista.append(completar_con_espacios(self.prefijo, self.LONGITUDES_CAMPO[PREFIJO]))
        lista.append(completar_con_espacios(self.comprobante, self.LONGITUDES_CAMPO[NUMERO_COMPROBANTE]))
        lista.append(completar_con_espacios(self.cuit, self.LONGITUDES_CAMPO[CUIT]))
        lista.append(completar_con_espacios(self.base_sujeta, self.LONGITUDES_CAMPO[BASE_SUJETA]))
        lista.append(completar_con_espacios(self.alicuota, self.LONGITUDES_CAMPO[ALICUOTA]))
        lista.append(completar_con_espacios(self.impuesto, self.LONGITUDES_CAMPO[IMPUESTO]))
        return lista