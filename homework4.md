# 第四次作页
##背景
- *本次作业选择了简单的1.2题，即关于匀速运动的问题*

##正文
- *这道题对匀速运动中路程与时间的函数关系式求解。*
- *解析解法为对常微分方程$$ dx/dt=v*detat**
- *用欧拉法解决该题就是将微分方程化为差分方程,即
 $$ v(t+detat)=v(t)+(a-b*v(t))*detat*
- *选择参数a=10,b=1,和初值为v(t=0)=100*
- *[代码在此](https://github.com/computationalphysics2013301020107/computationalphysics-N_2013301020107/blob/master/1.py)
- *![这是图片](https://github.com/computationalphysics2013301020107/computationalphysics-N_2013301020107/blob/master/v-t%E5%9B%BE.png)

- *进一步地,我找到了精确解:v=90+10/e^t,可以检验之前的欧拉法的正确度.[对比代码](https://github.com/computationalphysics2013301020107/computationalphysics-N_2013301020107/blob/master/homework4.py)
-  *![这是对比图](https://github.com/computationalphysics2013301020107/computationalphysics-N_2013301020107/blob/master/homework4.png)
 
##总结
- **明显可见用欧拉法计算的曲线和之前分析的情况一样.速度极限为10m/s.在大概6s的时候就已经很逼近极限值了.**
- **对比精确解和欧拉法可以发现二者在前段和后段都比较贴近,在曲线中间部分略有错开,证明在这里欧拉法出现了一点误差.仔细分析可以发现,这一段的曲线正是变化率较大的一段,说明欧拉法这种属于迭代的数值解法在变化率较大时会累计一定的误差,而在其他比较平缓的段则可以较好模拟.

##致谢
 **感谢百度!!感谢蔡老师的示例代码!!**
