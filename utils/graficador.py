import numpy as np
import matplotlib.pyplot as plt
import os

def graficar_soluciones(x_vals, y_numerica, y_analitica, metodo_nombre="", guardar=False):
    """
    Compara la solución numérica y la analítica graficándolas juntas.
    
    Parámetros:
    - x_vals: lista de valores de x
    - y_numerica: lista de resultados del método numérico
    - y_analitica: lista o array de solución analítica
    - metodo_nombre: nombre del método numérico
    - guardar: si True, guarda la gráfica en resultados/
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
        filename = f"resultados/comparacion_{metodo_nombre.lower().replace(' ', '_')}.png"
        plt.savefig(filename)
        print(f"Gráfica guardada como {filename}")
    
    plt.show()

def graficar_error(x_vals, error, metodo_nombre="", guardar=False):
    """
    Grafica el error absoluto de la solución numérica.
    
    Parámetros:
    - x_vals: lista de valores de x
    - error: lista de errores absolutos
    - metodo_nombre: nombre del método numérico
    - guardar: si True, guarda la gráfica en resultados/
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
        filename = f"resultados/error_{metodo_nombre.lower().replace(' ', '_')}.png"
        plt.savefig(filename)
        print(f"Gráfica de error guardada como {filename}")
    
    plt.show()