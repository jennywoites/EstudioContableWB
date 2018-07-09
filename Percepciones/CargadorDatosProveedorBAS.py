from utils import *
from Percepciones.Percepcion import Percepcion
from Percepciones.Anulacion import Anulacion

ABREVIADO_FACTURA = "FAC"
ABREVIADO_NOTA_DE_CREDITO = "NCR"
REGIMEN_LHE = "LHE"

class CargadorDatosProveedorBAS:
    """
    Utilizado para cargar los datos requeridos de percepciones y anulaciones
    en base a un archivo obtenido de BAS que posee las columnas de la manera
    que se indica en las constantes. Si se modifica una columna, se deben
    cambiar las columnas asociadas.
    """

    NUMERO_TRANSACCION = 0
    FECHA = 1
    FECHA_EXTERNA = 2
    TALONARIO = 3
    ABREVIADO = 4
    PREFIJO_EXTERNO = 5
    NUMERO_EXTERNO = 6
    COD_PRV = 7
    PROVINCIA = 8
    COD_CTA_CTE = 9
    NOMBRE = 10 #RAZON SOCIAL
    COD_DOC = 11
    NRO_DOC1 = 12 #CUIT
    NRO_DOC2 = 13
    COD_BAN = 14
    BANCO = 15
    COD_DOCB = 16
    NRO_DOC1B = 17
    NRO_DOC2B = 18
    REGIMEN = 19
    DESCRIPCION = 20
    IMPSUJ = 21
    IMPORTE = 22

    def agregar_percepcion(self, datos, percepciones):
        percepcion = Percepcion()

        percepcion.fecha = convertir_fecha(datos[self.FECHA])
        percepcion.prefijo = datos[self.PREFIJO_EXTERNO]
        percepcion.comprobante = datos[self.NUMERO_EXTERNO]
        percepcion.cuit = datos[self.NRO_DOC1]
        percepcion.base_sujeta = self.guardar_numero(datos[self.IMPSUJ])
        percepcion.impuesto = self.guardar_numero(datos[self.IMPORTE])

        percepciones.append(percepcion)

    def agregar_anulacion(self, datos, anulaciones):
        anulacion = Anulacion()

        anulacion.fecha = convertir_fecha(datos[self.FECHA])

        datos_letra = datos[self.NUMERO_EXTERNO].split(" ")
        if len(datos_letra) > 1:
            self.letra = datos_letra[-1]

        anulacion.numero = datos[self.NUMERO_EXTERNO]
        anulacion.fecha_anulacion = convertir_fecha(datos[self.FECHA])
        anulacion.impuesto = self.guardar_numero(datos[self.IMPORTE])
        anulacion.cuit = datos[self.NRO_DOC1]

        anulaciones.append(anulacion)

    SEPARADOR_NUMERO = "||"

    def guardar_numero(self, dato):
        numero = dato.replace(self.SEPARADOR_NUMERO, ",")
        while "." in numero:
            numero = numero.replace(".", "")
        return numero

    def limpiar_dato(self, dato):
        nuevo_dato = ""
        for caracter in dato:
            if not caracter.isdigit() and not caracter in ".,-":
                while(SEPARADOR in dato):
                    dato = dato.replace(SEPARADOR, " ")
                return dato

            if caracter in ".-":
                continue
            nuevo_dato += self.SEPARADOR_NUMERO if caracter == SEPARADOR else caracter
        return nuevo_dato

    def limpiar_linea(self, linea):
        linea = linea.rstrip(ENTER)

        while('"' in linea):
            pos_comilla = linea.index('"')
            parte_inicial_linea = linea[:pos_comilla]
            nueva_linea = linea[pos_comilla+1:]
            pos_nueva_comilla = nueva_linea.index('"')
            dato = self.limpiar_dato(nueva_linea[:pos_nueva_comilla])
            segunda_parte_linea = nueva_linea[pos_nueva_comilla+1:]

            linea = parte_inicial_linea + dato + segunda_parte_linea

        return linea

    def procesar_linea_archivo(self, linea, percepciones, anulaciones, gestor_clientes):
        datos = self.limpiar_linea(linea)
        datos = datos.split(";")

        if datos[self.REGIMEN] == REGIMEN_LHE:
            return # Filtrar la linea
        elif datos[self.ABREVIADO] == ABREVIADO_FACTURA:
            self.agregar_percepcion(datos, percepciones)
        elif ABREVIADO_NOTA_DE_CREDITO in datos[self.ABREVIADO]:
            self.agregar_anulacion(datos, anulaciones)
        else:
            imprimir_error("El valor del campo abreviado no corresponde a factura ni a nota de crédito", datos)

        gestor_clientes.buscar_o_crear_cliente_actual(datos[self.NRO_DOC1], datos[self.NOMBRE])

    def cargar_datos_proveedor_bas(self, nombre_archivo, percepciones, anulaciones, gestor_clientes):
        with open(nombre_archivo, "r", encoding="latin1") as f_datos_percepciones:
            primera_linea = True
            for linea in f_datos_percepciones:
                if primera_linea:
                    primera_linea = False
                    continue
                self.procesar_linea_archivo(linea, percepciones, anulaciones, gestor_clientes)
