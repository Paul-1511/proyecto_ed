# Proyecto Final - Ecuaciones Diferenciales I
**Simulación Numérica de Ecuaciones Diferenciales Ordinarias**

Autor: Pablo Méndez, José Chavarria 

Curso: Ecuaciones Diferenciales I  

Ciclo: Primer ciclo 2025  

---

## Descripción

Este proyecto tiene como objetivo implementar y comparar diferentes **métodos numéricos** para resolver ecuaciones diferenciales ordinarias (EDOs) de primer orden, segundo orden y sistemas 2x2.

Se ha elegido la **Alternativa 2** del proyecto final, que consiste en desarrollar simulaciones computacionales utilizando tres métodos iterativos: **Euler**, **Heun (Euler modificado)** y **Runge-Kutta de 4to orden (RK4)**, todos programados en **Python**.

---

## Estructura del proyecto

```bash
proyecto_ed/
│
├── main.py                 # Script principal para correr simulaciones
├── metodos/                # Métodos numéricos
│   ├── euler.py
│   ├── heun.py
│   └── runge_kutta.py
│
├── ecuaciones/             # Ecuaciones diferenciales a resolver
│   ├── primer_orden.py
│   ├── segundo_orden.py
│   └── sistemas.py
│
├── utils/                  # Utilidades para graficar y comparar
│   ├── graficador.py
│   └── comparador.py
│
├── pruebas/                # Pruebas y validación
│   └── test_metodos.py
│
├── resultados/             # Gráficas y archivos generados
│
└── README.md               # Este archivo
```

## Métodos implementados
- Euler
- Heun (Euler modificado)
- Runge-Kutta de 4to orden (RK4)
Cada método puede resolver:
- EDOs de primer orden
- EDOs de segundo orden
- Sistemas 2x2

## Ejecución del proyecto
Clona este repositorio
``` bash
git clone https://github.com/Paul-1511/proyecto_ed.git
```

Instala las librerias y dependencias necesarias
``` bash
pip install numpy matplotlib
```

Para ejecutar el proyecto principal
``` bash
python main.py
```

Para ejectuar las pruebas
``` bash
python pruebas/test_metodos.py
```

## Resultados

Las gráficas se guardarán en la carpeta `resultados/` al ejecutar el programa. Se comparan soluciones numéricas contra la solución analítica cuando está disponible

## Objetivo de aprendizaje
Este proyecto busca reforzar los siguientes temas:

-Implementación práctica de métodos numéricos iterativos.
-Comparación de precisión y error entre distintos algoritmos.
-Relación entre soluciones analíticas y numéricas.

## Referencias 

-Boyce, W. E., & DiPrima, R. C. (2017). Ecuaciones diferenciales y problemas con valores en la frontera. Wiley.
-Burden, R. L., & Faires, J. D. (2010). Análisis numérico. Cengage Learning.
