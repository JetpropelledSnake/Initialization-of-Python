3-29 作业
	一：编写一个有参和一个无参函数，然后实现下列装饰器
	二：编写装饰器，为函数加上统计时间的功能
	三：编写装饰器，为函数加上认证的功能

	四：编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需再输入用户名和密码
	注意：从文件中读出字符串形式的字典，可以用eval('{"name":"egon","password":"123"}')转成字典格式

	五：编写装饰器，为多个函数加上认证功能，要求登录成功一次，在超时时间内无需重复登录，超过了超时时间，则必须重新登录

	六：编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果

	七：为题目五编写装饰器，实现缓存网页内容的功能：
	具体：实现下载的页面存放于文件中，如果文件内有值（文件大小不为0），就优先从文件中读取网页内容，否则，就去下载，然后存到文件中

	扩展功能：用户可以选择缓存介质/缓存引擎，针对不同的url，缓存到不同的文件中

	八：还记得我们用函数对象的概念，制作一个函数字典的操作吗，来来来，我们有更高大上的做法，在文件开头声明一个空字典，然后在每个函数前加上装饰器，完成自动添加到字典的操作

	九 编写日志装饰器，实现功能如：一旦函数f1执行，则将消息2017-07-21 11:12:11 f1 run写入到日志文件中，日志文件路径可以指定
	注意：时间格式的获取
	import time
	time.strftime('%Y-%m-%d %X')


	参考答案：
	http://www.cnblogs.com/linhaifeng/articles/7532497.html#_label6