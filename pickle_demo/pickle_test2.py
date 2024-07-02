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


data = dict()
for i in range(5):
    data[i] = i + 1
data['k1'] = 'key1'
print('before', data)
saveObject(data, 'test2.pickle')

dataEx = readObject('test2.pickle')
del(dataEx['k1'])
print('after', dataEx)

dataEx[0] = 121
saveObject(dataEx, 'test2.pickle')

dataExW = readObject('test2.pickle')
print(dataExW)