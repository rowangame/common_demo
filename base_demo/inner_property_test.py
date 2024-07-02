# -*- coding: UTF-8 -*-

'''
__doc__：模块中用于描述的文档字符串
__name__：模块名
__file__：模块保存的路径
__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
'''


def test1():
    try:
        print('1', __doc__)
        print('2', __name__)
        print('3', __dict__)
    except Exception as e:
        print(repr(e))


if __name__ == '__main__':
    test1()