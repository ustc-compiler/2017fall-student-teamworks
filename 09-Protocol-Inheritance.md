# Project Description of Protocol Inheritance 
>Group 09 王子博 王嵩超 安鸣霄
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

  This includes concepts from `Frame Theory`.
- The embodiment of prototype inheritance in several programming languages(such as `JavaScript` and `Python`) and their usages
- The implementation insights we've found in some languages using Protocol Inheritance.