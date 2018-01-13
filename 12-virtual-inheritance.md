# Virtual Inheritance

## 小组成员：

| 姓名   | Github账户  |
| ---- | --------- |
| 陈泳舟  | elvinlife |
| 刑宇   | xyyimian  |
| 庄涛   | Ubpa      |

## 项目简介：

- 单重继承，多重继承的c++实现机制，包括如何消除歧义，实现虚函数
- c++如何处理多重继承中继承格带来的问题及虚继承原理
- c++如何实现多重继承中类的构造，类的析构，及类的控制权限
- 尝试实现一个我们的从C++到C的编译器

### 项目分工：

* 陈泳舟：组内分工；c++虚继承的实现机制，对比与普通多重继承的异同，提供示例。
* 刑宇：c++单重继承，多重继承的实现机制，内存模型详解，并提供示例。
* 庄涛：调研cfront-3编译器的细节。

### 小组交流：

* qq
* 线下图书馆讨论

### 组间交流：

#### 回答问题：

* question1: 虚继承和C++直接继承有什么区别，可以简单说说吗？(07组提问)
* answer1:由于共享所以不必要在对象内存中保存多份虚基类子对象的拷贝，这样较之多继承节省空间。虚拟继承与普通继承不同的是，虚拟继承可以防止出现diamond继承时，一个派生类中同时出现了两个基类的子对象。也就是说，为了保证这一点，在虚拟继承情况下，基类子对象的布局是不同于普通继承的。因此，它需要多出一个指向基类子对象的指针。
* question2:看了看你们文档，有个疑惑，“从虚继承的基类转化为派生类则不可行”在C++中是如何解决的？（09组提问）
* answer2:https://github.com/elvinlife/virtual-inheritance/issues/5
* question3:关于《Space and time-efficient memory layout for multiple inheritance》这篇文章中的优化内存布局的三个步骤，具体而言，有哪些可能的内存和时间上优化?(14组提问）
* answer3:https://github.com/elvinlife/virtual-inheritance/issues/6

#### 提问：

* question1:原型继承语言相对类继承语言而言有何缺点呢？（提问09组）
* answer1:从设计上说，原型继承语言中的一切事物均为对象，这对让初学者感到不适应。在实现原型继承时，该语言往往得使用解释性的语言和动态弱类型系统，这两点造成了程序执行效率变低和安全性的降低。而类继承语言，则完全可以做到编译执行和静态强类型。



## 12.23 commit

### 当前进展：

* 小组所有成员看完了Bjarne Stroustrup的《Multiple Inheritance for C++》，基本上了解了C++多重继承与虚继承的机制。
* c++单重继承，多重继承的实现机制的详解，并提供示例。
* 尝试编译cfront-3，但由于版本与年代问题，目前编译还是失败，正在更改源码。

### 下一步计划：

* c++虚继承实现机制的详解，对比其与普通多重继承的异同。
* 调查c++虚继承的应用及其缺陷。
* 编译cfront-3，尝试初步实现我们的编译器。

## 1.3 commit

### 当前进展：

* c++虚继承实现机制的详解，对比了虚继承和普通继承异同。
* 调研了虚继承的优点与缺点。
* 经过努力，但是发现实现cfont-3有些困难，决定放弃

### 下一步计划：

* 详解构造函数与析构函数的原理
* 阅读论文《Space and time-efficient memory layout for multiple inheritance》，看一下具体的多继承内存空间优化
* 准备答辩

## 1.13 commit

当前进展：

* 描述了虚继承中构造和析构函数的具体原理
* 阅读论文《Space and time-efficient memory layout for multiple inheritance》，详解该论文中是如何进行虚继承存储空间优化的
* 准备答辩ppt

### 仓库链接：

https://github.com/elvinlife/virtual-inheritance

### 资料链接：

https://en.wikipedia.org/wiki/Virtual_inheritance

http://condor.depaul.edu/dmumaugh/readings/handouts/CSC548/MultipleInheritance.pdf

https://dl.acm.org/citation.cfm?id=320408