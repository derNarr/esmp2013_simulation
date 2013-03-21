#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import time

import matplotlib.pyplot as plt
import pylab as pl
import numpy as np

from simulate_c import simulate
from helper import plot_scatter, plot2, simpleaxis, spine_shift

if __name__ == "__main__":

    subject = 1

    n = 6j
    y1, y2, y3 = np.mgrid[0.14:0.16:n, 0.14:0.16:n, 0.14:0.16:n]
    starting_yy1 = y1.flatten()
    starting_yy2 = y2.flatten()
    starting_yy3 = y3.flatten()
    #plot_scatter(final_y)

    # Biased to right
    if subject == 1:
        
        NBs = 20
        B = 8000
        b1 = np.linspace(0.9, 1.1, NBs)
        b3 = np.linspace(1.1, 0.9, NBs)
        c = np.concatenate((np.linspace(1.035, 0.965, 12),
                           np.linspace(0.965, 1.035, 8)))
        B1 = B*b1*c*0.5 + B*0.5
        B2 = (1-c)*B + B
        B3 = B*b3*c*0.5 + B*0.5
        asymm = 0.985
        B1 = asymm*B1
        B3 = B3+(1-asymm)*B3
        
        title_plot = 'Subject 1 - response bias to right'
        filename_data = 'sub1_data'

    # Biased to left
    if subject == 2:
        
        NBs = 20
        B = 8000
        b1 = np.linspace(0.9, 1.1, NBs)
        b3 = np.linspace(1.1, 0.9, NBs)
        c = np.concatenate((np.linspace(1.035, 0.965, 8),
                           np.linspace(0.965, 1.035, 12)))
        B1 = B*b1*c*0.5 + B*0.5
        B2 = (1-c)*B + B
        B3 = B*b3*c*0.5 + B*0.5
        asymm = 0.985
        B1 = B1+(1-asymm)*B1
        B3 = asymm*B3
        
        title_plot = 'Subject 2 - response bias to left'
        filename_data = 'sub2_data'

    # Biased to unproductive
    if subject == 3:
    
        NBs = 20
        B = 8000
        b1 = np.linspace(0.98, 1.02, NBs)
        b3 = np.linspace(1.02, 0.98, NBs)
        c = np.concatenate((np.linspace(1.01, 0.99, 12),
                            np.linspace(0.99, 1.01, 8)))
        B1 = B*b1*c*0.5 + B*0.5
        B2 = (1-c)*B + B
        B3 = B*b3*c*0.5 + B*0.5
        asymm = 1.0
        B1 = asymm*B1
        B3 = B3+(1-asymm)*B3
        
        title_plot = 'Subject 3 - hungover'
        filename_data = 'sub3_data'

    Bs_to_simulate = [("SOA_%i" % i, (B1[i], B2[i], B3[i])) for i in range(NBs)]

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
    # np.save("responses" + time_stamp + ".npy", responses)

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

    # accuracy = np.array(accuracy)
    # np.save("accuracy" + time_stamp + ".npy", accuracy)
    # print(accuracy)

    a = np.asarray([ amount_minus, amount_equal, amount_plus ])
    # np.savetxt("data" + time_stamp + ".csv", a, delimiter=",", fmt='%3.2f')
    
    np.savetxt(filename_data + ".csv", a, delimiter=",", fmt='%3.2f')
    
    
    #### PLOT ####
    
    fig = plt.figure(figsize=(5,4))
    ax = pl.axes()
    x = np.linspace(0, 19, 20)
    ax.plot(x, B1, 'b', label='B1: Sooner', lw=3)
    ax.plot(x, B2, 'r', label='B2: Equal', lw=3)
    ax.plot(x, B3, 'g', label='B3: Later', lw=3)
    spine_shift(ax)
    simpleaxis(ax)
    ax.axes.set_ylim((7500,8800))
    ax.axes.xaxis.set_ticklabels([-400,-200,0,200,400])
    ax.set_title(title_plot, size = 16)
    ax.set_ylabel('B parameter', size = 12)
    ax.set_xlabel('SOA (ms)', size = 12)
    leg = ax.legend(loc='upper right')
    leg.get_frame().set_alpha(0.9)
    if leg:
        for t in leg.get_texts():
            t.set_fontsize(14)    # the legend text fontsize
        for l in leg.get_lines():
            l.set_linewidth(2)  # the legend line width
    pl.subplots_adjust(bottom=0.15, top=0.9, left=0.15)
    pl.gca().spines["bottom"].set_linewidth(.5)
    pl.gca().spines["left"].set_linewidth(.5)
    
    fig.savefig(str.split(filename_data, '_')[0] + "_plot_Bs.pdf")
    
    
    
    
    #### REACTION TIMES ####
    n = 15j
    y1, y2, y3 = np.mgrid[0.14:0.16:n, 0.14:0.16:n, 0.14:0.16:n]
    starting_yy1 = y1.flatten()
    starting_yy2 = y2.flatten()
    starting_yy3 = y3.flatten()
    responses = list()
    for i in range(len(starting_yy1)):
        answer, reaction_time = simulate((starting_yy1[i], starting_yy2[i], starting_yy3[i]),
                       t_begin=0.0, t_end=0.10, dt=.0001, Bs=Bs_to_simulate[4][1])
        res = (answer, these_Bs, reaction_time)
        print res
        responses.append(res)
    
    responses = np.array(responses)
    
    
    RTs_minus = np.array(responses[(responses[:,0] == "minus"),2], dtype=int)
    RTs_equal = np.array(responses[(responses[:,0] == "equal"),2], dtype=int)
    RTs_plus = np.array(responses[(responses[:,0] == "plus"),2], dtype=int)
    
    fig = plt.figure(figsize = (5,4))
    ax1 = plt.subplot(1,1,1)
    ax1.hist(RTs_minus, bins=25, color='b', alpha=0.3, normed=True)
    ax1.hist(RTs_equal, bins=25, color='r', alpha=0.3, normed=True)
    ax1.hist(RTs_plus, bins=25, color='k', alpha=0.3, normed=True)
    spine_shift(ax1)
    simpleaxis(ax1)
    ax1.set_title("Reaction Times", size = 16)
    ax1.set_ylabel('', size = 12)
    ax1.set_xlabel('Reaction Time (ms)', size = 12)
    pl.subplots_adjust(bottom=0.17, top=0.9, left=0.15)
    pl.gca().spines["bottom"].set_linewidth(.5)
    pl.gca().spines["left"].set_linewidth(.5)
    
    fig.savefig(str.split(filename_data, '_')[0] + "_reaction_times2.pdf")
    
    # #### REACTION TIMES ####
    # 
    # RTs_minus = list()
    # RTs_equal = list()
    # RTs_plus = list()
    # for these_Bs, Bs in Bs_to_simulate:
    #     RTs_minus.append(responses[(responses[:,0] == "minus") *
    #                          (responses[:,1]==these_Bs),2])
    #     RTs_equal.append(responses[(responses[:,0] == "equal") *
    #                          (responses[:,1]==these_Bs),2])
    #     RTs_plus.append(responses[(responses[:,0] == "plus") *
    #                          (responses[:,1]==these_Bs),2])
    # 
    # number_of_subplots = len(RTs_minus)
    # fig = plt.figure(figsize=(5,4*number_of_subplots))
    # for i,v in enumerate(xrange(number_of_subplots)):
    #     
    #     x = np.array(RTs_minus[i], dtype=int)
    #     y = np.array(RTs_equal[i], dtype=int)
    #     z = np.array(RTs_plus[i], dtype=int)
    #     
    #     xx = np.concatenate((x,y,z))
    # 
    #     subplots_adjust(hspace=0.000)
    #         
    #     v = v+1
    #     ax1 = subplot(number_of_subplots,1,v)
    #     try:
    #         ax1.hist(x, bins=25, alpha=0.3)
    #         ax1.hist(y, bins=25, alpha=0.3)
    #         ax1.hist(z, bins=25, alpha=0.3)
    #     except ValueError:
    #         pass
    #     
    #     # ax1.hist(xx, bins=25, alpha=0.3)
    # 
    # fig.savefig("reaction_times2.pdf")
    
    
    
    
    
    
    
    
    
    
    
    
    
    

# ##################################################################################################################
