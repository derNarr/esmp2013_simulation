#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# helper.py
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
# created 2013-03-20 KS
# last mod 2013-03-22 09:43 KS

"""
Helper functions mostly for convenience.

"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot(ys):
    """
    make a nice 3D plot for ys as a line.

    """
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(ys[:,0], ys[:,1], ys[:,2])
    ax.set_xlim3d(0, 1)
    ax.set_ylim3d(0, 1)
    ax.set_zlim3d(0, 1)
    plt.show()

def plot2(ys, fig, c="b"):
    """
    make a nice 3D plot for ys as a line.

    """
    ax = fig.gca(projection='3d')
    ax.plot(ys[:,0], ys[:,1], ys[:,2], c=c)
    ax.set_xlim3d(0, 1)
    ax.set_ylim3d(0, 1)
    ax.set_zlim3d(0, 1)


def plot_scatter(ys):
    """
    make a nice 3D plot for ys as a scatter plot.

    """
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.scatter(ys[:,0], ys[:,1], ys[:,2])
    ax.set_xlim3d(0, 1)
    ax.set_ylim3d(0, 1)
    ax.set_zlim3d(0, 1)
    plt.show()


def simpleaxis(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

def spine_shift(ax, shift = 10):
    for loc, spine in ax.spines.iteritems():
        if loc in ['left','bottom']:
            spine.set_position(('outward', shift)) # outward by 10 points
        elif loc in ['right','top']:
            spine.set_color('none') # don't draw spine
        else:
            raise ValueError('unknown spine location: %s'%loc)
