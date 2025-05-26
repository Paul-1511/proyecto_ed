import numpy as np
import matplotlib.pyplot as plt
from metodos.euler import euler
from metodos.heun import heun
from metodos.runge_kutta import runge_kutta_4
from ecuaciones.primer_orden import f1, f2
from ecuaciones.segundo_orden import edo2_1
from ecuaciones.sistemas import sistema1

def solucion_analitica_f1(t):
    """Solución analítica de dy/dt = t + y, y(0) = 1"""
    return -t - 1 + 2 * np.exp(t)

def probar_edp_primer_orden(nombre_metodo, metodo_func):
    """Prueba los métodos con EDO de primer orden"""
    print(f"\n=== Probando {nombre_metodo} con EDO de primer orden ===")
    t0, y0 = 0, 1
    h = 0.1
    tf = 2

    t_vals, y_numerica = metodo_func(f1, t0, y0, h, tf)
    y_analitica = solucion_analitica_f1(t_vals)

    # Calcular errores
    error_abs = np.abs(y_analitica - y_numerica)
    error_prom = np.mean(error_abs)

    # Gráfico
    plt.figure(figsize=(10, 5))
    plt.plot(t_vals, y_numerica, 'b-', label=f"{nombre_metodo} (numérico)")
    plt.plot(t_vals, y_analitica, 'r--', label="Solución analítica")
    plt.title(f"EDO 1er orden: dy/dt = t + y\nMétodo: {nombre_metodo}")
    plt.xlabel("t")
    plt.ylabel("y(t)")
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"Error medio absoluto: {error_prom:.6f}")
    return error_prom

def probar_sistema(nombre_metodo, metodo_func):
    """Prueba los métodos con sistema 2x2"""
    print(f"\n=== Probando {nombre_metodo} con sistema 2x2 ===")
    t0 = 0
    y0 = np.array([1.0, 0.0])  # x(0)=1, y(0)=0
    h = 0.1
    tf = 5

    t_vals, sol = metodo_func(sistema1, t0, y0, h, tf)
    
    # Gráficos
    plt.figure(figsize=(12, 5))
    
    # Series temporales
    plt.subplot(1, 2, 1)
    plt.plot(t_vals, sol[:, 0], label='x(t)')
    plt.plot(t_vals, sol[:, 1], label='y(t)')
    plt.xlabel('t')
    plt.ylabel('Valores')
    plt.title(f"Sistema - {nombre_metodo}\ndx/dt=3x+4y\ndy/dt=-4x+3y")
    plt.legend()
    plt.grid(True)
    
    # Espacio de fases
    plt.subplot(1, 2, 2)
    plt.plot(sol[:, 0], sol[:, 1])
    plt.xlabel('x(t)')
    plt.ylabel('y(t)')
    plt.title(f"Espacio de fases\n{nombre_metodo}")
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

def probar_edo_segundo_orden(nombre_metodo, metodo_func):
    """Prueba los métodos con EDO de segundo orden"""
    print(f"\n=== Probando {nombre_metodo} con EDO 2do orden ===")
    t0 = 0
    y0 = np.array([1.0, 0.0])  # y(0)=1, y'(0)=0
    h = 0.1
    tf = 5

    t_vals, sol = metodo_func(edo2_1, t0, y0, h, tf)
    
    # Gráficos
    plt.figure(figsize=(12, 5))
    
    # Solución y derivada
    plt.subplot(1, 2, 1)
    plt.plot(t_vals, sol[:, 0], label='y(t)')
    plt.plot(t_vals, sol[:, 1], label="y'(t)")
    plt.xlabel('t')
    plt.ylabel('y')
    plt.title(f"EDO: y'' + 4y' + 4y = 0\nMétodo: {nombre_metodo}")
    plt.legend()
    plt.grid(True)
    
    # Espacio de fases
    plt.subplot(1, 2, 2)
    plt.plot(sol[:, 0], sol[:, 1])
    plt.xlabel('y(t)')
    plt.ylabel("y'(t)")
    plt.title(f"Espacio de fases\n{nombre_metodo}")
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Pruebas para cada método
    metodos = [
        ("Euler", euler),
        ("Heun", heun),
        ("Runge-Kutta 4", runge_kutta_4)
    ]
    
    for nombre, metodo in metodos:
        # Prueba EDO primer orden
        error = probar_edp_primer_orden(nombre, metodo)
        assert error < 0.5 if nombre == "Euler" else 0.1 if nombre == "Heun" else 0.01
        
        # Prueba sistema
        probar_sistema(nombre, metodo)
        
        # Prueba EDO segundo orden
        probar_edo_segundo_orden(nombre, metodo)
    
    print("\n¡Todas las pruebas pasaron exitosamente!")