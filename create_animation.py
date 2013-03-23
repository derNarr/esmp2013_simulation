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
# last mod 2013-03-22 17:37 KS

from __future__ import division

import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
import matplotlib.cm as cm

from helper import plot2

N = 120

ys = np.load("final_y_anim.npy")
ys = np.array([y[0:N] for y in ys])

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
        ax.set_xlabel('Audio first')
        ax.set_ylabel('Synchronous')
        ax.set_zlabel('Video first')

ANGLE1 = 60
ANGLE2 = 360

def animate(k):
    i = int(k/3)
    if k == 1:
        ax.view_init(20, 215)
        for j, y in enumerate(ys):
            y_seg = y[0:2]
            plot2(y_seg, fig, cm.spectral(j/len(ys)))
        ax.scatter(0.16, 0.16, 0.16, c="g", alpha=0.4, s=500)
        ax.scatter(0.82, 0.17, 0.17, c="b", alpha=0.4, s=500)
        ax.scatter(0.17, 0.82, 0.17, c="r", alpha=0.4, s=500)
        ax.scatter(0.17, 0.17, 0.82, c="k", alpha=0.4, s=500)
        set_title("Decision Space")
    if i > 0 and i < N:# ys.shape[1]:
        ax.view_init(20, 215+ANGLE1*k/N/3)
        for j, y in enumerate(ys):
            y_seg = y[i-1:i+1]
            plot2(y_seg, fig, cm.spectral(j/len(ys)))
        set_title("Decision Space")
    elif i >= N:# ys.shape[1]:
        ax.set_axis_off()
        j = k - 3*N
        print "rotate" + str(j)
        ax.view_init(20, (215+ANGLE1+ANGLE2*3*j/int(ANGLE2))%360)

def main():
    frames = int(ANGLE2/3) + 3*N # + ys.shape[1]
    print frames
    anim = animation.FuncAnimation(fig, animate, frames=frames)
    anim.save("animation.mp4", fps=20, codec="mpeg4", bitrate=2000)

if __name__ == "__main__":
    main()

