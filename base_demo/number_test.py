def testNumber():
    """
    int(x[, base])         将x转换为一个整数
    long(x[, base])        将x转换为一个长整数
    float(x)
    将x转换到一个浮点数
    complex(real[, imag])  创建一个复数
    str(x)
    将对象
    x
    转换为字符串
    repr(x)
    将对象
    x
    转换为表达式字符串
    eval(str)
    用来计算在字符串中的有效Python表达式, 并返回一个对象
    tuple(s)
    将序列
    s
    转换为一个元组
    list(s)
    将序列
    s
    转换为一个列表
    chr(x)
    将一个整数转换为一个字符
    unichr(x)
    将一个整数转换为Unicode字符
    ord(x)
    将一个字符转换为它的整数值
    hex(x)
    将一个整数转换为一个十六进制字符串
    oct(x)
    将一个整数转换为一个八进制字符串
    """
    strNumber = '123'
    print('int(x)=%d' % (int(strNumber)))

    number = 121
    print('str(x)=%s' % (str(number)))

    express = "(1 + 2 + 3) * 10"
    print('%s = %d' % (express, eval(express)))

    print('hex(x)=%s' % (hex(number)))
    print('chr(x)=%c' % (chr(97)))
    print('ord(x)=%d' % (ord('a')))
    print('oct(x)=%s' % (oct(100)))


if __name__ == '__main__':
    testNumber()
