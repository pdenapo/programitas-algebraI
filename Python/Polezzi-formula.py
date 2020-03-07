#!/usr/bin/env python3

# Programa para calcular el máximo común divisor con la fórmula de Marcelo Polezzi en el articulo
# "A Geometrical Method for Finding an Explicit Formula for the Greatest Common Divisor"
#  The American Mathematical Monthly
# Volume 104, 1997 - Issue 5 - Pages 445-446

# Ejemplo de uso:
# python3 Polezii-formula.py 20 30

# Este programa tiene solamente propósitos didácticos
# (es para mis alumnos de Algebra I).

# (C) 20014-2016  Pablo De Nápoli <pdenapo@dm.uba.ar>

# Este programa es software libre, y usted puede redistribuirlo o
# modificarlo libremente bajo los términos de la
# GNU General Public Licence (Licencia Pública General), versión 3
# o cualquier versión posterior,
# publicada por la Free Software Foundation. Vea:
#
# http://www.gnu.org/copyleft/gpl.html

import argparse
from math import floor


def mcd(m, n):
    return 2 * sum([floor(i * n / m) for i in range(1, m)]) + (m + n) - m * n


parser = argparse.ArgumentParser(
    description='Calcula el máximo común divisor usando la fórmula de Polezzi')
parser.add_argument("m", type=int)
parser.add_argument("n", type=int)
args = parser.parse_args()

print("Calculamos el máximo común divisor entre ", args.m, " y ", args.n)
print("Resultado=", mcd(args.m, args.n))
