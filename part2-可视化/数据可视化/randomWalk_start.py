import matplotlib.pyplot as plt
from RandomWalk import Randomwalk

while True:
    rw = Randomwalk()
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    points_number=range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_valuse,s=1,c=points_number,cmap=plt.cm.Blues,edgecolors="none")
    ax.scatter(0,0,c='red',s=100,edgecolors="none")
    ax.scatter(rw.x_values[-1],rw.y_valuse[-1],c='red',edgecolors="none",s=100)
    ax.set_aspect('equal')

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)


    plt.show()
    keep_running=input("Make another walk? Y/n")
    if keep_running == 'n':
        break