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
# last mod 2013-03-18 23:05 KS

import numpy as np
import matplotlib.pyplot as plt
import math
import random

tBegin=0
tEnd=2
dt=.00001

t = np.arange(tBegin, tEnd, dt)
N = t.size
IC=0
theta=1
mu=1.2
sigma=0.3

# calculate ground state

def drift_rate(y, free_energy):
    pass

def free_energy(y):
    # some important code
    pass

sqrtdt = math.sqrt(dt)
y = np.zeros(N)
y[0] = IC
for i in xrange(1,N):
    y[i] = y[i-1] + dt*drift_rate(y[i], free_energy) + sigma*sqrtdt*random.gauss(0,1)
    # did I cross one of the hyperplanes
    # store response
    # store RT

ax = plt.subplot(111)
ax.plot(t,y)
plt.show()
