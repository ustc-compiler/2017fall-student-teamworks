# Team 01 - Loopy

## 成员

姓名 | 学号
--------- | --------
[何宪航](https://github.com/orgs/01-Loopy/people/hangGit)| PB14011082
[范子健](https://github.com/orgs/01-Loopy/people/Fanzijian1996)| PB14209127
[韦清](https://github.com/orgs/01-Loopy/people/wwqqqqq) |  PB15000027

## 简介

Loo.py是一个内嵌于Python的编程系统，包含基于数组等数据模型的计算以及面向CUDA/OpenCL的代码生成。

传统的编译器往往通过重写用户代码的方式完成优化，而相应的代价就是较为复杂的优化方案在稳健性和性能方面注定存在一定程度的取舍。而Loo.py则要求用户在宿主语言（包括但不限于Python）中声明基于多面体的计算模型，而代码之前仅存在偏序关系，以便于代码生成器进行深度优化。

因此，Loo.py对于向量化操作、循环展开以及指令级并行均有较好的支持。此外，Loo.py和numpy以及PyOpenCL深度集成，便于快速将计算模型转换为高效代码实现。

## 研究内容

- Loo.py编程系统的实现方式

- Loo.py在TVM中的应用

- Loo.py的实例实现

- 加速比量化分析

## 链接

[Loo.py: transformation-based code generation for GPUs and CPUs](https://arxiv.org/abs/1405.7470)

[GitHub repository](https://github.com/01-Loopy/2017fall-student-teamworks)

[Docker example]() Work in progress