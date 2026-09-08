import matplotlib.pyplot as plt

x_values1=range(1,1001)
y_values1=[x**2 for x in x_values1]

fig, ax = plt.subplots()
ax.scatter(x_values1,y_values1,s=10,c=y_values1,cmap=plt.cm.Reds)
ax.set_title("Square Numbers",fontsize=24)
ax.set_xlabel("Numbers",fontsize=14)
ax.set_ylabel("Squares",fontsize=14)
ax.tick_params(labelsize=14)

ax.axis([0,1001,0,1_100_100])
plt.show()
