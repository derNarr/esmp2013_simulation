if __name__ == "__main__":
    
    n = 2j
    y1, y2, y3 = np.mgrid[0.14:0.16:n, 0.14:0.16:n, 0.14:0.16:n]
    starting_yy1 = y1.flatten()
    starting_yy2 = y2.flatten()
    starting_yy3 = y3.flatten()
    #plot_scatter(final_y)
    
    Bs_to_simulate = {
        "minus_5" : (8500, 8000, 8000),
        "minus_4" : (8400, 8000, 8000),
        "minus_3" : (8300, 8000, 8000),
        "minus_2" : (8200, 8000, 8000),
        "minus_1" : (8100, 8000, 8000),
        
        "same_2-" : (8000, 8100, 8000),
        "same_1-" : (8000, 8300, 8000),
        "same_0" : (8000, 8500, 8000),
        "same_1+" : (8000, 8300, 8000),
        "same_2+" : (8000, 8100, 8000),
        
        "plus_1" : (8000, 8000, 8100),
        "plus_2" : (8000, 8000, 8200),
        "plus_3" : (8000, 8000, 8300),
        "plus_4" : (8000, 8000, 8400),
        "plus_5" : (8000, 8000, 8500),
        }
    
    final_y = list()
    for these_Bs in Bs_to_simulate:
        Bs = Bs_to_simulate[these_Bs]
        
        for i in range(len(starting_yy1)):
            y = simulate((starting_yy1[i], starting_yy2[i], starting_yy3[i]), t_begin=0.0, t_end=0.02, dt=.0001, Bs=Bs)
            final_y.append(y)
    
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
