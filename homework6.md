#第六次作业
 
##摘要
- *本次作业为课本上2.9题，考虑风阻和空气密度对炮弹运动的影响，做出三条不同条件下的炮弹轨迹图。*

##背景
- 查询资料可得，炮弹射程在30-40km之间，与地球半径相比极小，故在不考虑地球自转的情况下，可以近似为平面运动求解。

##正文
- 选择直角坐标系，作三个不同方程如下：
           只考虑重力时:F1=mg(垂直向下) 
           考虑风阻时:F2=-mBV^2(与速度方向相反)
           考虑空气密度变换时:B不再是常数,而和高度有关,采取绝热近似,则B'=(1-ay/T0)^alpha * B(y=0)
           
- 采用数值解法，即欧拉法，有:

               只考虑重力时:x(i+1)=xi+vx(i)*dt
                           vx(i+1)=vx(i)
                           y(i+1)=y(i)+vy(i)*dt
                           vy(i+1)=vy(i)-g*dt
                           
               考虑风阻时:x(i+1)=xi+vx(i)*dt
                          vx(i+1)=vx(i)-B*v*vx(i)*dt
                          y(i+1)=y(i)+vy(i)*dt
                          vy(i+1)=vy(i)-g*dt-B*v*vy(i)*dt
                          
               考虑空气密度变化时: x(i+1)=xi+vx(i)*dt
                                  vx(i+1)=vx(i)-B'*v*vx(i)*dt
                                  y(i+1)=y(i)+vy(i)*dt
                                  vy(i+1)=vy(i)-g*dt-B'*v*vy(i)*dt      
                                
- 查阅资料可知，炮弹出射速度为500-700m/s，故取参数为vx=vy=500m/s。
- 考虑温度为室温，取参数为T0=293k,alpha=2.5,a=6.5*10^(-3),g=9.8
- [代码](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework6.py)
- ![图](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework6.png)
- 蓝线是没有风阻的情况,绿线是有风阻的情况,红线是考虑空气密度的情况.

##总结
- 由图可以看出，风阻和空气密度对炮弹射程影响极大。

##致谢
- 感谢蔡老师的例子
- 感谢刘祥干同学的帮助
- 感谢百度
