import os
import numpy as np
from .graficador import graficar_soluciones, graficar_error

def comparar_soluciones(x_vals, y_numerica, y_analitica, metodo_nombre="", guardar=False):
    """
    Compara la solución numérica y la analítica, mostrando gráficos y métricas.
    
    Parámetros:
    - x_vals: lista de valores de x
    - y_numerica: lista de resultados del método numérico
    - y_analitica: lista o array de solución analítica
    - metodo_nombre: nombre del método numérico
    - guardar: si True, guarda los resultados en archivos
    
    Retorna:
    - dict: diccionario con métricas de error
    """
    x = np.array(x_vals)
    y_num = np.array(y_numerica)
    y_exact = np.array(y_analitica)
    
    error_abs = np.abs(y_exact - y_num)
    error_rel = error_abs / (np.abs(y_exact) + 1e-10)  # Evita división por cero
    error_prom = np.mean(error_abs)
    error_max = np.max(error_abs)
    
    # Mostrar gráficos
    graficar_soluciones(x, y_num, y_exact, metodo_nombre, guardar)
    graficar_error(x, error_abs, metodo_nombre, guardar)
    
    # Mostrar métricas
    print(f"\nMétricas de error para {metodo_nombre}:")
    print(f"Error absoluto medio: {error_prom:.6e}")
    print(f"Error absoluto máximo: {error_max:.6e}")
    print(f"Error relativo máximo: {np.max(error_rel):.6e}")
    
    # Guardar datos numéricos si se solicita
    if guardar:
        if not os.path.exists('resultados'):
            os.makedirs('resultados')
        data_filename = f"resultados/datos_{metodo_nombre.lower().replace(' ', '_')}.csv"
        np.savetxt(data_filename, 
                  np.column_stack([x, y_num, y_exact, error_abs, error_rel]),
                  delimiter=',',
                  header='x,y_numerica,y_analitica,error_absoluto,error_relativo',
                  comments='')
        print(f"Datos numéricos guardados como {data_filename}")
    
    return {
        'error_absoluto_medio': error_prom,
        'error_absoluto_maximo': error_max,
        'error_relativo_maximo': np.max(error_rel)
    }