#第十四次作业
  何牧野 2013301020106

##摘要
  本次作业为课本6.6题，讨论一维机械波的线性独立性。
 
##背景
  对一维机械波，满足一维线性波动方程，表现为其不同解的叠加仍然为线性方程的解。
  
##正文
- 一维机械波满足波动方程：
    ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework14/homework141.png)
- 我们取固定边界条件，则可让非端点位置离散化，由下列迭代法求解：
    ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework14/homework142.png)
- 考虑一个高斯型波包，波的传播形状为：
    ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework14/homework14a.gif)
- 对两波包施加不同的高斯型扰动，波的传播形状为：
    ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework14/homework14b.gif)

##总结
- 由上图可以看出，两波包虽然在相遇时会有叠加，但确实是线性独立的。

##致谢
- 感谢吴雨桥同学的代码。
- 感谢陈洋遥同学的指导。
