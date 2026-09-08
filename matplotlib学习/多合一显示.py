import matplotlib.pyplot as plt
plt.figure()
plt.subplot(2,1,1)#分成两行两列
plt.plot([0,1],[0,1])

plt.subplot(2,3,4)
plt.scatter([1,1],[1,2])

plt.subplot(2,3,5)
plt.scatter([1,1],[1,2])

plt.subplot(2,3,6)
plt.scatter([1,1],[1,2])
plt.show()