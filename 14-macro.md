# 14 Teamwork -- Macro

## 项目地址 
[https://github.com/Robert-Lu/teamwork-14-Macro](https://github.com/Robert-Lu/teamwork-14-Macro)

## 组员（Github ID)

* 鲁吴越（[Robert-Lu](https://github.com/Robert-Lu)）
* 李双利（[agave233](https://github.com/agave233)）
* 罗永平（[ypluo](https://github.com/ypluo)）

## 项目简介

本项目主要研究各种宏的特点与优缺点，包括词法级别与语法级别的宏的调研，以及普通宏与 hygienic macro 的区别。

具体而言，本项目会

1. 首先对词法级别的宏做一个简单的总结，以大家熟知的 C 语言作为实例，由于词法级别的宏具有的特性较少，功能局限性也较多，对这一块不做过多的阐述；
2. 对于语法级别的宏，我们计划对 Lisp 和 Rust 的宏进行分析，这两种语言分别是较传统以及较新式的语言，对于他们之间的区别，Lisp 宏中存在的问题，以及新式语言设计中是如何解决这些问题的，进行调研和总结；
3. 对于 hygienic macro 相关问题的调研，可以穿插前两点中 C 语言和 Lisp 语言中宏存在的卫生性问题来进行解读；

## 任务和分工

将任务分为以下模块：

* 词法级别的宏 
  a. 总结 C 语言的宏的特性 
  b. 总结 C 语言的宏的局限性
  c. 结合宏的卫生性讨论
* 语法级别的宏
  d. 调研 Lisp 宏的特性
  e. 调研 Rust 宏的特性
  f. 比较两者以及总结宏机制在程序语言中的发展
  g. 结合宏的卫生性讨论
* hygienic macro 相关
  h. 完成宏的卫生性问题的简介
  i. 相关学术文献的阅读与调研
  j. 调研卫生宏的特点以及其与普通宏的区别
* 可选
  h. 在 `c1i` 项目基础上编写代码，来实现一些宏的高级特性。

经过组内讨论，以上问题部分是相对独立的，也有部分是 