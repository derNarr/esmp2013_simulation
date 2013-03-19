#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# free_energy.py
#
# (c) 2013 Konstantin Sering <konstantin.sering [aet] gmail.com>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content:
#
# input: --
# output: --
#
# created 2013-03-19 KS
# last mod 2013-03-19 15:29 KS

"""
Defining and providing the free energy function and its derivatives.

"""

import sympy

def create_free_energy():
    """
    Defining the symbolic free energy function for a three dimensional Ising
    model.

    """
    Wplus1, Wplus2, Wplus3  = sympy.symbols("Wplus1, Wplus2, Wplus3")
    Wminus12, Wminus13, Wminus23  = sympy.symbols("Wminus12, Wminus13, Wminus23")
    B1, B2, B3 = sympy.symbols("B1, B2, B3")
    THETA1, THETA2, THETA3 = sympy.symbols("THETA1, THETA2, THETA3")
    beta = sympy.symbols("beta")
    y1, y2, y3 = sympy.symbols("y1, y2, y3")
    N1, N2, N3 = sympy.symbols("N1, N2, N3")

    F_IDM = (-Wplus1*y1**2 - Wplus2*y2**2 - Wplus3*y3**2
            + Wminus12*y1*y2 + Wminus13*y1*y3 + Wminus23*y2*y3
            + (B1 - THETA1)*y1 + (B2 - THETA2)*y2 + (B3 - THETA3)*y3
            + 1/beta * (N1*(y1*sympy.log(y1) + (1-y1)*sympy.log(1-y1))
                        + N2*(y2*sympy.log(y2) + (1-y2)*sympy.log(1-y2))
                        + N3*(y3*sympy.log(y3) + (1-y3)*sympy.log(1-y3))))

    return F_IDM

free_energy = create_free_energy()

deriv_free_energy = (free_energy.diff("y1"),
                     free_energy.diff("y2"),
                     free_energy.diff("y3"))

