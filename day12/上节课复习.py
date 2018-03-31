上节课复习：
    1、为什么要有装饰器
        软件一旦上线，就应该遵循开放封闭原则，对扩展开放，对修改源代码及使用方式是封闭的

    2、什么是装饰器？
        器=》工具，装饰=》增加功能


        1、不修改源代码
        2、不修改调用方式
        装饰器是在遵循1和2原则的基础上为被装饰对象增加功能的工具

    3、实现无参装饰器
        1、无参装饰器的模板
        def outter(func):
            def wrapper(*args,**kwargs):
                res=func(*args,**kwargs)
                return res
            return wrapper

        2、使用:在被装饰对象正上方单独一行
        @无参装饰器名
        def foo():
            pass


    4、实现有参装饰器
        1、有参装饰器的模板
        def outter2(x,y,z):
            def outter(func):
                def wrapper(*args,**kwargs):
                    res=func(*args,**kwargs)
                    return res
                return wrapper
            return outter
        2、使用:在被装饰对象正上方单独一行
        @有参装饰器名(1,2,3)
        def foo():
            pass

今日内容：
    迭代器
    生成器
    面向过程编程