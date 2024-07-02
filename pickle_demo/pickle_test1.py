# -*- coding: UTF-8 -*-
import pickle

# 序列化到文件
obj = (123, "abcdedf", ["ac", 123], {"key": "value", "key1": "value1"})
print(obj, len(obj), type(obj))

# wb 读写到二进制文件
f = open("./test1.pickle", 'wb')
pickle.dump(obj, f)
f.close()

f = open("./test1.pickle", 'rb')
print(pickle.load(f))
f.close()
