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
# last mod 2013-03-21 11:28 KS

"""
Simulate a 3D Ising decision model (IDM).

Todo
----
* calculate ground state

"""

from __future__ import division

import numpy as np
cimport numpy as np
DTYPE = np.float

#param = {"Wplus1": 52000,
#     "Wplus2": 52000,
#     "Wplus3": 52000,
#     "Wminus12": 12000,
#     "Wminus13": 12000,
#     "Wminus23": 12000,
#     # Bs are substituted in the function
#     #"B1": 0, # 8000
#     #"B2": 0,
#     #"B3": 0,
#     "THETA1": 52500,
#     "THETA2": 52500,
#     "THETA3": 52500,
#     "N1": 1000,
#     "N2": 1000,
#     "N3": 1000,
#     "beta": 1/24}

cdef deriv_free_energy(np.ndarray ys, np.ndarray Bs):
    """
    .. warning:
        only works if len(ys) is 3

    """
    # 1/24 is beta hard coded
    cdef np.float B1 = Bs[0]
    cdef np.float B2 = Bs[1]
    cdef np.float B3 = Bs[2]
    cdef np.float y1 = ys[0]
    cdef np.float y2 = ys[1]
    cdef np.float y3 = ys[2]

    cdef np.float ans1 = (-B1 - 104000.0*y1 + 12000.0*y2 + 12000.0*y3 + 24000.0*np.log(y1) -
            24000.0*np.log(-y1 + 1.0) + 52500.0)
    cdef np.float ans2 = (-B2 + 12000.0*y1 - 104000.0*y2 + 12000.0*y3 + 24000.0*np.log(y2) -
            24000.0*np.log(-y2 + 1.0) + 52500)
    cdef np.float ans3 = (-B3 + 12000.0*y1 + 12000.0*y2 - 104000.0*y3 + 24000.0*np.log(y3) -
            24000.0*np.log(-y3 + 1.0) + 52500.0)
    cdef np.ndarray ans = np.array((ans1, ans2, ans3))
    return ans

cdef drift_rate(np.ndarray y, np.float D, np.ndarray Bs):
    """
    is in the direction of the vector of attraction.

    Parameters
    ----------
    y : position

    """
    # 1/24 is beta hard coded
    return -1./24 * D * deriv_free_energy(y, Bs)


def simulate(y_start, t_begin=0.0, t_end=0.002, dt=.0001, Bs=(8000, 8000, 8200)):
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
    cdef np.ndarray t = np.arange(t_begin, t_end, dt)
    cdef np.float Nt = t.size
    cdef np.float sigma = 0.10
    cdef np.float dt2 = 0.01
    cdef np.float D = 2*sigma**2/dt2

    cdef np.float sqrtdt = np.sqrt(dt2)
    cdef np.ndarray y = np.zeros((Nt, 3))
    res = list()

    y[0] = np.array(y_start)
    for i in xrange(1, Nt):
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
        y[i] = (y[i-1] + dt*drift_rate(y[i-1], D, Bs) +
                sigma*sqrtdt*np.array((np.random.gauss(0,1),
                                    np.random.gauss(0,1),
                                    np.random.gauss(0,1))))
        if y[i][0] < 0.3 and y[i][1] < 0.3 and y[i][2] > 0.7:
            res.append(("plus", i))
            break
        if y[i][0] < 0.3 and y[i][1] > 0.7 and y[i][2] < 0.3:
            res.append(("equal", i))
            break
        if y[i][0] > 0.7 and y[i][1] < 0.3 and y[i][2] < 0.3:
            res.append(("minus", i))
            break
    return res

