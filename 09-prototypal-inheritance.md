# Project Description of Prototypal Inheritance 

## Group Members
|Name|Github Account|
|:-:|:-:|
|王子博|Smart-Hypercube|
|王嵩超|songchaow|
|安鸣霄|nvagus|


Visit [our organization](https://github.com/compiler-teamwork-group09) for this project's codes and docs.

## Overview

Much different from Class-based Inheritance, as a style of object-oriented programming, Prototypal Inheritance provides a novel approach of reusing data.

**Here's a quick view of the phenomenon:**

```javascript
var foo = {name: "foo", one: 1, two: 2};
// another object
var bar = {two: "two", three: 3};
Object.setPrototypeOf(bar, foo); // foo is now the prototype of bar.
bar.one // Resolves to 1.
```
## Our Project's Description

In this project, we will do a simple survey on the phenomenon of Prototypal Inheritance. We will mainly cover in:

- Concepts of Prototypal Inheritance [songchaow]
- Genesis(origin) of prototype-based programming model [songchaow]

We will discuss the design ideas that Prototype-based Programming has adopted, including `delegation`, `extension` and other concepts from `Frame Theory` and a small language called `Actor`.

- The benefits of Prototypal Inheritance towards programmers [Smart-Hypercube, nvagus]
- The embodiment of Prototypal Inheritance in several programming languages(such as `JavaScript`) and their usages [Smart-Hypercube]
- The implementation of Prototypal Inheritance we'll try on `Python`. [nvagus, https://github.com/compiler-teamwork-group09/python3-proto]

Though `Python` itself already has some properties of Prototypal Inheritance(e.g. we can dynamically add attributes to an object instantiated from a class), We plan to implement a Prototypal Inheritance system that does not require our own definition of classes, providing full-featured interfaces without resort of classes via Python's decorators.
  
## Journal

- By Dec 23rd, 2017.
  * Discussion on QQ: scheduling.
  * Concept and origin: information collected.
  * Implementation on Python: utils confirmed.
- By Jan 3rd, 2017
  * Documents: repository established([documents repository](https://github.com/compiler-teamwork-group09/documents)). We've analyzed general features and design philosophy of prototype-based programming compared to class-based programming.

## To-do List
- Continue to read the paper, *Classifying Prototype-based Programming Language*, study several programming languages the paper has mentioned, and finally sort out how prototype-based languages are influenced by other languages before. [songchaow]

## References
- C.Dony, J.Malenfant, D.Bardou(1999). *Classifying Prototype-based Programming Language*. 
Retrieved from http://www.lirmm.fr/~dony/postscript/proto-book.pdf
- *Prototype-based programming*. Retrieved from https://en.wikipedia.org/wiki/Prototype-based_programming