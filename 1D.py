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
#dt derived from stability analysis of this finite difference to ensure numerical solution is stable and not too fast.
dt = .5 * dx**2 / a
t_nodes = int(time/dt)
#temperature at the ends of the rod must be known and distribution of temp before time starts must be known.
u = np.zeros(nodes) + 20 #Rod is initially at 20°C 
#Bound Initial Conditions, temp in C
u[0] = 100
u[-1] = 100

#Simulation
fig, axis = plt.subplots()

pcm = axis.pcolormesh([u], cmap = plt.cm.jet, vmin = 0, vmax = 100)
plt.colorbar(pcm, ax = axis)
axis.set_ylim([-2,3])

counter = 0

plt.ion()

while counter < time:
    w = u.copy()
    for i in range(1, nodes-1):
        u[i] = dt * a * (w[i-1]-2*w[i]+w[i+1]) / dx**2 + w[i] #derived from differential scheme
    counter += dt
    print("t: {:.3f} [s], Average temperature: {:.2f} Celsius".format(counter, np.average(u)))

    #update plot after each iteration

    pcm.set_array([u])
    axis.set_title("Distribution at t: {:.3f} [s].".format(counter))
    plt.draw()
    plt.pause(.01) #every 10 ms

plt.ioff()
plt.show()
    