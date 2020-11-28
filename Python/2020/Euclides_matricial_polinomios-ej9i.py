#!/usr/bin/env python3

# Programa en Python 3 que calcula el máximo común divisor
# usando la versión matricial del algoritmo de Euclides, y los coeficientes que permiten
# escribirlo como combinación lineal
# según el artículo de Antonio Cafure
# "El algoritmo de Euclides y la Noción de divisor común máximo"

# versión para polinomios usando Sagemath

# Este programa tiene solamente propósitos didácticos
# (es para mis alumnos de Algebra I).

# (C) 20014-2020  Pablo De Nápoli <pdenapo@dm.uba.ar>

# Este programa es software libre, y usted puede redistribuirlo o
# modificarlo libremente bajo los términos de la
# GNU General Public Licence (Licencia Pública General), versión 3
# o cualquier versión posterior,
# publicada por la Free Software Foundation. Vea:
#
# http://www.gnu.org/copyleft/gpl.html

import argparse
import sys
import numpy as np
from math import gcd

# Función para dividir polinomios en Sagemath
# https://ask.sagemath.org/question/9974/polynomial-division-command/


def chequea_invariante(a, b, m):
    if not (a * m[0, 0] + b * m[0, 1] == m[0, 2]):
        sys.exit("¡La primera ecuación no se cumple!")
    if not (a * m[0, 0] + b * m[0, 1] == m[0, 2]):
        sys.exit("¡La segunda ecuación no se cumple!")
    if not (a.gcd(b) == m[0, 2].gcd(m[1, 2])):
        sys.exit("El máximo común divisor no se preserva")


def Euclides_matricial_con_polinomios(a, b):
    paso = 0
    # El anillo donde vamos a trabajar
    R = PolynomialRing(QQ, 'x')
    # convertimos a y b a objetos en ese anillo
    a = R(a)
    b = R(b)
    m = matrix([[1, 0, a], [0, 1, b]])
    while True:
        print("paso ", paso)
        paso = paso + 1
        print(m)
        if m[0, 2] == 0:
            # Si se llega a un cero, el algoritmo termina y devuelve el mcd y los coeficientes de la
            # combinación lineal
            mcd_a_b = m[1, 2]
            s_a_b = m[1, 0]
            t_a_b = m[1, 1]
            break
        elif m[1, 2] == 0:
            mcd_a_b = m[0, 2]
            s_a_b = m[0, 0]
            t_a_b = m[0, 1]
            break
        elif m[0, 2] >= m[1, 2]:
            q, r = m[0, 2].quo_rem(m[1, 2])
            # Restamos a la primer fila q veces la segunda
            m[0, 0] = m[0, 0] - q * m[1, 0]
            m[0, 1] = m[0, 1] - q * m[1, 1]
            m[0, 2] = r
        else:
            q, r = m[1, 2].quo_rem(m[0, 2])
            # Restamos a la segunda fila q veces la primera
            m[1, 0] = m[1, 0] - q * m[0, 0]
            m[1, 1] = m[1, 1] - q * m[0, 1]
            m[1, 2] = r
        chequea_invariante(a, b, m)
    return (s_a_b, t_a_b, mcd_a_b)


f = x**5 + x**3 - 6 * x**2 + 2 * x + 2
g = x**4 - x**3 - x**2 + 1
Euclides_matricial_con_polinomios(f, g)
