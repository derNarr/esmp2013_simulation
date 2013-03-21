#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# simulate.py
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
# created 2013-03-18 KS
# last mod 2013-03-21 21:15 KS

"""
Simulate a 3D Ising decision model (IDM).

Todo
----
* calculate ground state

"""

from __future__ import division

import functools
import math
import random

import numpy as np
import matplotlib.pyplot as plt

import free_energy
from helper import plot_scatter, plot2

def initiate_deriv_free_energy():
    """
    Defining specific free energy functions...

    Returns
    -------
    Returns function that accepts ys and beta and returns the evaluation of the
    first partial derivatives.

    """
    param = {"Wplus1": 52000,
         "Wplus2": 52000,
         "Wplus3": 52000,
         "Wminus12": 12000,
         "Wminus13": 12000,
         "Wminus23": 12000,
         # Bs are substituted in the function
         #"B1": 0, # 8000
         #"B2": 0,
         #"B3": 0,
         "THETA1": 52500,
         "THETA2": 52500,
         "THETA3": 52500,
         "N1": 1000,
         "N2": 1000,
         "N3": 1000,
         "beta": 1/24}
    derivs = [func.subs(param) for func in free_energy.deriv_free_energy]
    print derivs
    def deriv_free_energy(ys, beta, Bs=(0, 0, 0)):
        """
        .. warning:
            only works if len(ys) is 3

        """
        B1, B2, B3 = Bs
        y1, y2, y3 = ys
        ans = [deriv.subs({"y1": y1, "y2": y2, "y3": y3, "beta": beta, "B1":
                           B1, "B2": B2, "B3": B3}) for
               deriv in derivs]
        print ans
        return np.array(ans)

    return deriv_free_energy

def drift_rate(y, deriv_free_energy, beta, D, Bs):
    r"""
    is in the direction of the vector of attraction.

    ..math:
        -\beta D \frac{\partial F(y)}{\partial y}

    Parameters
    ----------
    y : position
    deriv_free_energy : function
        function that takes the position and returns a vector with.
        (dF/dy_1, dF/dy_2, dF/dy_3...)

    """
    return -beta * D * deriv_free_energy(y, beta, Bs)


def simulate(y_start, t_begin=0.0, t_end=0.002, dt=.0001, Bs=(8000, 8000,
    8200), string_this_B="B", stop=True):
    """
    simulates y_start for a given time interval.

    Parameters
    ----------
    y_start : np.array
        the starting point
    t_begin : float
    t_end : float
    dt : float
        time step size

    Returns
    -------
    (res, ys) : (list, np.array)
        the res list contains pairs of (response, reaction time) and the ys array has shape (Nt, 3)

    """
    # time drift parameters
    #dt=.00001
    t = np.arange(t_begin, t_end, dt)
    Nt = t.size
    #theta=1
    #mu=1.2
    sigma = 0.10
    dt2 = 0.01
    D = 2*sigma**2/dt2

    dfe = initiate_deriv_free_energy()
    drate1 = functools.partial(drift_rate, deriv_free_energy=dfe, beta=1/24, D=D, Bs=Bs)
    sqrtdt = math.sqrt(dt2)
    y = np.zeros((Nt, 3))

    y[0] = np.array(y_start)
    res = False
    for i in xrange(1,Nt):
        if y[i-1][0] <= 0:
            print "WARNING y gets below zero"
            y[i-1][0] = 0.0001
        if y[i-1][0] >= 1:
            print "WARNING y gets above one"
            y[i-1][0] = 0.9999
        if y[i-1][1] < 0:
            print "WARNING y gets below zero"
            y[i-1][1] = 0.0001
        if y[i-1][1] >= 1:
            print "WARNING y gets above one"
            y[i-1][1] = 0.9999
        if y[i-1][2] < 0:
            print "WARNING y gets below zero"
            y[i-1][2] = 0.0001
        if y[i-1][2] >= 1:
            print "WARNING y gets above one"
            y[i-1][2] = 0.9999
        y[i] = (y[i-1] + dt*drate1(y[i-1]) +
                sigma*sqrtdt*np.array((random.gauss(0,1),
                                    random.gauss(0,1),
                                    random.gauss(0,1))))
        if y[i][0] < 0.3 and y[i][1] < 0.3 and y[i][2] > 0.7:
            if not res:
                res = ("plus", string_this_B, i)
            if stop:
                break
        if y[i][0] < 0.3 and y[i][1] > 0.7 and y[i][2] < 0.3:
            if not res:
                res = ("equal", string_this_B, i)
            if stop:
                break
        if y[i][0] > 0.7 and y[i][1] < 0.3 and y[i][2] < 0.3:
            if not res:
                res = ("minus", string_this_B, i)
            if stop:
                break
    return (res, y)

if __name__ == "__main__":
    n = 2j
    #y1, y2, y3 = np.mgrid[0.1:0.9:n, 0.1:0.9:n, 0.1:0.9:n]
    y1, y2, y3 = np.mgrid[0.15:0.17:n, 0.15:0.17:n, 0.15:0.17:n]
    starting_yy1 = y1.flatten()
    starting_yy2 = y2.flatten()
    starting_yy3 = y3.flatten()
    final_y = list()
    responses = list()
    for i in range(len(starting_yy1)):
        res, y = simulate((starting_yy1[i], starting_yy2[i], starting_yy3[i]),
                     t_begin=0.0, t_end=0.02, dt=.0001, stop=False)
        final_y.append(y)
        responses.append(res)
    final_y = np.array(final_y)
    end_points = np.array([y[-1] for y in final_y])
    print("Endpoints in the plot.")
    plot_scatter(end_points)

    print("last 25 points in the plot")
    fig = plt.figure()
    for y in final_y:
        plot2(y[-25:], fig)
    plt.show()

    print("traces in the plot")
    fig = plt.figure()
    for y in final_y:
        plot2(y, fig)
    plt.show()

