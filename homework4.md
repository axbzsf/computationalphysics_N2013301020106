# 第四次作页
##背景
- *本次作业选择了简单的1.2题，即关于匀速运动的问题。*

##正文
- *这道题对匀速运动中路程与时间的函数关系式求解。*
- *解析解法就是为对常微分方程 dx/dt=vdt求解，容易解得x=vt+vt0。*
- *数值解法即为欧拉法。*
- *选择参数v=40,dt=0.01*
- *[代码](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework4.py)
- *![图片](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework4.png）

- *进一步地,我找到了精确解:v=90+10/e^t,可以检验之前的欧拉法的正确度.[对比代码](https://github.com/computationalphysics2013301020107/computationalphysics-N_2013301020107/blob/master/homework4.py)
-  *![这是对比图](https://github.com/computationalphysics2013301020107/computationalphysics-N_2013301020107/blob/master/homework4.png)
 
##总结
- **明显可见用欧拉法计算的曲线和之前分析的情况一样.速度极限为10m/s.在大概6s的时候就已经很逼近极限值了.**
- **对比精确解和欧拉法可以发现二者在前段和后段都比较贴近,在曲线中间部分略有错开,证明在这里欧拉法出现了一点误差.仔细分析可以发现,这一段的曲线正是变化率较大的一段,说明欧拉法这种属于迭代的数值解法在变化率较大时会累计一定的误差,而在其他比较平缓的段则可以较好模拟.

##致谢
 **感谢百度!!感谢蔡老师的示例代码!!**
