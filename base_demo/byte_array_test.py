# -*- coding: UTF-8 -*-
import struct


def testStruct():
    # struct 封装字节数据
    # https://blog.csdn.net/weiwangchao_/article/details/80395941
    # @ 本机字节序
    # < 小端字节序
    # > 大端字节序
    # i 网络字节序(big-endian)
    num1 = 127
    num2 = 65535
    num3 = -32768
    num4 = 2147483647
    str1 = 'Python'
    data1 = struct.pack('<bHhi', num1, num2, num3, num4)
    print(len(data1), repr(data1), str(data1))

    data2 = struct.unpack('<bHhi', data1)
    print(data2)

    data3 = str1.encode('UTF-8')
    print('type(data3)=', type(data3))
    print(repr(data3), 'len(data3)=', len(data3))
    print('data3=', data3.decode('UTF-8'))

    # 用动态字节数据创建字节数据
    buf = bytearray()
    for tmpBt in data1:
        buf.append(tmpBt)
    data3_len = struct.pack('<B', len(data3))
    for tmpBt in data3_len:
        buf.append(tmpBt)
    for tmpBt in data3:
        buf.append(tmpBt)
    print('len(buf)=', len(buf), ' buf=', repr(buf))

    # 可用 + 运算符把字节数组连接起来
    bufEx = data1 + struct.pack('<B', len(data3)) + data3
    print('len(bufEx)=', len(bufEx), 'bytes=', repr(bufEx))
    # 解码字节数组
    dataEx = struct.unpack('<bHhiB', bufEx[0:10])
    print('dataEx=', dataEx)
    dataExW = bufEx[10:len(bufEx)].decode('UTF-8')  # 等价于: dataExW = bufEx[10:].decode('UTF-8')
    print('dataExW=', dataExW)

    # 从十六制字符串封装字节数组
    hexstr = '55 AA 04 03 CC'
    data = bytes.fromhex(hexstr)  # fromhex 函数会忽略字符串中间的空格
    print('type(data)=', type(data))
    dataHexStr = data.hex()
    print('len(data)=', len(data), 'data=', repr(data))
    print('dataHexStr=', dataHexStr)
    tmpFmt = 'B' * len(data)
    dataEx = struct.unpack(tmpFmt, data)
    print(dataEx)


if __name__ == '__main__':
    testStruct()