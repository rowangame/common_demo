# -*- coding: UTF-8 -*-

# 当需要对一个列表进行去重操作的时候，set()函数就派上用场了
def testSet():
    obj = ['a', 'b', 'c', 'b', 'a']
    print(set(obj))


# 计算表达式
def testEval():
    equation = '(1 + 3 + 4) * 5'
    value = eval(equation)
    print(f'value={value}')


# 将列表、字典、元组里面的元素正/倒排序
def testSort():
    v1 = {'k1': 1, 'k2': -1, 'k3': 10}
    v2 = [1, 3, -3, -5]
    v3 = (1, 5, 5, -11, 13)
    r1 = sorted(v1, reverse=True)
    r2 = sorted(v2, reverse=True)
    r3 = sorted(v3)
    print(r1)
    print(r2)
    print(r3)

def testSortEx():
    lst = ['1/N', '2/Y', '3/N', '4/Y', '10/Y', '8/N', '6/Y', '5/N']
    a = [int(lst[0].split('/')[0])]
    b = []
    tem = 0
    for i in range(1, len(lst)):
        if lst[i][-1] == 'N':
            tem = (tem + 1) % 2
        if tem == 0:
            a.append(int(lst[i].split('/')[0]))
        else:
            b.append(int(lst[i].split('/')[0]))

    a.sort()
    b.sort()

    # a = sorted(a,key=lambda x:int(x))
    # b = sorted(b,key=lambda x:int(x))

    # print(' '.join(a))
    # print(' '.join(b))
    print(a)
    print(b)

# 对序列里的每个单词进行大写转化操作
def testMap():
    chars = ['apple', 'watermelon', 'pear', 'banana']
    a = map(lambda x: x.upper(), chars)
    print(list(a))


# 对列表里的每个数字作运算处理，用reduce函数
def testReduce():
    from functools import reduce
    nums = [1, 2, 3, 4]
    a = reduce(lambda x, y: x - y, nums)
    print(a)

    # 将字母连接成字符串
    chars = ['a', 'p', 'p', 'l', 'e']
    a = reduce(lambda x, y: x + y, chars)
    print(a)


# filter()函数轻松完成了任务，它用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象
def testFilter():
    nums = [1, 2, 3, 4, 5, 6]
    a = filter(lambda x: x % 2 != 0, nums)
    print(list(a))


# 同时打印出序列里每一个元素和它对应的顺序号，我们用enumerate()函数做做看。
def testEnumerate():
    chars = ['apple', 'watermelon', 'pear', 'banana']
    for i, j in enumerate(chars):
        print(i, j)


if __name__ == '__main__':
    # testSet()
    # testEval()
    # testSort()
    # testMap()
    # testReduce()
    # testFilter()
    testEnumerate()
    # testSortEx()