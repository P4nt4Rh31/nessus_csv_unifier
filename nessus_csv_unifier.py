
""" 
Nessus CSV Unifier

This Python script, called Nessus CSV Unifier, was created by Arturo Correa "P4nth4_R31" and aims to consolidate multiple CSV files generated by the Nessus vulnerability scanning tool into a single unified file. In the context of a pentesting process, it is common to generate multiple vulnerability reports in CSV format using Nessus. Managing these multiple files can be tedious and error-prone, especially when you want to have a unified view of all vulnerabilities detected in different segments of the network or during different periods of time. Nessus CSV Unifier automates this consolidation process, allowing security analysts to save time and reduce the risk of human error. The script reads CSV files, handles errors, consolidates data into a single DataFrame, maintains an activity log, and exports the consolidated data into a new CSV file. To use this script, place all the CSV files in the same directory as the script and run it in your Python environment.

Execution Example: python csv_unifier.py

Requirements: Python 3.x, pandas library

Installing Pandas: You can install the pandas library using pip: pip install pandas

-------------------------------------------------------------------------------------------------------------------

UnNessus CSV Unifier

Este script de Python, llamado Nessus CSV Unifier, fue creado por Arturo Correa "P4nth4_R31" y tiene como objetivo consolidar múltiples archivos CSV generados por la herramienta de escaneo de vulnerabilidades de Nessus en un solo archivo unificado. En el contexto de un proceso de pentesting, es común generar múltiples informes de vulnerabilidad en formato CSV usando Nessus. Administrar estos múltiples archivos puede ser tedioso y propenso a errores, especialmente cuando desea tener una vista unificada de todas las vulnerabilidades detectadas en diferentes segmentos de la red o durante diferentes períodos de tiempo. Nessus CSV Unifier automatiza este proceso de consolidación, lo que permite a los analistas de seguridad ahorrar tiempo y reducir el riesgo de error humano. El script lee archivos CSV, maneja errores, consolida datos en un único DataFrame, mantiene un registro de actividad y exporta los datos consolidados a un nuevo archivo CSV. Para utilizar este script, coloque todos los archivos CSV en el mismo directorio que el script y ejecútelo en su entorno Python.

Ejemplo de ejecución: python csv_unifier.py

Requisitos: Python 3.x, biblioteca pandas

Instalación de Pandas: Puede instalar la biblioteca de pandas usando pip: pip install pandas

"""

import pandas as pd
import os
import logging

# Configuración del registro
logging.basicConfig(filename='consolidation_log.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# Directorio donde están tus archivos CSV
tuvan_dir = './'  # Directorio actual
elements_of_life = 'consolidated_file.csv'

# Lista para almacenar los DataFrames
airwaves = []

# Iterar sobre los archivos en el directorio
for sandstorm in os.listdir(tuvan_dir):
    if sandstorm.endswith('.csv'):
        communication = os.path.join(tuvan_dir, sandstorm)
        try:
            adagio_for_strings = pd.read_csv(communication)
            airwaves.append(adagio_for_strings)
            logging.info(f'Archivo leído exitosamente: {sandstorm}')
        except Exception as e:
            logging.error(f'Error al leer el archivo {sandstorm}: {e}')

# Verificar si se leyeron archivos
if not airwaves:
    logging.error('No se encontraron archivos CSV válidos en el directorio especificado.')
    raise FileNotFoundError('No se encontraron archivos CSV válidos en el directorio especificado.')

# Concatenar todos los DataFrames
try:
    sunrise = pd.concat(airwaves, ignore_index=True, sort=False)
    logging.info('Archivos concatenados exitosamente.')
except Exception as e:
    logging.error(f'Error al concatenar los archivos: {e}')
    raise e

# Guardar el DataFrame consolidado en un nuevo archivo CSV
try:
    sunrise.to_csv(elements_of_life, index=False)
    logging.info(f'Archivo consolidado guardado en {elements_of_life}')
except Exception as e:
    logging.error(f'Error al guardar el archivo consolidado: {e}')
    raise e

print(f"Archivos consolidados en {elements_of_life}")
