from metodos.euler import euler
from metodos.heun import heun
from metodos.runge_kutta import runge_kutta_4
from ecuaciones.primer_orden import f1, f2
from ecuaciones.segundo_orden import edo2_1, edo2_2
from ecuaciones.sistemas import sistema1, sistema2
from utils.comparador import comparar_soluciones
import numpy as np
import os

def solucion_analitica_f1(x):
    """Solución analítica de dy/dx = x + y, y(0) = 1"""
    return -x - 1 + 2 * np.exp(x)

def solucion_analitica_f2(x):
    """Solución analítica de dy/dx = y*cos(x), y(0) = 1"""
    return np.exp(np.sin(x))

def mostrar_menu():
    print("\nProyecto Final - Métodos Numéricos para Ecuaciones Diferenciales")
    print("1. Resolver dy/dx = x + y, y(0) = 1")
    print("2. Resolver dy/dx = y*cos(x), y(0) = 1")
    print("3. Resolver sistema de EDs (oscilador armónico)")
    print("4. Salir")
    return input("Seleccione una opción (1-4): ")

def seleccionar_metodo():
    print("\nSeleccione el método numérico:")
    print("1. Euler")
    print("2. Heun (Euler modificado)")
    print("3. Runge-Kutta de 4to orden")
    opcion = input("Ingrese una opción (1-3): ")
    
    metodos = {
        '1': ("Euler", euler),
        '2': ("Heun", heun),
        '3': ("Runge-Kutta 4", runge_kutta_4)
    }
    
    return metodos.get(opcion, (None, None))

def configurar_parametros():
    print("\nConfiguración de parámetros:")
    x0 = float(input("Valor inicial de x (x0): ") or "0")
    y0 = float(input(f"Valor inicial de y (y0): ") or "1")
    h = float(input("Tamaño de paso (h): ") or "0.1")
    xf = float(input("Valor final de x (xf): ") or "2")
    guardar = input("¿Guardar resultados? (s/n): ").lower() == 's'
    return x0, y0, h, xf, guardar

def resolver_ecuacion(f, sol_analitica, metodo, nombre_metodo, x0, y0, h, xf, guardar):
    print(f"\nResolviendo con método {nombre_metodo}...")
    x_vals, y_numerica = metodo(f, x0, y0, h, xf)
    x_array = np.array(x_vals)
    y_analitica = sol_analitica(x_array)
    return comparar_soluciones(x_array, y_numerica, y_analitica, nombre_metodo, guardar)

def main():
    while True:
        opcion = mostrar_menu()
        
        if opcion == '4':
            print("Saliendo del programa...")
            break
            
        nombre_metodo, metodo = seleccionar_metodo()
        if not metodo:
            print("Opción de método inválida.")
            continue
            
        x0, y0, h, xf, guardar = configurar_parametros()
        
        if opcion == '1':
            resolver_ecuacion(f1, solucion_analitica_f1, metodo, nombre_metodo, x0, y0, h, xf, guardar)
        elif opcion == '2':
            resolver_ecuacion(f2, solucion_analitica_f2, metodo, nombre_metodo, x0, y0, h, xf, guardar)
        elif opcion == '3':
            # Ejemplo para sistema de ecuaciones
            print("\nResolviendo sistema de EDs: dx/dt = y, dy/dt = -x")
            # Aquí iría la lógica para sistemas (puedes expandir esto)
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    # Crear carpeta resultados si no existe
    if not os.path.exists('resultados'):
        os.makedirs('resultados')
    main()