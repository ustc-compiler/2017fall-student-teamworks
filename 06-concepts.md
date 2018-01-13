# concepts

成员：

|职务|姓名|Github 账户|
|:-:|:-:|:-:|
|队长|李嘉豪|gloit042|
|队员|袁牧|Alexyuanmu|
|队员|毕昊阳|AyiStar|

## 简介

本项目是2017年秋季学期编译原理(H)课程小组作业，项目的主要研究对象是
C++的一个扩展: concepts。项目的主要内容包括:
- [concepts简介](https://github.com/ustc-compiler-concepts/report/blob/master/concepts-intro.md)
- [基于模板元编程的concepts实现](https://github.com/ustc-compiler-concepts/report/blob/master/concepts-by-TMP.md)
- [Haskell中的type class](https://github.com/ustc-compiler-concepts/report/blob/master/type-class-in-haskell.md)
- [concepts作为编程范式](https://github.com/ustc-compiler-concepts/report/blob/master/concepts-in-generic-programming.md)

## 项目分工

*   李嘉豪: concepts应用、文档整理与综合
*   袁牧: concepts实现机制
*   毕昊阳: 模板元编程实现、concepts和其他语言对比

## 小组交流

### 第三组

1.	给第三组成员提出了[建议](https://github.com/noirgif/ustc-compiler-pointer/issues/1)

2.	在第三组成员的提醒下，修正了文档中示例代码的一些[错误](https://github.com/ustc-compiler-concepts/report/issues/3)

### 第七组

问了我们两个问题

Q1: concepts使用时有遇到过什么问题

A1: concepts的取名要有一定的意义，所以相似的concepts要取不一样的名字会比较麻烦。
除此之外使用起来并不麻烦

Q2: 在concepts的设计方面，你们有没有觉得什么可以改进的

A2: 1.缩写形式的Concepts感觉并没有优雅地融入语言之中，但是想想也没有什么比较好的替代方式。
2.`requires`同时有定义和使用的功能，感觉不太一致

我们也向第七组提了一些问题

## 进展

#### 总体进展

在这段时间里，我们基本上完成了对concepts的研究，并编写了文档。

首先，我们完整地阅读了concepts的技术报告，对concepts的基本概念和形式有了了解，并做了一份[concepts简介](https://github.com/ustc-compiler-concepts/report/blob/master/concepts-intro.md)。

在这之后，我们探究了C++语言中的模板能否实现concepts的语义，并证明了基于模板元编程我们可以实现大部分concepts的功能，完整的说明见[基于模板元编程的concepts实现](https://github.com/ustc-compiler-concepts/report/blob/master/concepts-by-TMP.md)。

横向上，我们在[Haskell中的type class](https://github.com/ustc-compiler-concepts/report/blob/master/type-class-in-haskell.md)中将concepts与Haskell语言中的类似概念type class进行比较，说明concepts在泛型编程中的出现并不是偶然。

最后，我们在[concepts作为编程范式](https://github.com/ustc-compiler-concepts/report/blob/master/concepts-in-generic-programming.md)中讨论了concepts出现后可以应用的编程范式，以及它所带来的便利。

接下来我们会整理现有的报告，制作出一份小组报告时用的精简版，为最后的报告准备。
我们会继续同其它组的成员互相交流和评价，以便进一步完善报告。
也欢迎各位同学用任何方式来提出改进意见。

#### 1月13日

最终报告编写完成，编译成`HTML`

#### 1月3日

在第三组成员的提示下，修正了文档中示例代码的一些[错误](https://github.com/ustc-compiler-concepts/report/issues/3)

#### 1月1日

同其第三组组员进行了交流，并交换了意见
地点：线上
时间：半小时

#### 12月30日

听从助教意见，调研了一下C++中的traits(萃取器)，感觉关系并没其它内容那样联系紧密，遂未写入报告

#### 12月23日

改进了公共页面的说明

#### 12月15日

给第三组成员提出了[建议](https://github.com/noirgif/ustc-compiler-pointer/issues/1)

#### 12月7日

讨论组里进行了讨论，大家都基本完成了学习任务，并认为可以开始文档编写，
于是在github上建立了组织。在此之后就进行了文档编写。

#### 11月2日

课后进行了讨论。每个人都分享了自己对concepts的了解，然后分享了找到的资料。
讨论中，我们还得出了报告需要关注的一些重点，确定接下来以这些重点为中心进行
更进一步的了解。

#### 10月12日

课后进行了讨论，确定了学习计划，并确定了分工。

## 项目链接

https://github.com/ustc-compiler-concepts/report

