##python中的__init__和__new__
---
###定义
- __init__是什么：__init__就是用来初始化一个类实例，它是实例级别的方法，即它在实例生成后调用。
-  __new__是什么:__new__用来控制生成一个新实例的过程。它是类级别的方法即它在实例生成前调用。

- 类创建后，先运行__new__，在运行__init__, 然后再运行其他的方法。
###__init__和__new__的区别：
- _init_是当实例对象创建完成之后被调用的，然后设置对象属性的一些初始值； 
- _new_是在实例创建之前被调用的，因为它的任务就是创建实例然后返回该实例，是个静态方法。 
也就是，_new_在_init_之前被调用，_new_的返回值（实例）将传递给_init_方法的第一个参数，然后_init_给这些实例设置参数。
###例子
- 可以用__new__来实现设计模式中的单例模式。
```
class Singleton(object):
    __instance = None
    def __new__(cls, *args, **kws):
        if cls.__instance is None:#是否已经执行过Singleton
            cls.__instance = super().__new__(cls, *args, **kws)#
        return cls.__instance#返回实例化的对象super()
```

