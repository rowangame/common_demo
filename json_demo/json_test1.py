import json

# 文档参考 https://docs.python.org/2/library/json.html
"""
python 原始类型向    json类型的转化对照表：
Python              JSON
dict                object
list, tuple         array
str, unicode        string
int, long, float    number
True                true
False               false
None                null
"""

def test1():
    data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]

    data2 = json.dumps(data)
    print(type(data2), data2)

    data2 = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    print(data2)

    lst = '[{"k1":1,"k2":2,"k3":"value"},{"k1":21,"k2":22,"k3":"value2"}]'
    out = json.loads(lst)
    print(type(out), len(out), out)
    print(out[0]['k1'], out[0]['k1'] == 1, type(out[0]))


if __name__ == '__main__':
    test1()
