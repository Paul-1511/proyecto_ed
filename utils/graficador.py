import numpy as np
import matplotlib.pyplot as plt
import os
import re

def sanitize_filename(filename):
    """Convierte un string en un nombre de archivo válido"""
    # Reemplaza caracteres problemáticos con guiones bajos
    filename = re.sub(r'[\\/*?:"<>|\n=]', "_", filename)
    # Reemplaza múltiples espacios o guiones bajos con uno solo
    filename = re.sub(r'[\s_]+', '_', filename)
    return filename.strip('_')

def graficar_soluciones(x_vals, y_numerica, y_analitica, metodo_nombre="", guardar=False):
    """
    Compara la solución numérica y la analítica graficándolas juntas.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_numerica, 'b-', label=f"{metodo_nombre} (numérica)")
    plt.plot(x_vals, y_analitica, 'r--', label="Solución analítica")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Comparación: {metodo_nombre}")
    plt.grid(True)
    plt.legend()
    
    if guardar:
        if not os.path.exists('resultados'):
            os.makedirs('resultados')
        # Sanitizar el nombre del método para el nombre de archivo
        safe_name = sanitize_filename(metodo_nombre)
        filename = f"resultados/comparacion_{safe_name}.png"
        plt.savefig(filename)
        print(f"Gráfica guardada como {filename}")
    
    plt.show()

def graficar_error(x_vals, error, metodo_nombre="", guardar=False):
    """
    Grafica el error absoluto de la solución numérica.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, error, 'g-', label=f"Error absoluto ({metodo_nombre})")
    plt.xlabel("x")
    plt.ylabel("Error absoluto")
    plt.title(f"Error absoluto: {metodo_nombre}")
    plt.grid(True)
    plt.legend()
    
    if guardar:
        if not os.path.exists('resultados'):
            os.makedirs('resultados')
        # Sanitizar el nombre del método para el nombre de archivo
        safe_name = sanitize_filename(metodo_nombre)
        filename = f"resultados/error_{safe_name}.png"
        plt.savefig(filename)
        print(f"Gráfica de error guardada como {filename}")
    
    plt.show()