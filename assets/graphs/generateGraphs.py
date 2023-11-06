import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np

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
    # average marks data for 5 consecutive years 
    data = [[1.98,1.87,2.23,2.02,0.98],
            [1.53,1.68,1.32,1.56,1.79],
            [1.25,1.36,1.28,1.30,3.33],
            [1.31,1.16,1.26,1.24,4.17]]
  
    columns = ('P1:P2 of Trial One', 'P1:P2 of Trial Two', 'P1:P2 of Trial Three', 
           'Average P1:P2', 'Distance Calculated (L)') 
    rows = ['%d L from Camera One' % x for x in (1, 2, 3, 4)] 
  
    colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows))) 
    index = np.arange(len(columns)) + 0.3
    bar_width = 0.4
    n_rows = len(data)
  
    # Initialize the vertical-offset for 
    # the line plots. 
    y_offset = np.zeros(len(columns)) 
  
    cell_text = [] 
    for row in range(n_rows): 
        y_offset = data[row] 
        cell_text.append([x for x in y_offset]) 
  
    # Reverse colors and text labels to display 
    # the last value at the top. 
    colors = colors[::-1] 
    cell_text.reverse() 
  
    # Add a table at the bottom of the axes 
    the_table = plt.table(cellText=cell_text, 
                      rowLabels=rows, 
                      rowColours=colors, 
                      colLabels=columns, 
                      loc='top') 
  
    #plt.ylabel("marks".format(value_increment)) 
    #plt.xticks([]) 
    plt.title('average marks in each consecutive year') 
  
    plt.show() 

def secondTestTable():
    print()


if __name__ == '__main__':
    intialTestTable()