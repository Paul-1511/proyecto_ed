import numpy as np

def sistema1(t, U):
    """
    Sistema de EDs:
    dx/dt = 3x + 4y
    dy/dt = -4x + 3y
    """
    x, y = U
    dx_dt = 3 * x + 4 * y
    dy_dt = -4 * x + 3 * y
    return np.array([dx_dt, dy_dt])

def sistema2(t, U):
    """
    Sistema de EDs (oscilador armónico):
    dx/dt = y
    dy/dt = -x
    """
    x, y = U
    dx_dt = y
    dy_dt = -x
    return np.array([dx_dt, dy_dt])
