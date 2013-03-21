#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import time

#import matplotlib.pyplot as plt
import numpy as np

from simulate_c import simulate
#from helper import plot_scatter, plot2

if __name__ == "__main__":

    n = 6j
    y1, y2, y3 = np.mgrid[0.14:0.16:n, 0.14:0.16:n, 0.14:0.16:n]
    starting_yy1 = y1.flatten()
    starting_yy2 = y2.flatten()
    starting_yy3 = y3.flatten()
    #plot_scatter(final_y)

    Bs_to_simulate = (
        ("minus_5", (8200, 7900, 7900)),
        ("minus_4", (8160, 7920, 7920)),
        ("minus_3", (8120, 7940, 7940)),
        ("minus_2", (8080, 7960, 7960)),
        ("minus_1", (8040, 7980, 7980)),

        ("equal_2-", (8000, 8100, 7900)),
        ("equal_1-", (7950, 8150, 7900)),
        ("equal_0",  (7900, 8200, 7900)),
        ("equal_1+", (7900, 8150, 7950)),
        ("equal_2+", (7900, 8100, 8000)),

        ("plus_1", (7980, 7980, 8040)),
        ("plus_2", (7960, 7960, 8080)),
        ("plus_3", (7940, 7940, 8120)),
        ("plus_4", (7920, 7920, 8160)),
        ("plus_5", (7900, 7900, 8200)),
        )

    responses = list()
    for these_Bs, Bs in Bs_to_simulate:
        for i in range(len(starting_yy1)):
            answer, reaction_time = simulate((starting_yy1[i], starting_yy2[i], starting_yy3[i]),
                           t_begin=0.0, t_end=0.10, dt=.0001, Bs=Bs)
            res = (answer, these_Bs, reaction_time)
            print res
            responses.append(res)

    responses = np.array(responses)
    time_stamp = time.strftime("%Y%m%d_%H%M")
    np.save("responses" + time_stamp + ".npy", responses)

    accuracy = list()
    amount_minus = list()
    amount_equal = list()
    amount_plus = list()
    for these_Bs, Bs in Bs_to_simulate:
            amount_minus.append(sum((responses[:,0] == "minus") *
                                    (responses[:,1] == these_Bs)))
            amount_equal.append(sum((responses[:,0] == "equal") *
                                    (responses[:,1] == these_Bs)))
            amount_plus.append(sum((responses[:,0] == "plus") *
                                   (responses[:,1] == these_Bs)))
            right_answer = these_Bs.split("_")[0]
            accuracy.append(float(sum((responses[:,1] == these_Bs) *
                                      (responses[:,0] == right_answer)))
                            / sum(responses[:,1] == these_Bs))

    amount_minus = np.array(amount_minus)
    amount_equal = np.array(amount_equal)
    amount_plus = np.array(amount_plus)

    accuracy = np.array(accuracy)
    np.save("accuracy" + time_stamp + ".npy", accuracy)

    print(accuracy)

    a = np.asarray([ amount_minus, amount_equal, amount_plus ])
    np.savetxt("data" + time_stamp + ".csv", a, delimiter=",", fmt='%3.2f')




    # ##################################################################################################################
    #
    #
    # responses = []
    # for i in range(64):
    #     responses.append( ("minus", "minus_5", 32) )
    # for i in range(64):
    #     responses.append( ("minus", "minus_4", 32) )
    # for i in range(64):
    #     responses.append( ("minus", "minus_3", 32) )
    # for i in range(64):
    #     responses.append( ("minus", "minus_2", 32) )
    # for i in range(64):
    #     responses.append( ("minus", "minus_1", 32) )
    # for i in range(64):
    #     responses.append( ("equal", "equal_2-", 32) )
    # for i in range(64):
    #     responses.append( ("equal", "equal_1-", 32) )
    # for i in range(64):
    #     responses.append( ("equal", "equal_0", 32) )
    # for i in range(64):
    #     responses.append( ("equal", "equal_1+", 32) )
    # for i in range(64):
    #     responses.append( ("equal", "equal_2+", 32) )
    # for i in range(64):
    #     responses.append( ("plus", "plus_1", 32) )
    # for i in range(64):
    #     responses.append( ("plus", "plus_2", 32) )
    # for i in range(64):
    #     responses.append( ("plus", "plus_3", 32) )
    # for i in range(64):
    #     responses.append( ("plus", "plus_4", 32) )
    # for i in range(64):
    #     responses.append( ("plus", "plus_5", 32) )
