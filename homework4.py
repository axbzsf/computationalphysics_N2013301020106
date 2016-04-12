from pylab import*
x=[]
t=[]
v=40
dt=0.01
x.append(0)
t.append(0)
end_time=10
for i in range(int(end_time/dt)):
    x.append(x[i]+v*dt)	
    t.append((i+1)*dt)
    print t[-1],x[-1]
plot(t,x,color="red",linestyle='-',label="work")
ylabel("high(m)")
xlabel("time(s)")
title("x-t")
savefig('aa.png')
show()
