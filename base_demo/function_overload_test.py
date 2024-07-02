import traceback
from functools import singledispatch


@singledispatch
def fun(arg):
    raise NotImplemented


@fun.register
def __(arg: int):
    print("int arg", arg)


@fun.register
def __(arg: str, value: int):
    print("str arg,value", arg, value)


def myfun(p1: int, p2: str, p3: list):
    print(p1, p2, p3)

if __name__ == "__main__":
    fun(10)
    fun('str', 100)
    try:
        fun()
    except Exception as e:
        print(str(e))
        # traceback.print_exc()
    myfun(p1=10, p2="str", p3=[1, 2, 3])
    myfun(p2="str2", p3=[1, 2, 3], p1=11)
