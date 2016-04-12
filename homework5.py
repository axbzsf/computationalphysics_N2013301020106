from pylab import*
v=[]
t=[]
dt=0.05
v.append(0)
t.append(0)
end_time=10
for i in range(int(end_time/dt)):
        vn=v[i]+(10-v[i]*dt)
        v.append(vn)
        t.append(dt*(i+1))
        print v[i]
plot(v,t,color='blue',linestyle='-')
ylabel("speed(m/s)")
xlabel("time(s)")
title("v-t")
savefig('homework5.png')
show()
