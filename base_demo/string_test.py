# -*- coding: UTF-8 -*-
import math


def testFunction():
    str = 'hello Python'

    # 把字符串的第一个字符大写
    print(str.capitalize())

    # 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
    print(str.center(50).replace(' ', '*'))

    # 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
    print(str.count('hello'))

    # 以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除非 errors 指 定 的 是 'ignore' 或 者'replace'
    str2 = '字符串 test'
    try:
        str2_1 = str2.encode('GBK')
        str2_2 = str2_1.decode('GBK')
        str2_3 = str2.encode('UTF-8')
        str2_4 = str2_3.decode('UTF-8')
        print(str2_1, str2_2)
        print(str2_3, str2_4)
    except Exception as e:
        print(repr(e))

    str3 = 'xxx.png'
    print(str3.endswith('.png'))
    print(str3.find('.png'))
    print(str3.upper(), str3.lower())

    str4 = '12345'
    print('%s is digit %d' % (str4, str4.isdigit()))

def testMultiLinesStr():
    str = '''
    *	定义宽度或者小数点精度
    -	用做左对齐
    +	在正数前面显示加号(+)
    <sp> 在正数前面显示空格
    #	在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
    0	显示的数字前面填充'0'而不是默认的空格
    %	'%%'输出一个单一的'%'
    (var) 映射变量(字典参数)
    m.n. m是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
    '''
    print(str)
    print(ord(str[0]), ord(str[1]), ord(str[2]))
    str2 = 'Hello Python, Hello World'.replace('H', '#')
    print(str2)
    str3 = '0#1001#002#-1#03'
    str4 = str3.split(r'#')
    print(str4, '1001' in str4)
    str5 = '  012344.  5  '
    str6 = str5.strip()
    print(str6)


def testBase():
    s1 = 'Hello Python'
    print(s1, len(s1), s1[0:3])

    s2 = s1 * 2
    print(s2, 'Hello' in s2)

    s3 = r'\n\rPython..\t'
    print(s3)

    s4 = s3 == s2
    print(s4)

    num1 = 100
    num2 = math.pi
    num3 = -32768
    str1 = 'Python'
    s5 = '%+05d,%10.8f,%d,%s' % (num1, num2, num3, str1)
    print(s5)


if __name__ == '__main__':
    # testBase()
    # testMultiLinesStr()
    testFunction()