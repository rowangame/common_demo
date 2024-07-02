# -*- coding: UTF-8 -*-

import sys


print("__main__")
print(sys.path)

# '''
# 运行方式:
# D:\python\projs\base_demo>python -m package_demo
# __init__
# ['D:\\python\\projs\\base_demo', 'C:\\Python\\Python37\\python37.zip', 'C:\\Python\\P
# ython37\\DLLs', 'C:\\Python\\Python37\\lib', 'C:\\Python\\Python37', 'C:\\Python
# \\Python37\\lib\\site-packages']
# __main__
# ['D:\\python\\projs\\base_demo', 'C:\\Python\\Python37\\python37.zip', 'C:\\Python\\P
# ython37\\DLLs', 'C:\\Python\\Python37\\lib', 'C:\\Python\\Python37', 'C:\\Python
# \\Python37\\lib\\site-packages']
#
# D:\python\projs\base_demo>python package_demo
# __main__
# ['package_demo', 'C:\\Python\\Python37\\python37.zip', 'C:\\Python\\Python37\\DLL
# s', 'C:\\Python\\Python37\\lib', 'C:\\Python\\Python37', 'C:\\Python\\Python37\\
# lib\\site-packages']
#
# python -m package_demo 与 python package_demo 区别总结:
# 当加上-m参数时，Python会把当前工作目录添加到sys.path中；而不加-m时，Python则会把脚本所在目录添加到sys.path中。
# 当加上-m参数时，Python会先将模块或者包导入，然后再执行。
# __main__.py文件是一个包或者目录的入口程序。不管是用python package还是用python -m package运行，__main__.py文件总是被执行。
# '''

