def euler(f, x0, y0, h, xf):
    """
    Método de Euler para resolver ED de primer orden.
    
    Parámetros:
    f  : función f(x, y)
    x0 : valor inicial de x
    y0 : valor inicial de y
    h  : tamaño de paso
    xf : valor final de x

    Retorna:
    x_vals, y_vals: listas con los valores de x e y
    """
    x_vals = [x0]
    y_vals = [y0]

    while x_vals[-1] < xf:
        x = x_vals[-1]
        y = y_vals[-1]
        x_next = x + h
        y_next = y + h * f(x, y)
        x_vals.append(x_next)
        y_vals.append(y_next)

    return x_vals, y_vals
