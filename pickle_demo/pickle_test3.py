# -*- coding: utf-8 -*-
import pickle


def saveObject(obj, fileName):
    bFile = open(f'./{fileName}', 'wb')
    pickle.dump(obj, bFile)
    bFile.close()


def readObject(fileName):
    bFile = open(f'./{fileName}', 'rb')
    obj = pickle.load(bFile)
    bFile.close()
    return obj


class MyInfo(object):
    sn = '112233'
    bSn = '112244'
    logPort = 'com1'
    # def __init__(self):
    #     # self.sn = '112233'
    #     # self.bSn = '112244'
    #     # self.logPort = 'com1'
    #     pass

def test1():
    myInfo = MyInfo()
    fileName = 'port.pickle'
    saveObject(myInfo, fileName)
    tmpObj = readObject(fileName)
    print(dir(tmpObj))
    print(tmpObj.sn, tmpObj.bSn, tmpObj.logPort)
    print(type(tmpObj))


if __name__ == '__main__':
    test1()