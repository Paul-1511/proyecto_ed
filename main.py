from metodos.euler import euler
from metodos.heun import heun
from metodos.runge_kutta import runge_kutta_4
from ecuaciones.primer_orden import f1, f2
from ecuaciones.segundo_orden import edo2_1, edo2_2
from ecuaciones.sistemas import sistema1, sistema2
from utils.comparador import comparar_soluciones
from utils.analizador import graficar_sistema, graficar_segundo_orden
import numpy as np
import os

# Soluciones analíticas para EDOs de primer orden
def solucion_analitica_f1(x):
    """Solución analítica de dy/dx = x + y, y(0) = 1"""
    return -x - 1 + 2 * np.exp(x)

def solucion_analitica_f2(x):
    """Solución analítica de dy/dx = y*cos(x), y(0) = 1"""
    return np.exp(np.sin(x))

def mostrar_menu_principal():
    print("\n=== PROYECTO DE ECUACIONES DIFERENCIALES ===")
    print("1. EDO de primer orden")
    print("2. EDO de segundo orden")
    print("3. Sistema de EDOs")
    print("4. Salir")
    return input("Seleccione tipo de problema (1-4): ")

def mostrar_menu_edos_primer_orden():
    print("\nEDOs de primer orden disponibles:")
    print("1. dy/dx = x + y, y(0) = 1")
    print("2. dy/dx = y*cos(x), y(0) = 1")
    return input("Seleccione ecuación (1-2): ")

def mostrar_menu_sistemas():
    print("\nSistemas disponibles:")
    print("1. dx/dt = 3x + 4y, dy/dt = -4x + 3y")
    print("2. Oscilador armónico: dx/dt = y, dy/dt = -x")
    return input("Seleccione sistema (1-2): ")

def mostrar_menu_segundo_orden():
    print("\nEDOs de segundo orden disponibles:")
    print("1. d²y/dt² + 4dy/dt + 4y = 0")
    print("2. d²y/dt² = -9y (oscilador simple)")
    return input("Seleccione ecuación (1-2): ")

def seleccionar_metodo():
    print("\nMétodos numéricos disponibles:")
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

def configurar_parametros(es_sistema=False):
    print("\nConfiguración de parámetros:")
    t0 = float(input("Valor inicial de t (t0): ") or "0")
    
    if es_sistema:
        x0 = float(input("Valor inicial para x(0): ") or "1")
        y0 = float(input("Valor inicial para y(0): ") or "0")
        y0 = np.array([x0, y0])
    else:
        y0 = float(input(f"Valor inicial de y (y0): ") or "1")
    
    h = float(input("Tamaño de paso (h): ") or "0.1")
    tf = float(input("Valor final de t (tf): ") or "2")
    guardar = input("¿Guardar resultados? (s/n): ").lower() == 's'
    return t0, y0, h, tf, guardar

def resolver_edp_primer_orden():
    opcion = mostrar_menu_edos_primer_orden()
    if opcion not in ['1', '2']:
        print("Opción inválida")
        return
    
    nombre_metodo, metodo = seleccionar_metodo()
    if not metodo:
        print("Método inválido")
        return
    
    t0, y0, h, tf, guardar = configurar_parametros()
    
    if opcion == '1':
        f = f1
        sol_analitica = solucion_analitica_f1
        titulo = "dy/dx = x + y"
    else:
        f = f2
        sol_analitica = solucion_analitica_f2
        titulo = "dy/dx = y*cos(x)"
    
    t, y = metodo(f, t0, y0, h, tf)
    comparar_soluciones(t, y, sol_analitica(t), f"{titulo}\nMétodo: {nombre_metodo}", guardar)

def resolver_sistema():
    opcion = mostrar_menu_sistemas()
    if opcion not in ['1', '2']:
        print("Opción inválida")
        return
    
    nombre_metodo, metodo = seleccionar_metodo()
    if not metodo:
        print("Método inválido")
        return
    
    t0, y0, h, tf, guardar = configurar_parametros(es_sistema=True)
    
    if opcion == '1':
        f = sistema1
        titulo = "Sistema: dx/dt=3x+4y, dy/dt=-4x+3y"
    else:
        f = sistema2
        titulo = "Oscilador armónico"
    
    t, sol = metodo(f, t0, y0, h, tf)
    graficar_sistema(t, sol, f"{titulo}\nMétodo: {nombre_metodo}")
    
    if guardar:
        np.savetxt(f'resultados/sistema_{opcion}_{nombre_metodo}.csv',
                  np.column_stack([t, sol]),
                  delimiter=',',
                  header='t,x,y',
                  comments='')

def resolver_segundo_orden():
    opcion = mostrar_menu_segundo_orden()
    if opcion not in ['1', '2']:
        print("Opción inválida")
        return
    
    nombre_metodo, metodo = seleccionar_metodo()
    if not metodo:
        print("Método inválido")
        return
    
    t0, y0, h, tf, guardar = configurar_parametros(es_sistema=True)
    
    if opcion == '1':
        f = edo2_1
        titulo = "EDO: y'' + 4y' + 4y = 0"
    else:
        f = edo2_2
        titulo = "EDO: y'' = -9y"
    
    t, sol = metodo(f, t0, y0, h, tf)
    graficar_segundo_orden(t, sol, f"{titulo}\nMétodo: {nombre_metodo}")
    
    if guardar:
        np.savetxt(f'resultados/edo2_{opcion}_{nombre_metodo}.csv',
                  np.column_stack([t, sol]),
                  delimiter=',',
                  header='t,y,y_prime',
                  comments='')

def main():
    # Crear carpeta resultados si no existe
    if not os.path.exists('resultados'):
        os.makedirs('resultados')
    
    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == '1':
            resolver_edp_primer_orden()
        elif opcion == '2':
            resolver_segundo_orden()
        elif opcion == '3':
            resolver_sistema()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()