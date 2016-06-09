#第七次作业
- 何牧野 2013301020106

##背景
- 本次作业为课本2.19题，在考虑空气阻力的情况下讨论棒球运动的轨迹。


##正文
- 棒球的飞行为抛体运动，但考虑到棒球的质量和体积较小，相对速度较快，且带有一定的自旋。故棒球在飞行过程中除受到重力作用外，还会受到空气阻力和因棒球旋转产生的马格努斯力。
- 棒球飞行轨迹可由下述方程描述:![公式1](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter2/%E5%85%AC%E5%BC%8F1.png)
- S0在棒球的运动速度范围内一般是常量,而B2依赖于速度,其近似公式为:![公式2](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter2/%E5%85%AC%E5%BC%8F2.png)
- 欧拉法求解其运动:
  ![公式3](https://github.com/computationalphysics2013301020107/computationalphysics_N2013301020107/blob/master/chapter2/%E5%85%AC%E5%BC%8F3.png)
- 为了减小欧拉法带来的误差,将步长设为0.1秒.
- 考虑投掷棒球的实际情况：
- 取初始发射角为0度,为了使轨迹更明显，初始发射高度为50米,落地点取为-100米.
- 取初速度为500mph,分别取不同角速度计算,结果如下图
- [这是代码1](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework7.py)
- ![这是图片](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework7.png)
- 在三维空间的运动:其他参数不变,将角速度改为沿z轴方向,棒球的运动就会呈现三维的螺旋,即所谓的弧线球.
- [这是代码2](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework72.py)
- ![这是图片](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework72.png)

##小结
- 由图可见，棒球运动的特性使其轨迹在不同角速度下差别极大，但在实际棒球比赛中，由于人投球的高度为两米左右，故不会出现图中的奇异轨迹，只表现为微小的不同。

##感谢
- 感谢陈洋遥同学的代码.
- 感谢蔡老师课上的讲解.
- 感谢刘祥干同学的公式图
