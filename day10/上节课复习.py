上节课复习
    位置参数
        位置形参:必须被传值，多一个不行，少一个也不行
        def register(name,age,sex):
            pass



        位置实参：按照从左到右的顺序与形参一一对应

        register('egon',18,'male')
        register('egon1',28,'male')
        register('egon2',38,'male')
        register('egon3',48,'male')

    关键字参数:按照key=value形式指名道姓地为形参传值，可以完全不按照顺序
        1、关键字实参必须在位置参数后面
        2、可以混用位置实参与关键字实参，但不能为同一个形参重复传值
        register('egon3',sex='female',age=18)

    默认参数
        形参有默认值
         def register(name,age,sex='male'):
            pass
        register('egon',18,)
        register('egon1',28,)
        register('egon2',38,)
        register('egon3',48,)
        register('yangli',48,'female')

    可变长参数
        形参：*args,**kwargs

        实参:
            foo('a',*[1,2,3]) #foo('a',1,2,3)
            foo(x='bbb',*[1,2,3],) #foo(x='bbb',1,2,3) #语法错误

            foo(**{'x':1,'y':2}) #foo(x=1,y=2)
            #下面两个错误
            foo(**{'x':1,'y':2},1,2,3) #foo(x=1,y=2,1,2,3)
            foo(**{'x':1,'y':2},*(1,2,3)) #foo(x=1,y=2,1,2,3)


        def index(name):
            print('welecome %s to index page' %name)

        def wrapper(*args,**kwargs):
            index(*args,**kwargs) #index(1,2,name='egon')

        wrapper(1,2,name='egon')



补充:
    *的应用场景
    **的应用场景
    命名关键字参数



    def foo(x,y=1):
        pass



今日内容：
    1、函数嵌套
    2、名称空间与作用域
    3、函数对象
    4、闭包函数