ENTER = "\n"
SEPARADOR = ","
SEPARADOR_FECHA = "/"

def completar_con_espacios(texto, longitud, espacios_a_derecha=True):
    if len(texto) < longitud:
        espacios = " " * (longitud - len(texto))
        return (texto + espacios) if espacios_a_derecha else (espacios + texto)
    return texto

def convertir_fecha(fecha_texto):
    nueva_fecha = fecha_texto[:2] #dia
    nueva_fecha += SEPARADOR_FECHA
    nueva_fecha += fecha_texto[3:5] #mes
    nueva_fecha += SEPARADOR_FECHA

    year = fecha_texto[6:] #anio
    nueva_fecha += year if len(year) == 4 else ("20" + year)
    return nueva_fecha

def imprimir_error(texto, datos):
    print(texto)
    print("Datos: {}".format(datos))
    input("Presione ENTER para continuar")
