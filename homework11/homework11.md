#第十一次作业
- 何牧野 2013301020106

##背景
- 本次作业讨论双星系统，同时考虑广义相对论的影响

##内容
- 由万有引力定律方程为:

     ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework11/homework111.png)
    
- 又由牛顿第二定律：

    ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework11/homework112.png)
    
- 引入约化质量u，将双星系统简化为单体问题:
    ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework11/homework113.png)
    
- 可求得轨道方程为：
    ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework11/homework114.png)
    
- 其中l为：
  ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework11/homework115.png)
  
- e为离心率，与系统初值有关.
   [代码](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework11/homework11.py)
    ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework11/homework11a.png)
    
- 考虑广义相对论的影响，定性的表示为对平方反比率的微小偏离，即：
    ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework11/homework116.png)
    [代码](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework11/homework111.py)
    ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework11/homework11b.png)
    ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework11/homework11c.png)
    
##结论
- 由图可以看出，当满足牛顿平方反比率时，轨道为稳定的圆锥曲线.
- 考虑广义相对论的影响，不满足平方反比时，轨道有进动现象，与相对论预言的定性符合

##致谢
- 感谢王铮同学的代码.
- 感谢贾俊基老师教授的广义相对论引论
