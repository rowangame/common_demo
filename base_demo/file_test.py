import os
import pathlib
import struct


def testInput():
    str = input('input:')
    print(str)


def testCurrentWorkDir():
    tmpWd = os.getcwd()
    print(type(tmpWd))
    print(tmpWd)


def testTextFile():
    wkdir = os.getcwd()
    subdir = wkdir + '\\out'
    dirFile = pathlib.Path(subdir)
    if not dirFile.exists():
        os.mkdir(subdir)

    txtFile = open('out/test.txt', 'w+')
    txtFile.write('Python\n')
    txtFile.write('Python文件测试\n')
    txtFile.flush()
    txtFile.close()

    txtFile = open('out/test.txt', 'r')
    lines = txtFile.readlines()
    txtFile.close()
    print('len(lines)=', len(lines))
    for i in range(0, len(lines)):
        print('[%d]=%s' % (i, lines[i]))


def testBinaryFile():
    wkdir = os.getcwd()
    subdir = wkdir + '\\out'
    dirFile = pathlib.Path(subdir)
    if not dirFile.exists():
        os.mkdir(subdir)

    num1 = 0x0a
    num2 = 0x112233
    str3 = 'Python'

    fileName = 'out/data.bin'
    # binFile = open(fileName,'wb+')
    # binFile.write(struct.pack('<i',num1))
    # binFile.write(struct.pack('<h',len(str3)))
    # # for letter in str3:
    # #     binFile.write(struct.pack('b',ord(letter)))
    # # 使用bytes构造方法
    # binFile.write(bytes(str3,'utf-8'))
    # binFile.write(struct.pack('<i',num2))
    # binFile.flush()
    # binFile.close()

    # 获得方件大小
    size = os.path.getsize(fileName)
    print('size = ', size)
    binFile = open(fileName, 'rb')
    data = binFile.read(size)
    binFile.close()
    print(repr(data))
    print('len(data)=', len(data))
    print('type(data)=', type(data))

    # 输出字节数据
    # [10, 0, 0, 0, 6, 0, 80, 121, 116, 104, 111, 110, 51, 34, 17, 0]
    btLst = []
    for bt in data:
        btLst.append(bt)
        # print('type(bt)=,bt=',type(bt),bt)
    print(btLst)

    # 解码(得到第一个数和字符串长度)
    # 构造一个字节组
    # int (4字节) + short(2字节) + int(4字节)
    tmpLen = 4 + 2
    # bytesg不可变字节数据，bytearray可变数据。这里必须用可充数据赋值
    # tmpBuffer = bytes(tmpLen)
    # tmpBuffer = bytearray()
    # for i in range(tmpLen):
    #     tmpBuffer.append(data[i])
    # 使用下标值赋值(高级用法)
    tmpBuffer = data[0:tmpLen]

    elements = struct.unpack('<ih', tmpBuffer)
    print('%d,%d' % (elements[0], elements[1]))

    # 解码得到字符串内容
    start = tmpLen
    strLen = elements[1]
    tmpBuffer = data[start:(start + strLen)]
    print('解码得到字符串内容 len(tmpBuffer)=', len(tmpBuffer))
    print('解码得到字符串内容 type(tmpBuffer)=', type(tmpBuffer))

    #生成对应的字符串长度解码类型
    # strFmt = ''
    # for i in range(tmpLen):
    #     strFmt += 'b'
    # print('strFmt=',strFmt)
    # 生成地应的字符串长度解码类型(使用乘法,高级用法)
    strFmt = 'b' * 6
    elements = struct.unpack(strFmt, tmpBuffer)
    print(elements)
    strContext = ''
    for letter in elements:
        strContext += chr(letter)
    print(strContext)
    #用decode方法解码字符串
    tmpStr = tmpBuffer.decode('utf-8')
    print('tmpStr=', tmpStr)

    #解码第三个整数
    tmpBuffer = data[size - 4:size]
    elements = struct.unpack('<i', tmpBuffer)
    print('解码第三个整数 = %x' % (elements[0]))

def testPack():
    # https://blog.csdn.net/weiwangchao_/article/details/80395941
    # @ 本机字节序
    # < 小端字节序
    # > 大端字节序
    # i 网络字节序(big-endian)
    buffer = struct.pack("<ihb", 1, 2, 3)
    print('len(buffer)=', len(buffer))
    # print(buffer)
    print(type(buffer))
    print(repr(buffer))

    buffer2 = struct.unpack('<ihb', buffer)
    print(type(buffer2))
    print('len(buffer2)=', len(buffer2))
    for element in buffer2:
        print('type,value', type(element), element)

    name = 'Python'
    buffer3 = bytes(name, 'utf-8')
    print('type(buffer3)=', type(buffer3))
    print('buffer3=', buffer3)

    # other test
    allbuf = buffer + buffer3
    print('len(allbuf)=%d' % (len(allbuf)))
    tmpbuf = bytearray()
    for bt in buffer:
        tmpbuf.append(bt)
    for bt in buffer3:
        tmpbuf.append(bt)
    print('len(tmpbuf)=%d' % (len(tmpbuf)))

    # test bytes
    tmpbuf = bytes((1,2,3,4))
    print(tmpbuf)
    str = ' test strip  '
    tmpStr = str.strip()
    print(tmpStr.replace(' ', '*'))

if __name__ == '__main__':
    # testInput()
    # testCurrentWorkDir()
    # testTextFile()
    testPack()
    # testBinaryFile()
