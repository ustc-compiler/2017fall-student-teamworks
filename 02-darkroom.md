# Team 02-Darkroom
## Members
 Name   | identity| ID        | github                                                                                    
|----   |--------   |----      |------                                                                                    
|施泽丰 | 组员 | PB14210224 | [shiuang](https://github.com/orgs/Compiler-02/people/shiuang)                              
|钟  立 | 组长 | PB15000037 | [FloridSleeves](https://github.com/orgs/Compiler-02/people/FloridSleeves)                 
|郭振江 | 组员 | PB15030776 | [ExquisiteFunction](https://github.com/ExquisiteFunction/darkroom/commits/master/report.md?author=ExquisiteFunction)

## Introduction
Darkroom is a language and compiler for image processing embedded in Terra. It allows to compile program directly into line-buffered pipelines, with all intermediate values in local line-buffer sotrage.

Our group dive into the principle of Darkroom, doing research on the programming model of Darkroom and the strategy of Darkroom to optimize the performance of program in ASIC, FPGA and CPU. 

## Task  
### 施泽丰

 **Programming model** of Darkroom including pipeline buffer,shift operator...

 **Schedule strategy** of Darkroom

### 钟立

 The former **related work**: Halide,DSP,SDF...
 
 The **comparison** of former work and Darkroom

 **Background knowledge**:ISP, FPGA...

### 郭振江

 **Implementation** of Darkroom on ASIC, FPGA and CPU

 The **output** of Darkroom implementation

 Optimization **result**

### Common Task

Install and run the example of darkroom

Read the related publication to get the basic concepts of Darkroom.

## Discussion

* 10.12

 Discussion on the topic

* 11.28

 Installation problem discussion

* 12.09

 Division of team work
 
* Total

1-2h, mostly online
 
## Progress
**10.07-10.12**

  Choose the research topic

**10.12-11.28**

  Install Darkroom and the dependencies(lua,terra，llvm...)

  Read the related publication.

**12.09-12.23**

  Report writing

  Materials collection

**Updated on 12.23**

Now we have know the working process of Darkroom, and get to know the background knowledge, the related work and the major technology and strategy in Darkroom. We run the example, and test some simple, small dataset in Darkroom to get the direct sense of the function and performance of Darkroom on CPU. Besides, we get useful information from the related publication, so that we can see how Darkroom works so fast and the innovation of Darkroom.

## TODO List
* More materials collection for a better understanding
* Read the source code to get a rough sense of the implementation of Darkroom
* The comparison to Halide and other similiar language

## Problem
1. We are not familiar with lua, which Darkroom is implemented with.

2. The FPGA implementation is not available for us because of the lack of hardware support.

## Links
[Darkroom: Compiling High-Level Image Processing Code into Hardware Pipelines](http://darkroom-lang.org/darkroom14-low.pdf)

[Darkroom](http://darkroom-lang.org/)

**To see our current progress**

[Github Repository](https://github.com/Compiler-02)
