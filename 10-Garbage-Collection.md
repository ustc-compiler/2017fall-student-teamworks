# 项目介绍
### 1. 项目链接
#### [项目主页](https://github.com/USTC-Compiler-H-Team-10/teamwork.git)<br>
#### ssh key 
git@github.com:USTC-Compiler-H-Team-10/teamwork.git

### 2. 成员信息
 | job  |  name  |    GitHub      |
 | ---- | ------ | -------------- |
 | 队长 | 齐炜祯 | qiweizhen      |
 | 成员 | 黄一凡 | GhostScreaming | 
 | 成员 | 金泽文 | leo2589        |

### 3. 项目简介
&emsp;&emsp;本组研究的课题为“Java Garbage Collection 与各种GC算法”。<br>
&emsp;&emsp;WikiPedia 对 Garbage Collection 的定义如下:

>In computer science, garbage collection (GC) is a form of automatic memory management. The garbage collector, or just collector, attempts to reclaim garbage, or memory occupied by objects that are no longer in use by the program

&emsp;&emsp;几乎现代编程语言都使用了动态内存分配，在内存有限的环境下，回收运行过程中不再需要的对象，重新释放内存就显得尤为重要。通常有两种回收策略：显示内存释放和自动动态内存管理。显示内存释放由程序员负责回收使用的内存，但常出现过早回收（引发悬挂指针问题）和未释放内存（引发内存泄露问题）两大错误。此外，考虑内存分配也大大提高了编程方案的复杂性。实际中，我们常使用自动动态内存管理方案。GC 则是管理中实现回收的重要步骤。
 
&emsp;&emsp;学习GC相关的若干算法：GC标记-清除法，引用计数法，GC复制算法，GC标记-压缩算法，保守式GC，分代垃圾回收，增量式垃圾回收，RC IMmix算法等等，尝试编写代码体验简单的GC操作，展望是学习现在最新的GC信息，或者找到GC算法中不足和可以改进的地方。