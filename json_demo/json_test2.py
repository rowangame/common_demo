import json

# python 原始类型向    json类型的转化对照表：
# Python	            JSON
# dict	                object
# list, tuple	        array
# str, unicode	        string
# int, long, float	    number
# True	                true
# False	                false
# None	                null

def testJsonArrayObject():
    srcJsn = '{"retCode":200,"lstCells":[{"name":"nm0","url":"http://www.test.com/id=0","id":1,"info":{"desc":"desc0","errorCode":0}},{"name":"nm1","url":"http://www.test.com/id=1","id":2,"info":{"desc":"desc1","errorCode":0}}]}'

    decodeInfo = json.loads(srcJsn)
    print('len(decodeInfo)', len(decodeInfo), decodeInfo)
    print(decodeInfo['retCode'])
    print(decodeInfo['lstCells'][0]['url'])
    print(decodeInfo['lstCells'][1]['info']['desc'])

    encodeInfo = json.dumps(decodeInfo)
    print(encodeInfo)


if __name__ == '__main__':
    testJsonArrayObject()
