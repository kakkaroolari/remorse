import numpy as np                 # v 1.19.2
import matplotlib.pyplot as plt    # v 3.3.2
#from pylab import *


def f(x):
    return 2*x + 1

if __name__ == "__main__":
    # input, syote on: (-5,-4,-3,-2,-1,0,1,2,3,4,5)
    x_arvot = range(-5, 6)
    # tulosta "otsikko"
    print("y = 2*x + 1") # todo: lue funktiosta.. DRY
    # iteroi x_arvot arraysta:
    y_arvot = []
    for x_arvo in x_arvot:
        # laske funktiolla y:n arvo
        y_arvo = f(x_arvo)
        # tulosta pisteen koordinaatit
        print("kun x={x}, y={y}".format(x=x_arvo, y=y_arvo))
        # laita y koordinaatti listaan (Sama kohta kun x)
        y_arvot.append(y_arvo)
    # yritä piirtää koordinaattisysteemi
    #scatter(x_arvot, y_arvot, s=100 ,marker='o')
    #show()
    # Plot points
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.scatter(x_arvot, y_arvot)

    # Select length of axes and the space between tick labels
    xmin, xmax, ymin, ymax = -5, 5, -5, 5
    ticks_frequency = 1    

    # Set bottom and left spines as x and y axes of coordinate system
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Create 'x' and 'y' labels placed at the end of the axes
    ax.set_xlabel('x', size=14, labelpad=-24, x=1.03)
    ax.set_ylabel('y', size=14, labelpad=-21, y=1.02, rotation=0)

    # Create custom major ticks to determine position of tick labels
    x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
    y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
    ax.set_xticks(x_ticks[x_ticks != 0])
    ax.set_yticks(y_ticks[y_ticks != 0])

    # Create minor ticks placed at each integer to enable drawing of minor grid
    # lines: note that this has no effect in this example with ticks_frequency=1
    ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
    ax.set_yticks(np.arange(ymin, ymax+1), minor=True)

    # Draw major and minor grid lines
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

    # Draw arrows
    arrow_fmt = dict(markersize=4, color='black', clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)

    plt.show()