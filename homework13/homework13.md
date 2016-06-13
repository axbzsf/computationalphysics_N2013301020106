#第十三次作业
 何牧野 2013301020106
 
##背景
- 本次作业为课本5.3题，讨论具体两平行板电容组成的方形势场中的电势能的分布。

##正文
- 对无源静电场问题，可由麦克斯韦方程组求解，静电势满足拉普拉斯方程：
    ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework13/homework131.png)
-在直角坐标系下，可将方程离散化为：
    ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework13/homework132.png) 
-由于该方程的解并不容易猜出，故可采用Jacobi算法，即：先随便猜一个解，再将此解带入方程右边，可得一个新解，再重复以上过程，知道收敛。
-对平行板电容而言，其势场存在对称性，故可只计算其中的对称部分，再由对称性直接对其他区域赋值，可简化计算。
-取两边电位为1V，则可得势场图像为：
   [代码](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework13/homework13.py)
    ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework13/homework13a.png) 


 
##总结
- 由图可知，电势能分布极为对称，符合平行板电容的电势分布
- 

##致谢
-感谢刘文焘同学的代码
-感谢电磁学
