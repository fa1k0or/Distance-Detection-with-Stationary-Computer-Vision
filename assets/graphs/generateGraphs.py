import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches


def f(x):
    return 1 + 1/(x)


def intialTest():
    test1P1P2 = [2.02,1.56,1.30,1.24]
    test1Distance = [1,2,3,4]

    falX = []
    falY = []

    for i in range(100,401):
        falX.append(i/100)
        falY.append(f(i/100))

    fig, ax = plt.subplots() #create graph

    maroon_patch = mpatches.Patch(color='maroon', label='L = 1 / ( P1: P2 - 1)')
    deepskyblue_patch = mpatches.Patch(color='deepskyblue', label='Results from Falkor')

    #wrist to tip
    ax.plot(test1Distance,test1P1P2,color = 'deepskyblue') #plot real length for camera 1
    ax.plot(falX,falY,color = 'maroon',linestyle = '--') #plot fictional length for camera 1

    ax.set(xlabel='Distance (L)',
       ylabel='P1/P2',
       title ='Results From Initial Test Against Equation Derived')

    ax.grid() #define x y values, title and grid

    plt.legend(handles=[deepskyblue_patch,maroon_patch])

    fig.savefig("graph4.png")
    plt.show()

def intialTestTable():
    print()

def secondTestTable():
    print()


if __name__ == '__main__':
    intialTest()