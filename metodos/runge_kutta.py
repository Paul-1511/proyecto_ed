def runge_kutta_4(f, x0, y0, h, xf):
    """
    Método de Runge-Kutta de cuarto orden (RK4) para ED de primer orden.

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
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h * k1 / 2)
        k3 = f(x + h / 2, y + h * k2 / 2)
        k4 = f(x + h, y + h * k3)
        x_next = x + h
        y_next = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x_vals.append(x_next)
        y_vals.append(y_next)

    return x_vals, y_vals
