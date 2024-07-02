import re


def testCompile():
    # re.compile函数
    # compile函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供
    # match()和search()这两个函数使用。
    # 语法格式为：
    # re.compile(pattern[, flags])
    pattern = re.compile(r'\d+')  # 用于匹配至少一个数字
    m = pattern.match('one12twothree34four')  # 查找头部，没有匹配
    print('m0=', m)
    m = pattern.match('one12twothree34four', 2, 10)  # 从'e'的位置开始匹配，没有匹配
    print('m1=', m)
    m = pattern.match('one12twothree34four', 3, 10)  # 从'1'的位置开始匹配，正好匹配
    print('m2=', m)
    # group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)
    # start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
    # end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
    # span([group]) 方法返回 (start(group), end(group))。

    # findall
    # 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
    pattern = re.compile(r'\d+')  # 查找数字
    result1 = pattern.findall('runoob 123 google 456')
    result2 = pattern.findall('run88oob123google456', 0, 10)
    print(result1, result2)

    alines = '''
    re.I	使匹配对大小写不敏感
    re.L	做本地化识别（locale-aware）匹配
    re.M	多行匹配，影响 ^ 和 $
    re.S	使 . 匹配包括换行在内的所有字符
    re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
    re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
    '''
    print(alines)

    pattern = re.compile('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})')
    s = '1102231990xxxxxxxx'
    match = re.match(pattern, s)
    print('match=', match)
    grp = match.group()
    print('len(grp)', len(grp))
    grpdct = match.groupdict()
    print('len(grpdct)', grpdct)


def testSub():
    phone = "2004-959-559-9599-959 # 这里有注释"
    num = re.sub(r'#.*$', '', phone)
    numex = num.strip()
    print(num, numex, len(num) == len(numex))

    # idx = phone.index('959x')
    # print('idx=',idx)

    match = re.search(r'959', phone)
    if match == None:
        print('none')
    else:
        print(match)
        spn = match.span()
        print(spn[0], spn[1])
        print(phone[spn[0]:spn[1]])
        s1 = match.start(0)
        s2 = match.end(0)
        print(s1, s2, phone[s1:s2])


def testSplit():
    str = 's1#s2#s3#s4#'
    out = str.split(r'#')
    print(out)

    str = r's1\r\ns2\r\nOK\r\n'
    print(str)
    out = str.split(r'\r\n')
    print(out)


def testTrim():
    str = ' Python '
    str1 = str.lstrip()
    str2 = str.rstrip()
    str3 = str.strip()
    print(len(str), len(str1), len(str2), len(str3))
    str4 = str.replace(' ', '')
    print(len(str4))


def testRegex1():
    print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
    print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配

    print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
    print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配


def testRegex2():
    line = "Cats are smarter than dogs"

    matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

    if matchObj:
        print(type(matchObj))
        print("matchObj.group() : ", matchObj.group())
        print("matchObj.group(1) : ", matchObj.group(1))
        print("matchObj.group(2) : ", matchObj.group(2))
    else:
        print("No match!!")


if __name__ == '__main__':
    # testRegex1()
    # testRegex2()
    # testTrim()
    # testSplit()
    # testSub()
    testCompile()
