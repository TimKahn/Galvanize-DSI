import numpy as np
import scipy.stats as scs
import matplotlib.pyplot as plt


def plot_t():
    # t distribution 
    # inputs 
    df = 5 # degrees of freedom of t distribution
    t_dist = scs.t(df) # standardized t distribution
    plot_min_x = t_dist.ppf(0.005) # plot from 0.5% of area
    plot_max_x = t_dist.ppf(0.995) # to 99.5% of area
    num_x_vals = 200
    # set our limits based on our desired significance level
    t1 = t_dist.ppf(0.025) # t value at 2.5% of area
    t2 = t_dist.ppf(0.975) # t value at 97.5% of area
    # set the critical value
    t_cr = t_dist.ppf(0.99)

    "make the plot" 
    x_t = np.linspace(plot_min_x, plot_max_x, num_x_vals) 
    y_t = t_dist.pdf(x_t)
    fig, ax = plt.subplots(1,1)
    lbl = "t pdf with df {0}".format(df)
    ax.plot(x_t, y_t, lw = 3, label=lbl)
    ax.legend(loc = 'best')
    plt.axvline(x = t1, lw = 1, color = 'k')
    plt.axvline(x = t2, lw = 1, color = 'k')
    plt.axvline(x = t_cr, lw = 3, color = 'r')
    plt.xlabel('t value')
    plt.ylabel('t pdf')
    plt.savefig('t_dist.png')
    plt.close()


def plot_normal():
    # normal distribution (standardized)
    # inputs 
    norm_dist = scs.norm() # standardized normal distribution
    plot_min_x = norm_dist.ppf(0.005) # plot from 0.5% of area
    plot_max_x = norm_dist.ppf(0.995) # to 99.5% of area
    num_x_vals = 200
    # set our limits based on our desired significance level
    z1 = norm_dist.ppf(0.025) # z value at 2.5% of area
    z2 = norm_dist.ppf(0.975) # z value at 97.5% of area
    # set the critical value
    z_cr = norm_dist.ppf(0.99)

    "make the plot" 
    x_norm = np.linspace(plot_min_x, plot_max_x, num_x_vals) 
    y_norm = norm_dist.pdf(x_norm)
    fig, ax = plt.subplots(1,1)
    lbl = "normal pdf"
    ax.plot(x_norm, y_norm, lw = 3, label=lbl)
    ax.legend(loc = 'best')
    plt.axvline(x = z1, lw = 1, color = 'k')
    plt.axvline(x = z2, lw = 1, color = 'k')
    plt.axvline(x = z_cr, lw = 3, color = 'r')
    plt.xlabel('z value')
    plt.ylabel('normal pdf')
    plt.savefig('norm_dist.png')
    plt.close()


if __name__ == '__main__':
   plot_t() 
   plot_normal()
