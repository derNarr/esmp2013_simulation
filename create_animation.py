#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# create_animation.py
#
# (c) 2012 Konstantin Sering <konstantin.sering [aet] gmail.com>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content:
#
# input: --
# output: --
#
# created 2012-12-23 KS
# last mod 2013-03-21 22:29 KS

from __future__ import division

import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

from helper import plot2

N = 80

ys = np.load("final_y_anim.npy")
ys = np.array([y[1:N] for y in ys])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax.view_init(10, -np.pi)
ax.view_init(20, 215)

print("globals defined")
def set_title(title):
        ax.set_xlim3d((0, 1))
        ax.set_ylim3d((0, 1))
        ax.set_zlim3d((0, 1))
        ax.title.set_text(title)
        ax.set_xlabel('before')
        ax.set_ylabel('equal')
        ax.set_zlabel('after')

def animate(k):
    i = int(k/3)
    if i > 1 and i < ys.shape[1]:
        ax.view_init(20, 215+20*i/N)
        for y in ys:
            y_seg = y[i-1:i+1]
            plot2(y_seg, fig)
        set_title("Decision Space")

def main():
    frames = ys.shape[1]
    anim = animation.FuncAnimation(fig, animate, frames=frames)
    anim.save("animation.mp4", fps=30, codec="mpeg4", bitrate=2000)

if __name__ == "__main__":
    main()

