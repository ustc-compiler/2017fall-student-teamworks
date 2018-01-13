## Team 13-NNVM Compiler

### 小组成员:

| 组员   | GitHub 账号及链接                             |
| ---- | ---------------------------------------- |
| 朱一铭  | [suncio](https://github.com/suncio)      |
| 谢筠庭  | [MiroBamboo](https://github.com/MiroBamboo) |
| 林郅琦  | [ralzq01](https://github.com/ralzq01)    |

### 项目简介：
* NNVM 编译器是用于中间计算图表示和优化计算图的一种工具，建立在 TVM 堆栈的两个组成的基础上：用于计算图的 NNVM (狭义 NNVM)，和用于张量计算的 TVM。
* 此次调研项目目的为熟悉 NNVM 编译器的基本原理，了解 NNVM 编译器的特性和功能，并与传统编译器、同类性质工具（如 XLA 等）进行对比，具体安排情况如下：
  * 编译运行成功运行 NNVM 编译器，并能够针对 CPU 硬件资源产生关于 llvm 的代码表示。
  * 熟悉 NNVM 和 TVM 的基本特性，运用 NNVM 和 TVM 的的接口观察 NNVM 编译器的行为（如自定义运算符、自定义优化策略等）。
  * 了解 NNVM 编译器用于计算图优化的基本策略。
  * 时间和资源允许的情况下，比较 NNVM 编译器在针对 CPU 所做的优化和 GPU 所做的优化的不同点。
  * 与传统编译器、同类性质工具（如 XLA 等）进行比较。

### 仓库链接
Team 13 项目仓库： [team-13-repository](https://github.com/USTC-compiler-2017fall-group13/13-NNVM)

NNVM Compiler 项目仓库：[nnvm-git-repository](https://github.com/dmlc/nnvm)

### 当前进展（12.23）
* 了解 nnvm 的基本功能和作用                         
* 了解 tvm 的基本功能和作用                          
* 了解 nnvm compiler 执行基本流程                    
* 成功编译 nnvm compiler                            
* 完成 nnvm compiler 生成目标 cpu，llvm 的简单示例     
* 完成向 nnvm compiler 注册自定义函数的简单示例        
* 以上所完成的工作已经编写文档放置于项目仓库的 docs/ 和 test-bench/ 目录下

### 进展 (1.3)
* 正在联系作者了解关于对计算图优化的具体流程
* tvm 介绍文档介绍补充
* nnvm 计算图优化调研（由于 nnvm compiler 文档没有给出具体的图优化的介绍，正在从源码层面并结合典型优化方法进行调研）
* 优化示例（test-bench 中）

### 进展(1.13)

* 了解 nnvm 和 tvm 针对 cpu 和 gpu 所做的优化工作
* 了解 nnvm 高级图表示到 tvm 中间代码IR 生成的大致策略
* 与 XLA 小组 & Darkromm 小组进行讨论并得出框架对比结论
* 发布 gitbooks [最终报告](https://ustc-compiler-2017fall-group13.gitbooks.io/ustc-compiler-2017fall-group13/content/)版本
* 制作 representation

### 最终报告

*  [最终报告](https://ustc-compiler-2017fall-group13.gitbooks.io/ustc-compiler-2017fall-group13/content/)

### Reference
* [NNVM Compiler 整体知识了解](https://www.jiqizhixin.com/articles/2017-10-07-4)
  * 这篇文章介绍了 NNVM Compiler 的基本架构，他的一些特性和性能
* [NNVM 整体知识了解](http://nnvm.tvmlang.org/dev/index.html)
  * 官方文档，介绍了 NNVM 设计的核心特性
* [TVM 整体知识了解](http://docs.tvmlang.org/dev/index.html)
  * 官方文档，介绍了 TVM 设计的核心特性
* [NNVM 到 LLVM 目标代码生成](http://nnvm.tvmlang.org/tutorials/get_started.html#sphx-glr-tutorials-get-started-py)
  * 仓库代码改编自此 tutorial，初步了解 NNVM 生成 LLVM CPU 目标代码的流程
* [向 TVM 注册自定义函数](http://docs.tvmlang.org/dev/runtime.html#packedfunc)
  * 尝试 TVM 的核心特性之一，官方文档上没有给出具体如何完成自定义函数的注册，已经通过尝试并解决，解决方案在仓库 test-bench/def_func/ 目录下
* [NNVM Compiler 编译安装](http://nnvm.tvmlang.org/how_to/install.html)
  * 按照官方文档一步步编译即可，注意需要 llvm 的支持，仓库 docs/ 下有具体的中文编译过程