# Team 01 - [Loo.py](https://github.com/01-Loopy/loo.py-intro)

## 成员

姓名 | 学号         | GitHub用户名
---- | ----------- | ------
何宪航 | PB14011082 | [hangGit](https://github.com/orgs/01-Loopy/people/hangGit)
范子健 | PB14209127 | [Fanzijian1996](https://github.com/orgs/01-Loopy/people/Fanzijian1996)
韦清   | PB15000027 | [wwqqqqq](https://github.com/orgs/01-Loopy/people/wwqqqqq)

## 简介

Loo.py是一个内嵌于Python的编程系统，包含基于数组等数据模型的计算以及面向CUDA/OpenCL的代码生成。

传统的编译器一般会在保证执行结果不变的前提下，基于语言的内存模型对用户代码进行优化重写。而相应的代价就是较为复杂的优化方案在稳健性和性能方面注定存在一定程度的取舍。而Loo.py则保留了源代码的语义，主要通过Loo.py提供的转换库生成目标代码。因此，Loo.py的主要优点包括：

- 用户可自行检查修改代码的中间表现形式，并且通过自定义的转换进一步提高效率或扩展现有的转换库；
- 显式的代码转换更为灵活，可以完成更多的底层优化，并且和编译器的重写相比更容易证明其正确性；
- 内嵌于宿主语言提供了对于转换的全面控制，和简单的编译制导语句（如OpenMP）相比能够根据工作量进行运行时调整；
- 宿主语言的高层环境便于代码重用以及抽象；

事实上，抽象语法树(AST)作为常见的编译器中间表示并不适合复杂的程序优化。[多面体模型](https://dl.acm.org/citation.cfm?id=1025992)作为AST的改进，适合表示串行以及并行程序。基于多面体模型的编译器从抽象语法树开始对程序进行分析和变换，然后找到新的代码执行顺序。而目前的研究瓶颈主要在于现有算法难以找到合适的代码执行顺序。相比之下，Loo.py要求用户在宿主语言中采取基于多面体模型的方式具体描述计算模型。用户定义的计算模型被存储在宿主语言的对象中（如loopy kernel，类似于tensorflow session），而代码之间仅存在偏序关系，以便于代码生成器进行深度优化。

因此，Loo.py对于向量化操作、循环展开以及指令级并行均有较好的支持，其应用主要针对基于数组且控制流中数据依赖较少的循环代码，例如：稀疏矩阵乘法、迭代收敛等。此外，Loo.py和PyCUDA以及PyOpenCL深度集成，便于快速将计算模型转换为低层次、高性能代码实现。

具体介绍文档请参考此项目的 [GitHub repository](https://github.com/01-Loopy/loo.py-intro)。

## 研究任务以及分工

### 韦清：

- Loo.py编程系统的实现方式

结合论文以及代码具体说明介绍Loo.py完整的实现方式

Loo.py和一般的代码生成器的主要区别

Loo.py与传统编译器的比较以及优劣分析

- 多面体模型分析

多面体模型如何表示程序

多面体模型和抽象语法树的对比

应用场景

基于示例说明多面体模型和Loo.py中kernel的语句如何对应

### 何宪航：

- Loo.py的示例实现

使用Loo.py编写测试样例；如矩阵乘法、LU分解等

与Numpy的实现进行对比

测试样例基于PyOpenCL的GPU实现

### 范子健：

- Loo.py在TVM中的应用

TVM简介

结合源代码分析Loo.py对于TVM的影响

- 加速比量化分析

发布包含Loo.py以及测试样例的Docker容器

在单核、多核以及GPU等平台上进行测试

分析加速比

## 讨论记录

### 12.20

地点：西区图书馆；15分钟

讨论项目内容的重点和具体需要完成的任务，计划在下次讨论时确定每个人的分工以及任务需要完成到什么程度。
熟悉基于版本控制工具的协作。


### 12.22

地点：西区图书馆/在线；15分钟/3小时

确定个人分工，针对分工的任务制定提纲；讨论完成所需技能以及学习规划。

### 12.27

地点：线上；15分钟

总结进度，相互进行文档和代码评议


## 进展记录

### 12.13

添加项目简介，完成初次提交。

### 12.20

深入讨论项目内容，具体列出任务规划

### 12.22

确定分工，制定任务提纲

### 12.23

初步完成项目大纲，完成第二次提交。

### 12.27

针对进度和规划进行分析，互相检查文档，代码需要经过他人评议后再并入主分支

### 1.3

梳理调研结果，完成第三次提交

## 问题记录

- 多面体模型的具体解释以及示例

- 总结互相进行代码评议的规范

## 待办清单

- [x] 阅读参考文献并讨论

- [x] 分析组员熟悉和擅长的方向，确定具体分工

- [x] 安装Python以及Loo.py的相关包

- [x] 汇总各自调研信息

- [ ] 相互进行文档和代码评议

- [ ] 根据组员评价进行修改

## 引用

[Loo.py: transformation-based code generation for GPUs and CPUs](https://arxiv.org/abs/1405.7470)

[TVM: Tensor IR Stack for DL](https://github.com/dmlc/tvm)

## 相关链接

[此项目的 GitHub repository](https://github.com/01-Loopy/loo.py-intro)

[Docker example]() Work in progress

[Official Loo.py git repository](https://github.com/inducer/loopy)

[Documentation for Loo.py](https://documen.tician.de/loopy/)
