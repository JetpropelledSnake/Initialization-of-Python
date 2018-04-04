4月3号作业：
	1、求文件a.txt中总共包含的字符个数？思考为何在第一次之后的n次sum求和得到的结果为0？
	2、思考题
		with open('a.txt',encoding='utf-8') as f:
			g=(len(line) for line in f)
		print(sum(g))

	3、文件shopping.txt内容如下
		mac,2000,3
		lenovo,3000,10
		tesla,1000000,10
		chicken,200,1

		求总共花了多少钱？
		打印出所有的商品信息，格式为
		[{'name':'xxx','price':'3333','count':3},....]
		求单价大于10000的商品信息，格式同上


	4、改写ATM作业，将重复用到的功能放到模块中，然后通过导入的方式使用 