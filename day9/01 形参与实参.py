1、形参与实参是什么？
    形参（形式参数）：指的是
        在定义函数时，括号内定义的参数，形参其实就变量名
    实参（实际参数），指的是
        在调用函数时，括号内传入的值，实参其实就变量的值

    #x,y是形参
    def func(x,y): #x=10,y=11
        print(x)
        print(y)


    #10,11是实参
    func(10,11)

2、注意：
    实参值（变量的值）与形参（变量名）的绑定关系只在函数调用时才会生效/绑定
    在函数调用结束后就立刻解除绑定
    



