import numpy as np # import packages
import math
import mpl_toolkits.mplot3d
import matplotlib.pyplot as plt
# class BASEBALL will compute the trajetory of the baseball with air resistance
# vx0,vy0,vz0: initial velocity of the baseball
# dt: time step size
# omgx,omgy,omgz: the angular velocity
class BASEBALL(object):
    def __init__(self, _vx0, _vy0, _vz0, _dt= 0.1, _omgx=0,_omgy=0,_omgz=0):
        self.vx, self.vy, self.vz= _vx0, _vy0, _vz0
        self.v = math.sqrt(_vx0**2+ _vy0**2+ _vz0**2)
        self.B2= 0.0039+ 0.0058/(1.+math.exp((self.v-35)/5))
        self.S0= 4.1E-4
        self.g= 9.8
        self.dt= _dt
        self.x, self.y, self.z= [0], [50], [0]
        self.omgx, self.omgy, self.omgz= _omgx, _omgy, _omgz
    def calculate(self):
        while True:
            self.x.append(self.vx*self.dt+self.x[-1]) # append coordinates to x,y,z
            self.y.append(self.vy*self.dt+self.y[-1])
            self.z.append(self.vz*self.dt+self.z[-1])
            self.vx, self.vy, self.vz = \
                (-self.B2*self.v*self.vx+ self.S0*self.vy*self.omgz)*self.dt+ self.vx, \
                (-self.g- self.B2*self.v*self.vy+ self.S0*self.vz*self.omgx)*self.dt+ self.vy,\
                (self.S0*self.vx*self.omgy)*self.dt+ self.vz # change the velocity
            self.v= math.sqrt(self.vx**2+self.vy**2+self.vz**2)
            self.B2= 0.0039+ 0.0058/(1.+math.exp((self.v-35)/5))
            if self.y[-1]< -100:
               break
    def graphics(self,_gra, _omgz):
        _gra.plot(self.x, self.y, label=r'$\omega _z$ = %.2f rad/s'%_omgz)
        _gra.scatter([self.x[0],self.x[-1]],[self.y[0],self.y[-1]],s=30)
# class BASEBALL_NONFRIC will compute the trajetory of the baseball WITHOUT air resistance
# where
# vx0,vy0,vz0: initial velocity of the baseball
# dt: time step size
# omgx,omgy,omgz: the angular velocity
class BASEBALL_NONFRIC(BASEBALL):
    def calculate(self):
        while True:
            print self.y
            self.x.append(self.vx*self.dt+self.x[-1]) # append coordinates to x,y,z
            self.y.append(self.vy*self.dt+self.y[-1])
            self.z.append(self.vz*self.dt+self.z[-1])
            self.vx, self.vy, self.vz = \
                self.vx, \
                -self.g*self.dt+ self.vy, \
                self.vz # change the velocity
            if self.y[-1]< 0:
                self.gama= -self.y[-2]/self.y[-1]
                self.x[-1],self.y[-1]= \
                    (self.x[-2]+self.gama*self.x[-1])/(self.gama+1.),0
                break
def graphics(self,_gra,_dt):
    _gra.plot(self.x, self.y, '--',label= 'dt = %.2f s'%_dt)
    _gra.scatter([self.x[0],self.x[-1]],[self.y[0],self.y[-1]],s=30)
# this class give another plotstyle of the trajetory of baseball without air resistance
class BASEBALL_NONFRIC_2(BASEBALL_NONFRIC):
    def graphics(self,_gra,_dt):
        _gra.plot(self.x, self.y, '--',label=' no air drag')
        _gra.scatter([self.x[0],self.x[-1]],[self.y[0],self.y[-1]],s=30)
fig= plt.figure(figsize=(11,6))

ax2= plt.subplot(1,2,1)
comp= BASEBALL_NONFRIC_2(500*0.4470*math.cos(np.pi/4), 500*0.4470*math.sin(np.pi/4), 0., 0.1)
comp.graphics(ax2,0.1)
for omgz in [-5000., -1000.,0, 1000., 5000.]:
    comp= BASEBALL(500*0.4470*math.cos(np.pi/4), 500*0.4470*math.sin(np.pi/4), 0., 0.1, 0, 0, omgz)
    comp.calculate()
    comp.graphics(ax2,omgz)
ax2.set_xlabel('x (m)', fontsize=18)
ax2.set_ylabel('y (m)', fontsize=18)
ax2.set_title('trajectory of batted ball', fontsize=15)

ax2.legend(fontsize=8)
ax2.text(10,80,'with air drag', fontsize= 10)
plt.show(fig)
