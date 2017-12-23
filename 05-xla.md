# XLA

## Project link

https://github.com/TensorflowXLABeginner/2017fall-student-teamworks

##Group Members

| Name | Github Account | ID         |
| ---- | -------------- | ---------- |
| 宋小牛  | Jeffery-Song   | PB15000301 |
| 王若冰  | MalcolmUnWang  | PB15121735 |
| 陈翊辉  | cyh-ustc       | PB15111656 |

## Introduction

**XLA** (Accelerated Linear Algebra)([github](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/compiler)) is a domain-specific compiler for linear algebra that optimizes TensorFlow computations. The results are improvements in speed, memory usage, and portability on server and mobile platforms. Users can use XLA via JIT (just-in-time) compilation or AOT (ahead-of-time) compilation.

In this project, we will do a small research on XLA, which covers in

* What kind of acceleration can XLA do
* How does XLA do it
* Where does JIT and AOT came in

##Task Assignment

### 宋小牛：Implementation of XLA, focusing on "How does XLA do it".

1. Implemented interface and architecture of XLA.
2. XLA working mechanism in TensorFlow.

### 王若冰：Performance of XLA, focusing on "What kind of acceleration can XLA do".

1. Measure the performance matrix of XLA.
2. Doing profiling with XLA and propose some possible optimization for current XLA.

### 陈翊辉：JIT and AOT in XLA, focusing on "Where does JIT and AOT came in"

1. JIT and AOT working mechanism.
2. How JIT and AOT applied in XLA and how they make the performance better.

## Discussion

### Online Discussion 

Time: 				Hard to do statistic. Approximately 3 hours.

Accomplishment:		Decide research goal and task assignment. Share study resources and documents. 

## What we have done

- [x] Discuss what will do and assign the research tasks.
- [x] Get start with TensorFlow and learning the background knowledge. 
- [x] Install TensorFlow with GPU support and start toying with the basic operation.
- [x] Learning the general concepts and implementation about XLA.

## Problems

1. **Lack experience on TensorFlow and knowledge of deep learning.** This project needs us to learning and research about XLA which is a part of TensorFlow. However, three of us have little experience with TensorFlow and deep learning, which results in lots of background knowledge to learning before we can get started on XLA.
2. **Little study resources and documents can be found about XLA.** There are, of course, huge amount of study resources about TensorFlow on the Internet. However, much of them mention little on the topic of XLA. So the learning and research of XLA in detail may need us to dig into its source code.   

## To Do

- [ ] Start testing the XLA result and performance.
- [ ] Learning the implementation of XLA in detail by viewing the source code.

## Reference

[XLA Overview](https://www.tensorflow.org/performance/xla/)

[XLA - TensorFlow 编译器](http://developers.googleblog.cn/2017/03/xla-tensorflow.html)

[XLA Source Code](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/compiler/xla)
