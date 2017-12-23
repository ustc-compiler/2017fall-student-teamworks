# C++的trait

c++的trait是用来进行编译期类型判断和检测的，与论文“Traits: Composable Units of Behaviour”并无关系。

应该属于模板的一种应用。

# 源码分析

```c++
//std::integral_constant源码
typelate<class T, T v>
struct integral_constant
{
    static const T value = v;
    typedef T value_type;
    typedef integral_constant<T, v> type;
    operator value_type() {return value;}
};
```

利用的是static常量为编译器常量的特，定义了value。使用方法：从std::integral_constant派生，无需自己定义static const常量或enum类型。

std有两个定义好的std::integral_constant实例，分别定义了编译期的true和false类型，用途很广：

```c++
typedef integral_constant<bool, true> true_type;
typedef integral_constant<bool, false> false_type;
```

###常见的类型判断

* is_void

  ```c++
  template<class T, class U>
  struct is_same : std::false_type
  {};

  template<class T>
  struct is_same : std::true_type
  {};

  template<class T>
  struct is_void : std::is_same<void, typename std::remove_cv<T>::type>
  {};
  ```

  首先利用模板的匹配实现用以判断两种类型是否一致的is_same，再将T去除c（const）、v（volatile）限定符后与void类型判断是否一致。

* is_floating_point

  ```c++
  template< class T >
  struct is_floating_point : std::integral_constant<bool,std::is_same<float, typename std::remove_cv<T>::type>::value || std::is_same<double, typename std::remove_cv<T>::type>::value || std::is_same<long double, typename std::remove_cv<T>::type>::value> 
  {};
  ```

  判断是否是float，double，long double，与is_void相似。

* is_array

  ```c++
  template<class T>
  struct is_array : std::false_type {};

  template<class T>
  struct is_array<T[]> : std::true_type {};

  template<class T, std::size_t N>
  struct is_array<T[N]> : std::true_type {};
  ```

  进行了两个特化，找出数组类型。

* is_pointer

  ```c++
  template< class T > struct is_pointer_helper     : std::false_type {};
  template< class T > struct is_pointer_helper<T*> : std::true_type {};
  template< class T > struct is_pointer : is_pointer_helper<typename std::remove_cv<T>::type> {};
  ```

  特化了指针类型的is_pointer_helper继承了true_type。

*  is_member_pointer

  ```c++
  template< class T >
  struct is_member_pointer_helper : std::false_type {};

  template< class T, class U >
  struct is_member_pointer_helper<T U::*> : std::true_type {};

  template< class T >
  struct is_member_pointer : is_member_pointer_helper<typename std::remove_cv<T>::type> 
  {};
  ```

  与is_pointer相似，但多了类属信息。

* is_class

  ```c++
  namespace detail {
      template <class T> char test(int T::*);
      struct two { char c[2]; };
      template <class T> two test(...);
  }

  template <class T>
  struct is_class : std::integral_constant<bool, sizeof(detail::test<T>(0))==1 && !std::is_union<T>::value> 
  {};
  ```

  定义了两个模板函数，一个形参是int T::*（指向int型类成员变量的指针），返回值是char（大小是1）；另一个形参是所有类型，返回值是struct two（大小是2）。

  is_class继承了std::integral_constant< T, T v >（内部定义了一个static const T类型变量value，取值为v），value的类型为bool，当detail::test(0)的大小为1时（只要T是class类型，就符合第一个模板函数test，则其返回值大小就为1，否则返回值大小为2），并且不为union类型时（加上这个是因为，union类型类似struct类型，也支持T::*），则为class（或struct）类型。

*  is_base_of

  ```c++
  template <typename Base, typename Derived, 
      bool = (is_class<Base>::value && is_class<Derived>::value)>
  class is_base_of
  {
      template <typename T>
      static char helper(Derived, T);
      static int helper(Base, int);
      struct Conv
      {
          operator Derived();
          operator Base() const;
      };
  public:
      static const bool value = sizeof(helper(Conv(), 0)) == 1;
  };


  template <typename Base, typename Derived>
  class is_base_of<Base, Derived, false>
  {
  public:
      static const bool value = is_same<Base, Derived>::value;
  };
  ```

  * 如果Base不是Derived的基类，那么Conv()做隐式转换时，两个候选类型Base和Derived都是平等的，两个helper函数都可以匹配，但在这里按照规则，会去优先匹配非模板的函数。
  * 如果Base是Derived的基类，这种情况比较复杂。这种情况下，除非Conv对象是一个const的，否则它的隐式转换是只会去调用operator ()Derived的，因为operator ()Base const后面所带的const。于是这样的情况下，Conv()总是隐式转换成一个Derived对象，这时候对于两个helper的第一个参数，一个是精确匹配，一个是要转换为基类。







