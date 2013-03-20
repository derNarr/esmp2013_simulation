#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

from simulate import simulate
from helper import plot_scatter, plot2

if __name__ == "__main__":
    
    n = 6j
    y1, y2, y3 = np.mgrid[0.14:0.16:n, 0.14:0.16:n, 0.14:0.16:n]
    starting_yy1 = y1.flatten()
    starting_yy2 = y2.flatten()
    starting_yy3 = y3.flatten()
    #plot_scatter(final_y)
    
    Bs_to_simulate = {
        "minus_5" : (8200, 7900, 7900),
        "minus_4" : (8160, 7920, 7920),
        "minus_3" : (8120, 7940, 7940),
        "minus_2" : (8080, 7960, 7960),
        "minus_1" : (8040, 7980, 7980),
        
        "same_2-" : (8000, 8100, 7900),
        "same_1-" : (7950, 8150, 7900),
        "same_0" :  (7900, 8200, 7900),
        "same_1+" : (7900, 8150, 7950),
        "same_2+" : (7900, 8100, 8000),
        
        "plus_1" : (7980, 7980, 8040),
        "plus_2" : (7960, 7960, 8080),
        "plus_3" : (7940, 7940, 8120),
        "plus_4" : (7920, 7920, 8160),
        "plus_5" : (7900, 7900, 8200),
        }
    
    final_y = list()
    responses = list()
    for these_Bs in Bs_to_simulate:
        Bs = Bs_to_simulate[these_Bs]
        
        for i in range(len(starting_yy1)):
            res, y = simulate((starting_yy1[i], starting_yy2[i], starting_yy3[i]), t_begin=0.0, t_end=0.02, dt=.0001, Bs=Bs)
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
