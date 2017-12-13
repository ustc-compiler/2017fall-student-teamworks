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

Traits是一种语言特征，表示一组方法可以用于扩展一个类的功能。


## 2. 关于Traits

单继承的语言中类无法同时从两个基类继承属性或方法。于是，Traits被提出，通过在类中声明要组合的Trait名称，来达到从其他地方获得代码进行复用的目的。Trait不能实例化。

### trait的特点

* trait提供一系列方法来执行行为。
* 每个方法作为行为的参数。
* trait不指定状态变量，并且trait提供的方法不直接访问状态变量。（即不能定义与使用成员变量）
* 类和trait可以由其他trait构成，但是构成的顺序无关。相冲突的方法必须被明确解决。
* trait不影响构成的类的语义。
* trait不影响构成的trait的语义。

### trait的优点

trait能让类既可以看作方法的平展的集合，也能看作由许多trait构成的整体。看作方法的集合使类的含义容易被理解，不同trait的整合提供了复用。trait整合了这两个特点，使得trait在构造类的同时对类的含义没有影响。


### trait的缺陷

* 没有完全解决命名冲突，使用别名的方式只是缩小了该问题的范围
* 虽然trait基于单继承，但是还是会有Diamond Problem。例如，trait X使用了traitY1和Y2，而Y1和Y2使用了traitZ，则trait Z的方法foo会被X得到两次。trait不会将这种情况视为冲突。


### 继承的问题

* 单继承：表达能力不足
* 多继承：当一个类可以沿不同路径继承自一个基类时，存在语义不明
* Mixin继承：由于结构是线性的并且处理冲突的方式有限，当在其中一mixin中增加一个新的方法时，可能会重载在链上前面的mixin的一个同名的方法，而programmar不知道。
* Traits：当方法出现冲突时，类的方法优先级高于trait，trait的方法优先级高于父类。


## 3.与接口的不同


与Java的接口不同之处有：

interface 是定义接口，将逻辑交给其他程序员实现。trait是自己实现逻辑，供其他人使用。

接口的约束是前置的是定义初始就必须实现的, 他可以约束方法的实现却无法约束方法的调用, trait 是一种后置的调用, 他已经实现了方法, 关键的是, 他只对调用了自身的类产生约束, 而对没有调用自身的类不产生影响, 同时他是可复用的。

也就是说，Java的接口是你要求其他人实现而定义出来的，是某个对象必须去做某件事；而Traits，包括mixin，是你已经写完代码后给其他人使用，是某个对象可以、有能力去做某件事。

## 4. 与Mixin的区别

* Mixin可能更多的是指动态语言，它是在执行到某个点的时候，将代码插入到其中来达到代码复用的效果。Traits更多的是编译过程中，通过一些静态手段赋值代码到类中使得其拥有Trait中的一些功能以达到代码复用的目的；

* “Mixins may contain state, (traditional) traits don't.” 即mixin可以有成员变量而最开始的traits是不能的。但是现在事实上Scala中Trait已经可以保存成员变量了。 

* “Mixins use "implicit conflict resolution", traits use "explicit conflict resolution"”。 mixin碰到冲突会隐式的进行重写，后面覆盖前面的；而trait有明确的优先级。

* “Mixins depends on linearization, traits are flattened.” mixin是线性的，往类里追加的，后来的覆盖之前的；而traits是扁平的。