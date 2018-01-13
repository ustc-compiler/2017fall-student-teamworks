# Team 02-Darkroom
## Members
|Name   | identity| ID        | github                                                                                    
|----|--------|----|------                                                                                    
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
 
* 01.01

 Decide the group and the topic to discussion

 * 01.13
 
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

**12.23**

Now we have know the working process of Darkroom, and get to know the background knowledge, the related work and the major technology and strategy in Darkroom. We run the example, and test some simple, small dataset in Darkroom to get the direct sense of the function and performance of Darkroom on CPU. Besides, we get useful information from the related publication, so that we can see how Darkroom works so fast and the innovation of Darkroom.

**12.23-1.3**

 Halide research
 
 Image pyramid research
 
 NNVM research

**1.3**

We get to know that Darkroom can not implement image pyramid(and some other image processing algorithms) currently, which is a point for us to research into. We find that Halide, a language designed to write high-performance image processing code, is able to deal with image pyramid. This prompts us to compare these two language, and to find out the reason why Halide can implement image pyramid, and why Darkroom cannot so that we can have a deeper understanding on the limitation of Darkroom programming model.

Besides, we are interested in the way NNVM applies the principle of Darkroom. So we research on the information about NNVM, to find out the relation between NNVM and Darkroom. 

The two questions above are the topics we are going to discussion with the other two groups working on them. 

With a quick look on the source code, we find the part of implementation on scheduling and optimization.  

**1.3-1.13**

Discussed with Halide group(E1) and NNVM group(E4) 

Test on Halide and Darkroom

Read source code

Comparison between NNVM and Darkroom


**Updated on 1.13**

We discussed with other groups to get information on Halide and NNVM. Then we compare Halide and Darkroom from many aspects to get the differences between them. We read through the source code and finally get the details of Darkroom. We experimented on Halide and NNVM, and measured the time consumed for a comparison. By intergroup discussion, we realized the general principle in language designing.

## TODO List
- [x] More materials collection for a better understanding
- [x] Halide research
- [x] NNVM research
- [x] Read the source code to get a rough sense of the implementation of Darkroom
- [x] The comparison to Halide and other similiar language
- [x] The application of Darkroom principle in NNVM
- [x] A closer look on the implementation of Darkroom optimization and scheduling.


## Problem and Solution
1. We are not familiar with lua, which Darkroom is implemented with.

Ignore the trivial, but get the main idea of Darkroom.

2. The FPGA implementation is not available for us because of the lack of hardware support.

We choose CPU as the test platform because Darkroom optimization is available on CPU.

**Summary**

In our teamwork, we start from Darkroom, read the publications and then run examples on CPU platform. Next, we skip the source code, find the point to discussion and research deeply on. Then, we discussion with outher groups, do experiment to get the straightforward comparison, and read the source code to understand the implementation of Darkroom. Finally, we not only get to know the Darkroom principle, but also make sense of the general principle of language designing.

## Links
[Darkroom: Compiling High-Level Image Processing Code into Hardware Pipelines](http://darkroom-lang.org/darkroom14-low.pdf)

[Darkroom](http://darkroom-lang.org/)

[Halide](http://halide-lang.org/)

[NNVM](http://nnvm.tvmlang.org/)

[Pyramid (image processing) - Wikipedia](https://en.wikipedia.org/wiki/Pyramid_(image_processing))

**To see our work**

[Github Repository](https://github.com/Compiler-02)
