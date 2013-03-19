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
# last mod 2013-03-19 17:33 KS

"""

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

def initiate_deriv_free_energy():
    """
    Defining specific free energy functions...

    Returns
    -------
    Returns function that accepts ys and beta and returns the evaluation of the
    first partial derivatives.

    """
    param = {"Wplus1": 1,
             "Wplus2": 1,
             "Wplus3": 1,
             "Wminus12": 1,
             "Wminus13": 1,
             "Wminus23": 1,
             "B1": 1,
             "B2": 1,
             "B3": 1,
             "THETA1": 1,
             "THETA2": 1,
             "THETA3": 1,
             "N1": 1,
             "N2": 1,
             "N3": 1}
    derivs = [func.subs(param) for func in free_energy.deriv_free_energy]
    def deriv_free_energy(ys, beta):
        """
        .. warning:
            only works if len(ys) is 3

        """
        y1, y2, y3 = ys
        ans = [deriv.subs({"y1": y1, "y2": y2, "y3": y3, "beta": beta}) for
               deriv in derivs]
        return np.array(ans)

    return deriv_free_energy

def drift_rate(y, dfe, beta, D):
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
    return -beta * D * dfe(y, beta)


def simulate(y_start, t_begin=0, t_end=2, dt=.1):
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
    ys : np.array
        the ys array has shape (Nt, 3)

    """
    # time drift parameters
    #dt=.00001
    t = np.arange(t_begin, t_end, dt)
    Nt = t.size
    #theta=1
    #mu=1.2
    sigma=0.3

    dfe = initiate_deriv_free_energy()
    drate1 = functools.partial(drift_rate,
            dfe=dfe, beta=1/24, D=1)
    sqrtdt = math.sqrt(dt)
    y = np.zeros((Nt, 3))

    y[0] = np.array(y_start)
    for i in xrange(1,Nt):
        y[i] = (y[i-1] + dt*drate1(y[i-1]) +
                sigma*sqrtdt*np.array((random.gauss(0,1),
                                    random.gauss(0,1),
                                    random.gauss(0,1))))
        # did I cross one of the hyperplanes
        # store response
        # store RT
    return y

y = simulate((0.1, 0.2, 0.3), t_begin=0, t_end=2, dt=.1)

ax = plt.subplot(111)
ax.plot(range(len(y)), y[:,0], "r-")
ax.plot(range(len(y)), y[:,1], "g-")
ax.plot(range(len(y)), y[:,2], "b-")
plt.show()

