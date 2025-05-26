import numpy as np
import matplotlib.pyplot as plt

from metodos.euler import euler
from metodos.heun import heun
from metodos.runge_kutta import runge_kutta_4
from ecuaciones.primer_orden import f1

def solucion_analitica(x):
    """
    Solución analítica de la ED:
    dy/dx = x + y, y(0) = 1
    La solución es: y(x) = -x - 1 + 2e^x
    """
    return -x - 1 + 2 * np.exp(x)

def probar_metodo(nombre_metodo, metodo_func):
    x0, y0 = 0, 1
    h = 0.1
    xf = 2

    x_vals, y_numerica = metodo_func(f1, x0, y0, h, xf)
    x_array = np.array(x_vals)
    y_analitica = solucion_analitica(x_array)

    # Calcular error absoluto medio
    error = np.abs(y_analitica - np.array(y_numerica))
    error_prom = np.mean(error)

    # Mostrar gráfico comparativo
    plt.plot(x_vals, y_numerica, label=f"{nombre_metodo} (numérico)")
    plt.plot(x_vals, y_analitica, '--', label="Solución analítica")
    plt.title(f"Comparación: {nombre_metodo}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"Error medio absoluto con {nombre_metodo}: {error_prom:.6f}")

if __name__ == "__main__":
    probar_metodo("Euler", euler)
    probar_metodo("Heun", heun)
    probar_metodo("Runge-Kutta 4", runge_kutta_4)
