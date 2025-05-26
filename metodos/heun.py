import numpy as np

def heun(f, t0, y0, h, tf):
    """
    Método de Heun (Euler modificado) para:
    - EDOs de primer orden
    - Sistemas de EDOs
    """
    t_vals = np.arange(t0, tf + h, h)
    n = len(t_vals)
    
    if np.isscalar(y0):
        y_vals = np.zeros(n)
        y_vals[0] = y0
        for i in range(n-1):
            k1 = f(t_vals[i], y_vals[i])
            k2 = f(t_vals[i] + h, y_vals[i] + h * k1)
            y_vals[i+1] = y_vals[i] + (h / 2) * (k1 + k2)
    else:
        m = len(y0)
        y_vals = np.zeros((n, m))
        y_vals[0] = y0
        for i in range(n-1):
            k1 = f(t_vals[i], y_vals[i])
            k2 = f(t_vals[i] + h, y_vals[i] + h * k1)
            y_vals[i+1] = y_vals[i] + (h / 2) * (k1 + k2)
    
    return t_vals, y_vals