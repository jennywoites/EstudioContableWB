from utils import ENTER

class GeneradorArchivosPercepciones:
    def generar_archivos(self, nombre_archivo, datos_percepciones):
        if len(datos_percepciones) == 0: #No genera el archivo si no hay datos
            return

        with open(nombre_archivo + ".txt", "w") as arch_txt:
            with open(nombre_archivo + ".csv", "w") as arch_csv:
                for dato_percepcion in datos_percepciones:
                    arch_txt.write(dato_percepcion.get_linea_para_txt() + ENTER)
                    arch_csv.write(dato_percepcion.get_linea_para_csv() + ENTER)