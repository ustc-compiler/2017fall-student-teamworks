# Team 03 Smart Pointers

## Members

| Name | Student ID | Github ID  |
| ---- | ---------- | ---------- |
| 王若晖  | PB15000142 | noirgif    |
| 张一卓  | PB15111610 | eastOffice |
| 钱劲翔  | PB15151800 | Qianjx     |

## Content

智能指针是一种模拟指针的行为，但提供如自动内存管理功能的抽象数据类型。它对普通指针加了一层封装机制，其目的是为了使得智能指针可以方便的管理一个对象的生命期。正确使用智能指针，可以方便的防止指针的悬空引用，内存泄漏等问题。

本次项目尝试从C++的智能指针入手，探索并讨论如下内容：

* [raw pointer 在应用中可能产生的问题](https://github.com/noirgif/ustc-compiler-pointer/blob/master/cpp-raw-pointer-problem.md)
* [C++ 中 smart pointer 的标准，实现方式和内存管理](https://github.com/noirgif/ustc-compiler-pointer/blob/master/cpp-smart-pointer.md)
* [Rust 语言中的智能指针及其内存管理](https://github.com/noirgif/ustc-compiler-pointer/blob/master/rust-smart-pointer.md)
* smart pointer 在项目中的案例分析

## 分工

* 王若晖： 
  * Rust 语言中的智能指针及其内存管理
* 张一卓： 
  * C++ 中 smart pointer 的标准，实现方式和内存管理
  * C++ smart pointer 的简单实现
* 钱劲翔： 
  * raw pointer 在应用中可能产生的问题
  * C++ 标准库以及 boost库中部分 smart pointers 的分析

## 第一次提交

### 提交内容

王若晖:

* 阅读Rust文档，完成Rust中Box和Rc的部分描述。

张一卓:

* 阅读了C++智能指针的大部分源码，寻找参考文献
* 结合源码总结了 `std::auto_ptr` 的使用方式，源码的策略，以及引入了 RAII 的概念
* 完成`std::auto_ptr`部分的编写

钱劲翔:

* 对C/C++中raw pointer部分问题的描述

### 下一步计划

* 继续结合源码，添加`std::unique_ptr`, `std::shared_ptr` 的分析
* 调研 C++ 标准库以外的智能指针，主要是 boost 库
* 完成`Rc<T>`和`RefCell<T>`的描述，和其内存管理
* 考虑自己实现一个基于计数与不基于计数的 C++ 智能指针
* 加强讨论，与 GC 组交流一下

## 第二次提交

### 提交内容

王若晖:

张一卓：

- 继续结合源码，分析了`std::unique_ptr`和`std::weak_ptr`的使用方式和实现机制，并编写了一些示例程序
- 补充文档，见 [cpp-smart-pointer.md](https://github.com/noirgif/ustc-compiler-pointer/blob/master/cpp-smart-pointer.md)

钱劲翔:

- 结合源码分析了`std::shared_ptr`的使用和实现，补充了文档[cpp_smart_pointer.md](https://github.com/noirgif/ustc-compiler-pointer/blob/master/cpp-smart-pointer.md)
- 调研了`boost`库中的一些智能指针，介绍了它们的特点，编写示例程序说明使用方式，文档见 [boost-smart-pointer.md](https://github.com/noirgif/ustc-compiler-pointer/blob/master/boost-smart-pointers.md)

### 下一步计划

- 完成 C++ 智能指针的简单实现
- 整理完善所写的文档
- 与 GC 组讨论，互提 issue

## Links

[Teamwork Repository](https://github.com/noirgif/ustc-compiler-pointer)

C++ source code of smart pointers：

[auto_ptr](https://github.com/noirgif/ustc-compiler-pointer/blob/master/References/source_auto_ptr.cpp), [unique_ptr](https://github.com/noirgif/ustc-compiler-pointer/blob/master/References/source_unique_ptr.cpp), [shared_ptr](https://github.com/noirgif/ustc-compiler-pointer/blob/master/References/source_shared_ptr.cpp), [weak_ptr](https://github.com/noirgif/ustc-compiler-pointer/blob/master/References/source_weak_ptr.cpp)

[ICSE2016-SERVO](https://github.com/noirgif/ustc-compiler-pointer/blob/master/References/icse16-servo-preprint.pdf)

[Rust doc](https://doc.rust-lang.org/book/second-edition/)

