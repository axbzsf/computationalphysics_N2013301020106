#第十次作业
- 何牧野 2013301020106

##背景
- 本次作业考虑台球在台球桌上的运动问题。

##内容
- 对于台球的运动问题，不考虑台球的自旋和体积，则可简化为质点与在矩形封闭区域的碰撞问题，并由欧拉法可求出它的运动轨迹.
- 质点与边界的碰撞可以由下述方程给出:
 
    ![公式1](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter3/homework10/%E5%85%AC%E5%BC%8F1.png)
- 反射后的速度为:

    ![公式2](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter3/homework10/%E5%85%AC%E5%BC%8F2.png)
                                                                
- [代码1](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter3/homework10/10.py)

- 1.讨论矩形边界.
  (1)给出初始条件为vx=1,vy=2

    ![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter3/homework10/1%2C2.png)
      
  (2)给出初始条件为vx=1.32,vy=3
  
    ![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter3/homework10/1.32%2C3.png)
      
  (3)给出初始条件为vx=1.31,vy=3
  
    ![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter3/homework10/1.31%2C3.png)
      
  (4)给出初始条件为vx=1.33,vy=3
  
    ![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter3/homework10/1.33.png) 
      
  (5))给出初始条件为vx=1.32,vy=7^0.5
  
    ![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter3/homework10/1.32%2C7**0.5.png)
      
  
- 2.讨论圆形边界和体育场边界
  先考虑边界形状为半径为的圆形，可以预见台球的运动应该是高度规则的。然后考虑所谓的体育场模型，即在两个半圆之间加上一块矩形区域.
- 初始条件为vx=0.6,vy=0.8
   [代码2](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter3/homework10/10_1.py)
- 相应的轨迹和相图为 
           ![](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter3/homework10/2016-06-10%2021:10:48%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)


##结论
- 1.当速度方向即vx比vy为有限小数时,轨迹比较规则.
    当vx比vy为无限小数时,轨迹不再是规则的了.可以发现随着步数的增加,轨迹会逐渐充满整个区域.
    当vx比vy为无限不循环小数(无理数)时,轨迹更加密集和"魔性"了
- 2.圆形边界下,轨迹能到达的区域和不能到达的区域分界很明显.且相点基本分布在两条相轨上.很规则.
    而在体育场边界下,仅仅由于一点点的不对称,也可以看出最后轨迹几乎可以充满整个区域,而相图上的相点则分布不规则.
    
    
##致谢
- reference:课本
- 百度
- 感谢陈洋遥提供的范例.
