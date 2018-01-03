# XLA

## Project link

Detailed Reports are included in our [XLA-Report repository](https://github.com/TensorflowXLABeginner/XLA-Report).

## Group Members

| Name | Github Account | ID         |
| ---- | -------------- | ---------- |
| 宋小牛  | Jeffery-Song   | PB15000301 |
| 王若冰  | MalcolmUnWang  | PB15121735 |
| 陈翊辉  | cyh-ustc       | PB15111656 |

## Introduction

**XLA** (Accelerated Linear Algebra)([Github](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/compiler)) is a domain-specific compiler for linear algebra that optimizes TensorFlow computations. The results are improvements in speed, memory usage, and portability on server and mobile platforms. Users can use XLA via JIT (just-in-time) compilation or AOT (ahead-of-time) compilation.

In this project, we will do a small research on XLA, which covers in

* What kind of acceleration can XLA do
* How does XLA do it
* Where does JIT and AOT came in

## Task Assignment

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

Time: 				

- Hard to do statistic. Approximately 3 hours.

Accomplishment:		

- Decide research goal and task assignment. 
- Share study resources and documents. 

## What we have done

### 12.23 Commit

- [x] Discussed what will do and assign the research tasks.
- [x] Get start with TensorFlow and learning the background knowledge. We have wrote a report for [TensorFlow Programming](https://github.com/TensorflowXLABeginner/XLA-Report/blob/master/FirstCommitReports/Accelerated%20Linear%20Algebra%20Intro.md).
- [x] Installed TensorFlow with GPU support and start toying with the basic operation.
- [x] Learned the general concepts and implementation about XLA. We have wrote two report individually for [XLA Overview](https://github.com/TensorflowXLABeginner/XLA-Report/blob/master/FirstCommitReports/Accelerated%20Linear%20Algebra%20Intro.md) and [XLA Just-in-time Compilation](https://github.com/TensorflowXLABeginner/XLA-Report/blob/master/FirstCommitReports/xla_Just-in-time%20compilation.md).

### 1.3 Commit

- [x] Compiled TensorFlow from source since XLA can only be included when TensorFlow is compiled from source.
- [x] Turned on JIT compilation to include XLA and run some optimized example.
- [x] Did some basic profiling with CUDA Profiling Tools Interface (CUPTI).
- [x] Report the test and profiling we have done in the [repository](https://github.com/TensorflowXLABeginner/XLA-Report/tree/master/SecondCommitReports).

## Problems

1. **Lack experience on TensorFlow and knowledge of deep learning.** This project needs us to learning and research about XLA which is a part of TensorFlow. However, three of us have little experience with TensorFlow and deep learning, which results in lots of background knowledge to learning before we can get started on XLA.
2. **Little study resources and documents can be found about XLA.** There are, of course, huge amount of study resources about TensorFlow on the Internet. However, much of them mention little on the topic of XLA. So the learning and research of XLA in detail may need us to dig into its source code.   

## To Do

### 12.23 Commit

- [ ] Start testing the XLA result and performance.
- [ ] Learning the implementation of XLA in detail by viewing the source code.

### 1.3 Commit

- [ ] Do some benchmarks in more details.
- [ ] Test and using profiling tools to do profiling.
- [ ] Lots of idea will come out after we have done the job above, try to implement the ideas.

## Reference

[TensorFlow: Getting Started](https://www.tensorflow.org/get_started/)

[Deep learning with Tensorflow](https://www.packtpub.com/mapt/book/big_data_and_business_intelligence/9781786469786/9/ch09lvl1sec82/accelerated-linear-algebra)

[XLA Overview](https://www.tensorflow.org/performance/xla/)

[XLA - TensorFlow 编译器](http://developers.googleblog.cn/2017/03/xla-tensorflow.html)

[XLA Source Code](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/compiler/xla)
