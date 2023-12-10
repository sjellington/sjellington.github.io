import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def fn1(x,y):
    return (0.0*x, 0.16*y)
def fn2(x,y):
    return (0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6)
def fn3(x,y):
    return (0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6)
def fn4(x,y):
    return (-0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44)
fns = [fn1, fn2, fn3, fn4]

points = 100000
width, height = 500,500
fern_image = np.zeros((width, height))
x, y = 0, 0

for i in range(points):
    function = np.random.choice(fns, p=[0.01, 0.85, 0.07, 0.07])
    x, y = function(x,y)
    ix, iy = int(width / 2 + x * width / 7), int(y * height / 12)
    fern_image[iy,ix] = 1

plt.imshow(fern_image[::-1,:], cmap=cm.Greens)
plt.savefig('fern.svg')