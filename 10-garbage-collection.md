# 项目介绍
### 1. 项目链接
#### [项目主页](https://github.com/USTC-Compiler-H-Team-10/teamwork.git)
#### ssh key 
git@github.com:USTC-Compiler-H-Team-10/teamwork.git

### 2. 成员信息
 | job  |  name  |    GitHub      |
 | ---- | ------ | -------------- |
 | 队长 | 齐炜祯 |[ qiweizhen](https://github.com/qiweizhen)      |
 | 成员 | 黄一凡 | [GhostScreaming](https://github.com/GhostScreaming) | 
 | 成员 | 金泽文 | [leo2589](https://github.com/leo2589)        |

### 3. 项目简介
本组研究的课题为“Java Garbage Collection 与各种GC算法”。
WikiPedia 对 Garbage Collection 的定义如下:

>In computer science, garbage collection (GC) is a form of automatic memory management. The garbage collector, or just collector, attempts to reclaim garbage, or memory occupied by objects that are no longer in use by the program

几乎现代编程语言都使用了动态内存分配，在内存有限的环境下，回收运行过程中不再需要的对象，重新释放内存就显得尤为重要。通常有两种回收策略：显示内存释放和自动动态内存管理。显示内存释放由程序员负责回收使用的内存，但常出现过早回收（引发悬挂指针问题）和未释放内存（引发内存泄露问题）两大错误。此外，考虑内存分配也大大提高了编程方案的复杂性。实际中，我们常使用自动动态内存管理方案。GC 则是管理中实现回收的重要步骤。

实现GC有几种经典算法，如：**标记-清除算法**——对所有堆中活动对象进行标记，把剩余没有标记的对象进行清除；**引用计数法**——每个对象记录有多少个程序在引用自己，计数为0的对象被释放；**GC复制算法**——将某个内存分配完的空间里的活动对象整理后，复制到另一个未被分配的活动对象，释放原内存的所有对象；**GC标记-压缩算法**——结合了GC标记-清除算法和复制-压缩算法，和GC标记-清除算法一样，先进行标记，然后搜索数次堆进行压缩，重新装填活动对象（不用牺牲半个堆）。

具体实现GC时，为了提升回收效率，还有**分代垃圾回收算法**——给每个对象记录年龄，优先回收容易成为垃圾的对象；**增量式垃圾回收算法**——通过逐渐推进垃圾回收来控制mutator最大暂停时间。

本次项目，我们准备了解探究GC的经典算法，每个算法实现一些实例，最后调研java语言中GC的具体实现策略。
 
### 4. 12月23日提交
**任务和分工**  

已经完成了之前制定的任务计划：调研若干个经典算法，以及JAVA中GC的算法使用情况。具体完成效果如下：  
齐炜祯：[调研GC复制算法、标记压缩法、增量式垃圾回收算法](https://github.com/USTC-Compiler-H-Team-10/teamwork/blob/master/Algotirhms.md)  
黄一凡：[调研GC标记-清除算法、引用计数法、分代垃圾回收](https://github.com/USTC-Compiler-H-Team-10/teamwork/blob/master/Algorithm%20by%20Fan.md)  
金泽文：[调研JVM中GC算法的使用](https://github.com/USTC-Compiler-H-Team-10/teamwork/blob/master/notes_for_JVM.md)

**讨论记录**  
#### 12.23
QQ群: 30分钟 + 图书馆四楼讨论区: 40分钟  
第一阶段的任务已经完成；  
分享各自学习心得；  
讨论制定接下来的目标和计划
#### 12.14
QQ群: 40分钟  
交流了各自找到的资料；具体分配任务。
#### 12.13
QQ群: 40分钟  
确定课题，开始准备。  

**进展记录及问题**

第一阶段就完成了项目简介中计划的内容；调研成果在任务分工中已经给出了链接。因此商讨下一步的研究方向。现在遇到的问题是后面的工作需要重新指定，现在确定了若干个有可能进行的希望，但是暂时不能完全确定。

**下一步的计划**  

因为前面指定的计划（探索经典GC算法）已经被完成掉了，因此商讨出下面探索的方向，并会在进一步探索后具体确定。  
探索方向：  
1. 尝试探索JVM源码，分配任务阅读JVM的GC源码；
2. 如果有可能，在探索JVM后，确定造JVM的小轮子或者改写or实现JVM中GC部分的难度和可行性。
3. 探索现在最前沿的GC算法，阅读新发表的论文。
4. 对C语言的malloc函数进行封装，并实现GC函数，为C语言提供垃圾回收机制。  
**后面的任务将会探索以上四个方向，并选择最合适的方向进行。**

**文献及引用和参考链接**  
若干GC分析博客  
[《垃圾回收的算法与实现》 【日】 中村成洋 相川光](https://www.amazon.cn/dp/B01JZS0AO8 )  
[JVM的GC相关内容](https://javapapers.com/java/how-java-garbage-collection-works)
