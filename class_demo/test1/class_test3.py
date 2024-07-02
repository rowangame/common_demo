# python类的继承
class ClsA(object):
    def __init__(self, a):
        print("ClsA init...")
        self.a = a


class ClsB(ClsA):
    def __init__(self, a):
        print("ClsB init...")
        super(ClsB, self).__init__(a)


class ClsC(ClsA):
    def __init__(self, a):
        print("ClsC init...")
        super(ClsC, self).__init__(a)


class ClsD(ClsB, ClsC):
    def __init__(self, a):
        print("ClsD init...")
        super(ClsD, self).__init__(a)


if __name__ == '__main__':
    clsD = ClsD('a')
