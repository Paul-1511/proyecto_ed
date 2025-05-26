import numpy as np

def f1(x, y):
    """
    ED de primer orden:
    dy/dx = x + y
    """
    return x + y

def f2(x, y):
    """
    ED de primer orden:
    dy/dx = y * cos(x)
    """
    return y * np.cos(x)
