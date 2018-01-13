# 07-Halide

## 组员

| Name |  身份  |                GitHub ID                 |
| :--: | :--: | :--------------------------------------: |
| 张航凯  |  队长  |  [Catkins](https://github.com/Caktins)   |
|  汪超  |  队员  |  [ChaoWao](https://github.com/ChaoWao)   |
| 阮超逸  |  队员  | [Christianyi](https://github.com/Christianyi) |

## 简介

本项目以研究编程语言Halide为主。Halide旨在使编写高性能图像处理代码更加容易。 Halide的前端目前嵌在C ++中。
预期研究内容:

- Halide在中小项目中的应用
- Halide源码阅读和分析
- Halide优化

## 项目链接

[Github Repository](https://github.com/Caktins/compiler-teamwork.git)

## 1.3 提交内容

### 成员讨论方式
* 线下图书馆组会
* QQ讨论组

### 进展情况
* 每人阅读3篇paper并记录下相关资料。
* 每人详细写一篇paper的总结，详见git中的[notes for paper](https://github.com/Caktins/compiler-teamwork/tree/master/notes%20for%20paper)
* 在论文的基础上交流讨论，了解`Halide`作为嵌在C++内的一门语言，其实际使用

### 下一步计划
* 根据论文所描述的用法，探索使用和复现的可能性
* 学习相关`Halide`的实际应用，一些具体应用来自于paper中。
* 自主尝试构建`Halide`应用



## 12.23 提交内容

### 任务分工

* 调研类：三人独立阅读相关论文，做好相关笔记，在下次组会上交流。
  阅读论文见参考资料。汪超负责1，2，3；阮超逸负责2，3，4；张航凯负责3，4，1；
  保证每篇论文至少两人看过，便于互补不足。
* 工程类：汪超负责运行halide的样例，对halide做性能测试，与经典算法做对比；阮超逸、张航凯      调研与halide有关的中型工程项目、halide内部算法优化等工作。

### 成员讨论方式
* 线下图书馆组会
* QQ讨论组

### 进展情况
* 完成对halide的基本语法了解、使用、编译工作。
* 通过阅读论文，了解halide内部机制、特性及业界对其的研究热点。

### 下一步计划
* 论文交流，深入探讨halide内部机制及特性
* 着手开始构建自己的halide应用或者内部算法优化。



## 1.13 提交内容

### 任务分工

我与汪超负责demo例子编写，展示halide用于图像处理例子；张航凯负责汇报总结部分

### 进展

* 了解halide语言特性
* 了解halide工作模式

### 成员讨论方式

线下开会讨论，交流文章。

### 参考文献

1.[**Automatically Scheduling Halide Image Processing Pipelines** ](http://graphics.cs.cmu.edu/projects/halidesched/)

[Ravi Teja Mullapudi](http://rmullapudi.bitbucket.org/) [Andrew Adams](http://people.csail.mit.edu/abadams), [Dillon Sharlet](http://www.dsharlet.com/), [Jonathan Ragan-Kelley](http://people.csail.mit.edu/jrk), [Kayvon Fatahalian](http://www.cs.cmu.edu/~kayvonf/). 
*SIGGRAPH 2016*

2.[**Decoupling Algorithms from the Organization of Computation for High Performance Image Processing**](http://people.csail.mit.edu/jrk/jrkthesis.pdf)
[Jonathan Ragan-Kelley](http://people.csail.mit.edu/jrk)
Ph.D. dissertation, MIT, May 2014.

3.[**Halide: A Language and Compiler for Optimizing Parallelism, Locality, and Recomputation in Image Processing Pipelines**](http://people.csail.mit.edu/jrk/halide-pldi13.pdf)

[Jonathan Ragan-Kelley](http://people.csail.mit.edu/jrk), [Connelly Barnes](http://www.connellybarnes.com/work/), [Andrew Adams](http://people.csail.mit.edu/abadams), [Sylvain Paris](http://people.csail.mit.edu/sparis), [Frédo Durand](http://people.csail.mit.edu/fredo), [Saman Amarasinghe](http://people.csail.mit.edu/saman). 
*PLDI 2013*

4.[**Decoupling Algorithms from Schedules for Easy Optimization of Image Processing Pipelines** ](http://people.csail.mit.edu/jrk/halide12)

[Jonathan Ragan-Kelley](http://people.csail.mit.edu/jrk), [Andrew Adams](http://people.csail.mit.edu/abadams), [Sylvain Paris](http://people.csail.mit.edu/sparis), [Marc Levoy](http://graphics.stanford.edu/~levoy), [Saman Amarasinghe](http://people.csail.mit.edu/saman), [Frédo Durand](http://people.csail.mit.edu/fredo). 
*SIGGRAPH 2012*

