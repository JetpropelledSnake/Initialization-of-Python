上节课复习
    1、三元表达式
        条件成立的情况下返回的值 if 条件 else 条件不成立的情况下返回的值

    2、函数递归
        回溯
        递推

        注意点：
            1、必须要有一个明确的结束条件
            2、每进入下一次递归，问题的规模都应该减少

    3、匿名函数
        lambda x,y:x+y
        info=[
            {'name':'egon','age':'18','salary':'3000'},
            {'name':'wxx','age':'28','salary':'1000'},
            {'name':'lxx','age':'38','salary':'2000'}
        ]
        max(info,key=lambda dic:int(dic['salary']) )
        max([11,22,33,44,55])

        min(info,key=lambda dic:int(dic['salary']))
        l=sorted(info,key=lambda dic:int(dic['salary']))
        map(lambda x:x**2,[1,2,3,4])
        reduce
        filter(lambda x:x > 2,[1,2,3,4])



列表解析
生成器表达式

剩余的内置函数





今日内容
    模块的使用
    包的使用
    软件开发目录规范