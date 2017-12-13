# Project Description of Protocol Inheritance 
>Group 09 王子博 王嵩超 安鸣霄

Visit [our organization](https://github.com/compiler-teamwork-group09) for this projects's codes and docs.

## Overview

Much different from Class-based Inheritance, as a style of object-oriented programming, Protocol Inheritance provides a novel approach of reusing data.

**Here's a quick view of the phenomenon:**

```javascript
var foo = {name: "foo", one: 1, two: 2};
// another object
var bar = {two: "two", three: 3};
Object.setPrototypeOf(bar, foo); // foo is now the prototype of bar.
bar.one // Resolves to 1.
```
## Our Project's Description

In this project, we will do a simple survey on the phenomenon of Protocol Inheritance. We will mainly cover in:
- Concepts of Protocol Inheritance
- Genesis(origin) of prototype-based programming model

  We will discuss the design ideas that Prototype-based Programming has adopted, including `delegation`, `extension` and other concepts from `Frame Theory` and a small language called `Actor`.
- The benefits of Protocol Inheritance towards programmers
- The embodiment of prototype inheritance in several programming languages(such as `JavaScript`) and their usages
- The implementation of Prototype Inheritance we'll try on `Python`.

  Though `Python` itself already has some properties of Prototype Inheritance(e.g. we can dynamically add attributes to an object instantiated from a class), We plan to implement a Prototype Inheritance system that does not require our own definition of classes, providing full-featured interfaces without resort of classes via Python's decorators.