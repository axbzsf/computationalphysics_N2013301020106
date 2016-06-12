#第八次作业
- 何牧野 2013301020106

##摘要
- 本次作业为课本3.4题，采用Euler-cromer methond对单摆模型进行处理


##背景
- 单摆为现实中比较常见的一种物理模型，通常是采用小角近似的方法进行解析求解。
- 于是我们可以用Euler-cromer methond进行数值求解。
- ![单摆图片] (https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter3/2016-06-01%2012:04:55%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)


##正文
- 单摆动力学方程为:
- ![1](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework81.png)
- 有解为:
- ![2](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework82.png)
- 由Euler methond有
- ![3](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework83.png)
- 由Euler-cromer methond有
- ![3](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework84.png)
##结果(线长都为1m)
- 1.初始值w0=0,thet0=15度,计算步长dt=0.01s
     thet-t对比图![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter3/problem3.8_1.png)
- 2.初始值wo=0,thet0=60度,计算步长dt=0.01s
     thet-t对比图![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter3/problem3.8_2.png)

- 3.初始值w0=0,thet0=179.9度,计算步长dt=0.01s
     thet-t对比图![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter3/problem3.8_5.png)
     相图![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter3/%20phase%20diagram1.png)

- 4.初始值w0=2,thet0=179度,计算步长dt=0.01s
     thet-t对比图![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter3/problem3.8_4.png)
     相图![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter3/phase%20diagram2.png)



##总结
- 从这几个对比图可以看出,当初始角度越大时,与非线性摆与线性摆的差别越大.
- 也可以看出,非线性摆的周期随着初始摆幅的增大而增大,后面越来越明显.
- 如果初始角速度超过一定值,其相图不再是封闭的轨线.系统不稳定.即出现了非线性系统的一般特征.
 


##致谢
- 感谢郭潇同学提供的原始代码和指导.
- reference:N.J. Giordano,H. Nakanishi.Computational Physics(second edition)（影印版）.清华大学出版社
##背景
- 单摆现象很常见,然而解析求解只能通过一级近似变成谐振子模型,这时要求单摆的线长较长而摆度及振幅较小.
- 如果直接数值求解呢?结果会怎样?此次作业选择书本上3.8题.借此粗略的讨论一下.
- ![单摆图片] (https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter3/2016-06-01%2012:04:55%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)

