import os
import shutil

# Ruta del directorio raíz del proyecto (ajusta si es necesario)
proyecto_dir = os.path.abspath(os.path.dirname(__file__))

# Nombres de carpetas a eliminar
carpetas_a_borrar = ['__pycache__', 'env', 'venv', '.venv', '.vscode']

# Extensiones de archivos a eliminar
extensiones_a_borrar = ['.pyc', '.pyo', '.log', '.sqlite3']

def limpiar_directorio(raiz):
    for carpeta_actual, subcarpetas, archivos in os.walk(raiz, topdown=False):
        # Eliminar carpetas innecesarias
        for subcarpeta in subcarpetas:
            if subcarpeta in carpetas_a_borrar:
                ruta_completa = os.path.join(carpeta_actual, subcarpeta)
                try:
                    shutil.rmtree(ruta_completa)
                    print(f'🗑️ Carpeta eliminada: {ruta_completa}')
                except Exception as e:
                    print(f'❌ Error al eliminar carpeta {ruta_completa}: {e}')

        # Eliminar archivos con extensiones no deseadas
        for archivo in archivos:
            if any(archivo.endswith(ext) for ext in extensiones_a_borrar):
                ruta_archivo = os.path.join(carpeta_actual, archivo)
                try:
                    os.remove(ruta_archivo)
                    print(f'🗑️ Archivo eliminado: {ruta_archivo}')
                except Exception as e:
                    print(f'❌ Error al eliminar archivo {ruta_archivo}: {e}')

if __name__ == '__main__':
    print(f'🧼 Limpiando proyecto en: {proyecto_dir}\n')
    limpiar_directorio(proyecto_dir)
    print('\n✅ Limpieza completada.')
