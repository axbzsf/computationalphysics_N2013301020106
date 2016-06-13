#第十次作业
- 何牧野 2013301020106

##背景
- 本次作业考虑台球在台球桌上的运动问题。

##内容
- 对于台球的运动问题，不考虑台球的自旋和体积，且认为台球为刚性球，则可简化为质点与在矩形封闭区域的碰撞问题，并由欧拉法可求出它的运动轨迹.
- 质点与边界的碰撞可以由下述方程给出:
 
    ![公式1](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework10/homework101.png)
- 反射后的速度为:

    ![公式2](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework10/homework102.png)
                                                                
- [代码1](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework10/homework10.py)

- 矩形边界.
  (1)给出初始条件为vx=1,vy=1

    ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework10/homework10a.png)
      
  (2)给出初始条件为vx=1,vy=2
  
    ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework10/homework10b.png)
      
  (3)给出初始条件为vx=1,vy=10
  
    ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework10/homework10c.png)
      
  (4)给出初始条件为vx=1,vy=50
  
    ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework10/homework10d.png) 
      
  (5))给出初始条件为vx=1,vy=100
  
    ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework10/homework10e.png)
      
  (6))给出初始条件为vx=1,vy=π
  
    ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework10/homework10f.png)
      

##结论
- 由图中可以看出：
  1.当速度方向即vx比vy为有理数时，轨迹为规则图形，且随着比值减小，台球可遍历整个区域.

  2.当速度方向即vx比vy为无理数时，轨迹极不规则，且与为有理数时不同，比值较大时也可遍历整个区域
- 再考虑真实台球中有自旋和与其它球碰撞的情况，整个轨迹将对初值极为敏感，为一混沌系统.

##致谢
- 感谢王铮同学的代码.
- 感谢百度.
