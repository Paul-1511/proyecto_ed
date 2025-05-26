import numpy as np

def euler(f, t0, y0, h, tf):
    """
    Método de Euler para resolver:
    - EDOs de primer orden (y0 es escalar)
    - Sistemas de EDOs (y0 es array numpy)
    
    Parámetros:
    f  : Función f(t, y)
    t0 : Valor inicial de t
    y0 : Valor(es) inicial(es) (puede ser escalar o array)
    h  : Tamaño de paso
    tf : Valor final de t

    Retorna:
    t_vals: Array de valores de t
    y_vals: Array de soluciones (shape (n,) para EDO, (n,m) para sistema m-dimensional)
    """
    t_vals = np.arange(t0, tf + h, h)
    n = len(t_vals)
    
    if np.isscalar(y0):
        y_vals = np.zeros(n)
        y_vals[0] = y0
        for i in range(n-1):
            y_vals[i+1] = y_vals[i] + h * f(t_vals[i], y_vals[i])
    else:
        m = len(y0)
        y_vals = np.zeros((n, m))
        y_vals[0] = y0
        for i in range(n-1):
            y_vals[i+1] = y_vals[i] + h * f(t_vals[i], y_vals[i])
    
    return t_vals, y_vals