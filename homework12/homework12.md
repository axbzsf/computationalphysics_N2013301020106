#第十二次作业
- 何牧野 2013301020106

##摘要
- 本次作业为课本4.16题，讨论太阳，木星，地球三体系统的轨道运动.

##背景
- 在太阳，木星，地球系统中，可以考虑为地球在太阳-木星组成的双星系统中运动，当太阳-木星质量比变化时，地球轨道也随之变化。

##正文
- 考虑太阳-木星双星系统为圆轨道，具体讨论见[作业十一](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework11/homework11.md)
- 在此条件下，太阳和木星满足方程：

   ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework12/homework121.png)
   ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework12/homework122.png)
- 由欧拉法可得运动方程为：

   ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework12/homework123.png)
-则其速度方程有：

   ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework12/homework124.png)
  其中k为太阳木星质量之比。
[代码](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework12/homework12.py)
- 当太阳木星大小为实际比值，即k=1000时

   ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework12/homework12a.png)
- 当k=10时

   ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework12/homework12b.png)
-当太阳与木星质量相等，即k=1时

   ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework12/homework12c.png)
-当太阳小于木星，即k=0.1时

   ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework12/homework12d.png)
   ![](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework12/homework12e.png)
  
##结论
- 由图可以看出，木星质量越大，地球受扰越严重，当木星超过太阳质量时，地球将会飞离系统.

##致谢
- 感谢刘文涛同学的指导.
- 感谢百度百科
