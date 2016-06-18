import numpy as np 
import random 
import matplotlib.pyplot as plt 

N = 10
M = 1e11
#pos = np.array([[1, 0], [4,4], [3,7]], dtype='float')
#vel = np.array([[-1, 0], [1,0], [1,1]], dtype='float')
pos = 10 * np.array([[random.random() - 0.5, random.random() - 0.5] for i in range(N)]) 
vel = 2 * np.array([[random.random() - 0.5, random.random() - 0.5] for i in range(N)]) 
G = 6.67e-11
Lambda = 1e-3
epsilon = 0.1

def force(x1, x2):
	# the force on 1 by 2
	# or acceleration
	dx = 1.0 * (np.array(x2) - np.array(x1))
	return dx * G * M / (np.dot(dx, dx) + epsilon**2)**1.5 - dx * Lambda 

def update(dt):
	# update vel
	for i in range(N):
		for j in range(N):
			if i != j:
				vel[i] += force(pos[i], pos[j]) * dt 
	# update pos
	for i in range(N):
		pos[i] += vel[i] * dt 


for i in range(10):
	print force([0,0], [10*i, 0])


x_lst = [[] for i in range(N)]
y_lst = [[] for i in range(N)]
TIME = 1
dt = 0.01
for i in range(int(TIME/dt)):
	update(dt)
	for j in range(N):
		x_lst[j].append(pos[j][0])
		y_lst[j].append(pos[j][1])



for i in range(N):
	plt.plot(x_lst[i], y_lst[i])

plt.show()
