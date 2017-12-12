04-Traits
===

## 0.小组成员：

```
名字	学号		github用户名
戢凯文	PB15000211	jikaiwen
滕思洁	PB15020737	yunmoxyz
赵皓宇	PB15111605	PB15111605

项目链接：
https://github.com/2017-CompilerH-a3/Teamwork-Traits
```

## 1. 课题：

Traits。

Traits为一种语言特征，表示一组方法可以用于扩展一个类的功能。


## 2. 关于Traits

PHP是单继承的语言，在PHP 5.4 Traits出现之前，PHP的类无法同时从两个基类继承属性或方法。php的Traits和Go语言的组合功能类似，通过在类中使用use关键字声明要组合的Trait名称，而具体某个Trait的声明使用trait关键词，Trait不能直接实例化。


## 3.与接口的不同


与Java的接口不同之处有：

interface 是定义接口，将逻辑交给其他程序员实现。trait是自己实现逻辑，供其他人使用。

接口的约束是前置的是定义初始就必须实现的, 他可以约束方法的实现却无法约束方法的调用, trait 是一种后置的调用, 他已经实现了方法, 关键的是, 他只对调用了自身的类产生约束, 而对没有调用自身的类不产生影响, 同时他是可复用的。




## 4. 与Mixin的区别

a. Mixin可能更多的是指动态语言，它是在执行到某个点的时候，将代码插入到其中来达到代码复用的效果。Trait更多的是编译过程中，通过一些静态手段赋值代码到类中使得其拥有Trait中的一些功能以达到代码复用的目的；

b. “Mixins may contain state, (traditional) traits don't.”这个区别比较弱，事实上Scala中Trait已经可以保存状态了（成员变量）； 

c. “Mixins use "implicit conflict resolution", traits use "explicit conflict resolution"”。这个区别可能是个明显的区别；但是如果某个语言它可以让Trait implicit resolve，那也没什么大不了。

d. “Mixins depends on linearization, traits are flattened.”这个区别可能有。至少Scala里面貌似Trait是Flattened处理的，跟Java嵌套类差不多。



---

bak

因为STL里面也有个traits的概念。下面这段先别删...

老师的意思似乎是让我们做上面那个。我先去万能的贴吧问问STL的Traits和多继承的Traits是否有关<_<

Traits，又被叫做特性萃取技术，说得简单点就是提取“被传进的对象”对应的返回类型，让同一个接口实现对应的功能。比如，C++里的STL的算法和容器是分离的，两者通过迭代器链接。但是，算法的实现并不知道自己被传进来什么。萃取器相当于在接口和实现之间加一层封装，来隐藏一些细节并协助调用合适的方法，这需要一些技巧（例如，偏特化）。






