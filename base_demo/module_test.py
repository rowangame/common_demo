# from module_demo.MyModule import myminus,mysum
import module_demo.my_module as MyDul
import module_demo.ssp_com as SspCom

if __name__ == '__main__':
    """
    result = mysum(100,120)
    print('mysum=',result)

    result = myminus(100,120)
    print('myminus',result)
    """
    result = MyDul.mysum(100, 120)
    print('mysum=', result)

    result = MyDul.myminus(a=100, b=120)
    print('myminus', result)

    # print(globals())
    # print(dir(MyDul))
    MyDul.testGlobal()

    SspCom.openPort()
    SspCom.closePort()
