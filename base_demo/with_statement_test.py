# with语句的工作原理
# __enter__()/__exit__()这两个方法
#
# with后面返回的对象要求必须有这两个方法，而文件对象f刚好是有这两个方法的。
#
# object.__enter__(self)
# 进入与此对象相关的运行时上下文。with语句将将此方法的返回值绑定到语句的AS子句中指定的目标（如果有设置的话）
#
# object.__exit__(self, exc_type, exc_value, traceback)
# 退出与此对象相关的运行时上下文。参数描述导致上下文退出的异常。如果上下文运行时没有异常发生，那么三个参数都将置为None。
# 如果有异常发生，并且该方法希望抑制异常（即阻止它被传播），则它应该返回True。否则，异常将在退出该方法时正常处理。
#
# 注意：
#  __exit__()方法不应该重新抛出传入的异常，这是调用者的职责。

class ClsA:
    def __enter__(self):
        print('__enter__() is call!')
        return self

    def doSomething(self):
        num = 1 / 0
        print('doSomething() is call!')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__() is call!')
        print(f'type:{exc_type}')
        print(f'value:{exc_val}')
        # 出现异常，阻止异常抛出
        return True


def testWith():
    with ClsA() as sample:
        sample.doSomething()


if __name__ == '__main__':
    testWith()
