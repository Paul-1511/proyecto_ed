import matplotlib.pyplot as plt
import numpy as np

def graficar_sistema(t, Y, titulo=""):
    """Visualiza solución de sistema 2x2"""
    plt.figure(figsize=(12, 5))
    
    # Gráfico de series temporales
    plt.subplot(1, 2, 1)
    plt.plot(t, Y[:, 0], label='x(t)')
    plt.plot(t, Y[:, 1], label='y(t)')
    plt.xlabel('Tiempo (t)')
    plt.ylabel('Variables')
    plt.title(f"Series temporales\n{titulo}")
    plt.legend()
    plt.grid(True)
    
    # Espacio de fases
    plt.subplot(1, 2, 2)
    plt.plot(Y[:, 0], Y[:, 1])
    plt.xlabel('x(t)')
    plt.ylabel('y(t)')
    plt.title(f"Espacio de fases\n{titulo}")
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

def graficar_segundo_orden(t, Y, titulo=""):
    """Visualiza EDO de segundo orden convertida a sistema"""
    plt.figure(figsize=(12, 5))
    
    # Solución y derivada
    plt.subplot(1, 2, 1)
    plt.plot(t, Y[:, 0], label='y(t)')
    plt.plot(t, Y[:, 1], label="y'(t)")
    plt.xlabel('Tiempo (t)')
    plt.ylabel('y')
    plt.title(f"Solución\n{titulo}")
    plt.legend()
    plt.grid(True)
    
    # Espacio de fases
    plt.subplot(1, 2, 2)
    plt.plot(Y[:, 0], Y[:, 1])
    plt.xlabel('y(t)')
    plt.ylabel("y'(t)")
    plt.title(f"Espacio de fases\n{titulo}")
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()