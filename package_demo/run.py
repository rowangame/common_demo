# -*- coding: UTF-8 -*-

import sys

print(sys.path)

print(__name__)

# '''
# 运行方式:
# C:\Users\asus>d:
# D:\>cd D:\python\projs\base_demo\package_demo
#
# D:\python\projs\base_demo\package_demo>python run.py
# ['D:\\python\\projs\\base_demo\\package_demo', 'C:\\Python\\Python37\\python37.zip', '
# C:\\Python\\Python37\\DLLs', 'C:\\Python\\Python37\\lib', 'C:\\Python\\Python37'
# , 'C:\\Python\\Python37\\lib\\site-packages']
#
# D:\python\projs\base_demo\package_demo>python -m run.py
# C:\Python\Python37\python.exe: Error while finding module specification for 'run
# .py' (ModuleNotFoundError: No module named 'run')
#
# D:\python\projs\base_demo\package_demo>
#
# 由于输出结果只列出了关键的部分，应该很容易看出他们之间的差异：
# 直接运行方式是把run.py文件所在的目录放到了sys.path属性中
# 以模块方式运行是把你输入命令的目录（也就是当前工作路径），放到了 sys.path 属性中。
# 以模块方式运行还有一个不同的地方：多出了一行No module named run.py的错误。实际上以模块方式运行时，
# Python先对run.py执行一遍 import，所以print(sys.path)被成功执行，然后Python才尝试运行run.py模块，
# 但是在path变量中并没有run.py这个模块，所以报错。正确的运行方式，应该是python -m run。
#
# '''

