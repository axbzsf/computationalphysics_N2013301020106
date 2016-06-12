#第9次作业
- 何牧野 2013301020106

##摘要
- 本次作业为课本3.21题，用Euler-cromer model讨论非线性阻尼驱动物理摆的某些性质

##背景
- 对非线性阻尼驱动物理摆这种非线性模型，表现出混沌性质，故很难用解析法解得答案，我们选用Euler-cromer     model计算它在不同条件下的解。

##内容
- 非线性阻尼驱动物理摆的运动方程为:![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework91.png)
- 用Euler-cromer model有如下公式:![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework92.png)

- [代码](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework9.py)
- a.选择参数:F_D=5,Omega_D=2,q=1
     theta-t图
![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework9a1.png)
     相图
![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework9a2.png)
- b.选择参数:F_D=10,Omega_D=2,q=1
     theta-t图
![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework9b1.png)
     相图
![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework9b2.png)
- c.选择参数:F_D=100,Omega_D=2,q=1
     theta-t图
![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework9c1.png)
     相图
![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework9c2.png)
- d.选择参数:F_D=1000,Omega_D=2,q=1
- 
     theta-t图
![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework9d1.png)
     相图
![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework9d2.png)
    
##结论
- 由图可见，非线性阻尼驱动物理摆系统虽然是由一个决定性的方程描述的，但由于方程对初值极为敏感，故有混沌现象产生。
- 尽管如此，我们仍可通过一定的近似和计算来研究混沌系统

##致谢
- 感谢张爽同学的基本代码.
- 感谢郭潇同学的指导


