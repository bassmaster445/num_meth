import numpy as np
import matplotlib.pyplot as plt
#Define our problem
#diffusivity of rod, theoretical amount below, insert appropriate coef. for material in question. mm^2/s
a = 110
#length of rod in mm
length = 50
#time for temperature to diffuse in seconds
time = 4
#nodes on the rod, "cut" it up into segments so we can handle finite number of sections. More nodes, more precise
nodes = 100

#Initialization
dx = length / nodes
dy = length / nodes

#dt derived from stability analysis of this finite difference to ensure numerical solution is stable and not too fast.
dt = min(dx**2 / (4 * a), dy**2 / (4 * a))
t_nodes = int(time/dt)
#temperature at the ends of the rod must be known and distribution of temp before time starts must be known.
u = np.zeros((nodes, nodes)) + 20 #Rod is initially at 20°C 
#Bound Initial Conditions, temp in C
u[0, :] = 100
u[-1, :] = 100

#Simulation
fig, axis = plt.subplots()

pcm = axis.pcolormesh(u, cmap = plt.cm.jet, vmin = 0, vmax = 100)
plt.colorbar(pcm, ax = axis)


counter = 0

plt.ion()

while counter < time:
    w = u.copy()
    for i in range(1, nodes-1):
        for j in range(1, nodes - 1):

            dd_ux = (w[i-1, j] - 2*w[i,j] + w[i+1,j])/dx**2
            dd_uy = (w[i, j-1 ]- 2*w[i,j] + w[i, j+1])/dx**2

            u[i, j] = dt * a * (dd_ux + dd_uy) + w[i, j] #derived from differential scheme
    counter += dt
    print("t: {:.3f} [s], Average temperature: {:.2f} Celsius".format(counter, np.average(u)))

    #update plot after each iteration

    pcm.set_array(u)
    axis.set_title("Distribution at t: {:.3f} [s].".format(counter))
    plt.draw()
    plt.pause(.01) #every 10 ms

plt.ioff()
plt.show()