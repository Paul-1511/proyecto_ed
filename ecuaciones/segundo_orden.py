import numpy as np

def edo2_1(t, Y):
    """
    Sistema equivalente de:
    d²y/dx² + 4dy/dx + 4y = 0
    Se convierte a:
    dy1/dt = y2
    dy2/dt = -4*y2 - 4*y1
    """
    y1, y2 = Y
    dy1_dt = y2
    dy2_dt = -4 * y2 - 4 * y1
    return np.array([dy1_dt, dy2_dt])

def edo2_2(t, Y):
    """
    Sistema equivalente de:
    d²y/dx² = -9y
    Se convierte a:
    dy1/dt = y2
    dy2/dt = -9*y1
    """
    y1, y2 = Y
    dy1_dt = y2
    dy2_dt = -9 * y1
    return np.array([dy1_dt, dy2_dt])
