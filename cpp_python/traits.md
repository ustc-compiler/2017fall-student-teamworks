# trait的优点

trait能让类既可以看作方法的平展的集合，也能看作由许多trait构成的整体。看作方法的集合使类的含义容易被理解，不同trait的整合提供了复用。trait整合了这两个特点，使得trait在构造类的同时对类的含义没有影响。

# trait的特点

- trait提供一系列方法来执行行为。
- 每个方法作为行为的参数。
- trait不指定状态变量，并且trait提供的方法不直接访问状态变量。
- 类和trait可以由其他trait构成，但是构成的顺序无关。相冲突的方法必须被明确解决。
- trait不影响构成的类的语义。
- trait不影响构成的trait的语义。

# 继承的问题

* 单继承：表达能力不足
* 多继承：当一个类可以沿不同路径继承自一个基类时，存在语义不明
* Mixin继承：由于结构是线性的并且处理冲突的方式有限，当在其中一mixin中增加一个新的方法时，可能会重载在链上前面的mixin的一个同名的方法，而programmar不知道。

# trait的原理

* 继承用来从一个类衍生一个新的类，trait在一个类定义中实现复用，可以用Class = Superclass + State + Traits + Glue表示。
* 当方法出现冲突时，类的方法优先级高于trait，trait的方法优先级高于父类。

# trait的缺陷

* 没有完全解决命名冲突，使用别名的方式只是缩小了该问题的范围
* 虽然trait基于单继承，但是还是会有Diamond Problem。例如，trait X使用了traitY1和Y2，而Y1和Y2使用了traitZ，则trait Z的方法foo会被X得到两次。trait不会将这种情况视为冲突。













