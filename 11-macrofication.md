# Team 11-Marcofication

这是一个有关于在JavaScript使用的Marcofication的项目；

## Members
|     姓名      | 学号		    |            Github       						 	         | 职务 |
|:-------------:|:-------------:|:----------------------------------------------------------:|:-----:|
| 	余浩       |PB15000372| [difftime](https://github.com/difftime)     	|队长|
| 	周祺       |PB15050988| [ZhouQida](https://github.com/ZhouQida) 	    |队员|
|   李强	     |PB15111612| [PB15111612](https://github.com/PB15111612)   |队员|

## Introduction
Macrofication是运行在JavaScript语言中的一种新颖的重构过程，对于每一个pattern-template宏，他自动生成一个相应的重构工具，用于查找与宏模板相匹配的复杂片断，并用更简单的宏调用模式来替换他们；

Macrofication灵活性好，可扩展性强，在这里我们将深入研究其原理，探究其实现方式和编程模型，同时调研类似的工作和实现技术。

## 12.23 commit
### 项目分工
重构代码的实验部分，每个队员都需要亲自安装实验;每人分别总结Macrofication中的一部分，余浩负责Introduction和Macro expansion部分，李强负责Refactoring Correctness和Repetitions in Patterns部分，周祺负责Related Work和Future Work and Conclusions部分;未来工作将具体再安排分工。
### 目前进展
1.关于sweet.js的安装与实验已经基本完成，并且总结了安装及运行过程，可见[文档](https://github.com/ustc-compiler-macrofication/macrofication/blob/master/docs/getting_started.md)。
2.各队员对于Macrofication的总结工作已经完成，具体如下：

|负责人     |           名称   		      |github位置                                                                                                           |
|:--------:|:---------------------------:|:-------------------------------------------------------------------------------------------------------------------:|
|余浩       |Introduction                 |[文档](https://github.com/ustc-compiler-macrofication/macrofication/blob/master/docs/Introduction.md)                |
|余浩       |Macro expansion              |[文档](https://github.com/ustc-compiler-macrofication/macrofication/blob/master/docs/Macro_expansion.md)             |
|李强       |Refactoring Correctness      |[文档](https://github.com/ustc-compiler-macrofication/macrofication/blob/master/docs/Refactoring%20Correctness.md)   |
|李强       |Repetitions in patterns      |[文档](https://github.com/ustc-compiler-macrofication/macrofication/blob/master/docs/Repetitions%20in%20Patterns.md) |
|周祺       |Related Work                 |[文档](https://github.com/ustc-compiler-macrofication/macrofication/blob/master/docs/Related%20Work.md)              |
|周祺       |Future Work and Conclusions  |[文档](https://github.com/ustc-compiler-macrofication/macrofication/blob/master/docs/Future_Work_and_Conclusions.md) |

### 讨论方式
每周三在图书馆共同讨论一周进展，谈论时长约1-2个小时，另外，建立qq讨论组，随时有问题可以线上沟通与讨论。
### 下一步计划
按照工作要求调研与Macrofication类似的工作以及实现技术。

## Links
[Macrofication](https://users.soe.ucsc.edu/~cormac/papers/16esop.pdf) 

[sweetjs](https://www.sweetjs.org/doc/tutorial) 

[sweet.js-tutorials](https://github.com/jlongster/sweet.js-tutorials) 

[backbone.js](http://backbonejs.org/) 
