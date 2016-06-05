#第六次作业
- 刘祥干 2013301020107
 
##摘要
- *本次作业为课本上2.9题，考虑风阻和空气密度对炮弹运动的影响，做出三条不同条件下的炮弹轨迹图。*

##背景
- 查询资料可得，炮弹射程在30-40km之间，与地球半径相比极小，故在不考虑地球自转的情况下，可以近似为平面运动求解。

##正文
- 坐标系:对于平面运动选择直角坐标系.
- 计算方程:只考虑重力时:F1=mg(垂直向下) 
           考虑风阻时:F2=-mBV^2(与速度方向相反)
           考虑空气密度变换时:B不再是常数,而和高度有关,采取绝热近似,则B'=(1-ay/T0)^alpha * B(y=0)
           
- 采用欧拉法:

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
                                
- 参数选择为vx=vy=700m/s,T0=288k,alpha=2.5,a=6.5*10^(-3),g=9.8
- [代码在此](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/homework6.py)
- ![这是对比图](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/homework6%281%29.png)
- 蓝线是没有风阻的情况,绿线是有风阻的情况,红线是考虑空气密度的情况.

##小结
- 由图易知,没有风阻的情况射程是最远的.而有风阻的情况下,考虑了空气密度变化的射程更远.这也符合常识(因为空气密度是随高度增高而减小的,阻力又和密度成正比.)

##致谢
- **感谢蔡老师的例子**
- **感谢刘祥干同学的帮助**
- **感谢百度**
