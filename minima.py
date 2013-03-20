#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# minima.py
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
# last mod 2013-03-20 09:10 KS

"""
Script to calculate minima on the free energy hyperplane with some
deterministic fast algorithms.

"""

from __future__ import division

from scipy import optimize
import numpy as np
import sympy

from free_energy import free_energy
from helper import plot_scatter


param = {"Wplus1": 52000,
         "Wplus2": 52000,
         "Wplus3": 52000,
         "Wminus12": 12000,
         "Wminus13": 12000,
         "Wminus23": 12000,
         "B1": 8000, # 8000
         "B2": 8000,
         "B3": 8000,
         "THETA1": 52500,
         "THETA2": 52500,
         "THETA3": 52500,
         "N1": 1000,
         "N2": 1000,
         "N3": 1000,
         "beta": 1/24}

free_energy = free_energy.subs(param)


sympy.pprint(free_energy)

def fe(y):
    res = free_energy.subs({"y1": y[0], "y2": y[1], "y3": y[2]})
    if isinstance(res, sympy.Basic):
        #print y
        #raise "evaluation returns formula not a number"
        #print "evaluation returns formula not a number"
        #print y
        #print res
        try:
            res = float(res)
        except:
            res = np.nan
    if res == np.nan:
        print "NaN"
    return res

n = 4j
y1, y2, y3 = np.mgrid[0.1:0.9:n, 0.1:0.9:n, 0.1:0.9:n]
starting_yy1 = y1.flatten()
starting_yy2 = y2.flatten()
starting_yy3 = y3.flatten()

starting_values = np.array([(starting_yy1[i], starting_yy2[i], starting_yy3[i]) for i in
                   range(len(starting_yy1))])

bounds = ((0.0001, 0.9999), (0.0001, 0.9999), (0.0001, 0.9999))

x = list()
results = list()
for starting in starting_values:
    res = optimize.minimize(fe, starting, method='L-BFGS-B', bounds=bounds)
    x.append(res["x"])
    results.append(res)

yy = np.array(x)
print("\n\nPlot is ready!")
plot_scatter(yy)

