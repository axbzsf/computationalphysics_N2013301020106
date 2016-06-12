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
- [代码](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework8.py)

##结果
- ![3](https://github.com/axbzsf/computationalphysics_N2013301020106/blob/master/homework8.png)   


##总结
- 由图可以看出，α为3时有稳定解，且周期随角度变化。
 


##致谢
- 感谢张爽同学提供的原始代码和指导，感谢刘祥干提供的图片.
- reference:N.J. Giordano,H. Nakanishi.Computational Physics(second edition)（影印版）.清华大学出版社
