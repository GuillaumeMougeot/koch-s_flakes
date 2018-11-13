import numpy as np
import matplotlib.pyplot as plt

def koch(n):
    angle = [0,np.pi/3,-np.pi/3,0]
    index = [0 for i in range(n)]
    index[0] = 1
    L = 1/(pow(3,n))
    x = [0,L]
    y = [0,0]
    for k in range(pow(4,n)-1):
        angl = sum([angle[index[k]] for k in range(n)])
        x += [x[k+1] + L * np.cos(angl)]
        y += [y[k+1] + L * np.sin(angl)]
        i = 0
        index[i] += 1
        while i < n and index[i] == 4:
            index[i] = 0
            i += 1
            if i < n:
                index[i] += 1
    return x,y


x, y = koch(8)
plt.plot(x,y)
plt.show()
