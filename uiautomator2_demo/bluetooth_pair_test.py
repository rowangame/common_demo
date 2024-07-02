# -*- coding: UTF-8 -*-

import logging
import os
import time

import uiautomator2 as u2


class ProjectConfig(object):
    phone_SN = 'HLRDU19816016577'  # Huawei Nova3

'''
Android SDK内置工具uiautomatorviewer.bat与uiautomator2冲突的方案:

使用weditor:
调用python-uiautomator2的两个接口screenshot和dump_hierarchy这样就不会有冲突问题了

安装方法: 
pip install --pre weditor

使用方法: 
首先运行python -m weditor，
之后浏览器会自动打开一个网页 
http://localhost:17310/
注:这个网址仅提供一个前端,而python -m weditor这个命令则本地开放了HTTP的接口,前端去跟本地的服务去通信）

解锁屏幕方案:
因weditor在获得解锁九宫格图案时，不能获取屏幕载图，无法定位位置信息
所以采用截图当前解锁界面，然后操作手机到主界面。进入文件->图片->选中当前截图的图(双击图片可全屏显示)。
然后再使用weditor中间那个动态同步按钮。使用当前界面与手机屏幕同步。
这里就可以进行坐标定位(可选百分比和像素类型，这里使用像素类型)了。
获取解锁屏幕九宫格坐标后就可以解锁屏幕了
'''


# 得到当前运行的app
def getCurrentApp(device: u2.Device):
    # # 直接包名打开app
    # device.app_start('com.android.browser')
    # # 关闭app
    # device.app_stop('com.android.browser')
    # # 清除app的数据
    # device.app_clear('com.android.browser')
    # # 列举正在运行的app
    # print(device.app_list_running())
    # # 获取正在运行的app //com.xiaomi.shop
    # print(device.app_current)
    return device.app_current()


# 打开音乐App
def startMusicApp(device: u2.Device):
    pckName = 'com.android.mediacenter'
    device.app_start(pckName)

    time.sleep(4)
    # 查找当前默认音乐标题
    if device(resourceId="com.android.mediacenter:id/song_title").exists:
        title = device(resourceId="com.android.mediacenter:id/song_title").get_text()
        print('找到默认的音乐标题:', title)
    else:
        print('没有找到默认的音乐标题')

    # 播放默认音乐
    if device(resourceId="com.android.mediacenter:id/repeat_play_tip_layout").exists:
        print('播放默认音乐')
        device(resourceId="com.android.mediacenter:id/repeat_play_tip_layout").click()
        time.sleep(10)
    else:
        print('没有找到播放音乐按钮，不能播放音乐')

    time.sleep(1)
    print('停止音乐播放')
    device.app_stop(pckName)

    # print('当前运行的app列表')
    # print(device.app_list_running())

    # 返回到设置界面
    goBackmain(device)


# 返回到主界面
def goBackmain(device: u2.Device):
    try:
        # 返回到主界面
        time.sleep(1)
        device.press('back')
        time.sleep(1)
        device.press('back')

        time.sleep(1)
        # 打开设置面板
        device(description='设置').click()

        time.sleep(2)
        # 打开蓝牙面板
        device(resourceId="android:id/title", text="蓝牙").click()

        # 取消配对操作
        time.sleep(2)
        try:
            bleName = 'HUAWEI FreeLace Pro'
            boFindXPath = ''
            findPathIndex = -1
            boFindDevice = False
            # 遍历蓝牙设备列表(查找蓝牙设备)
            # 获得最上层父类
            rootNode = device.xpath('//*[@resource-id="com.android.settings:id/list"]')
            if rootNode and rootNode.info['childCount'] > 2:
                childCnt = rootNode.info['childCount']
                for i in range(2, childCnt):
                    # 获得子类控件
                    lstNode = device.xpath(
                        f'//*[@resource-id="com.android.settings:id/list"]/android.widget.LinearLayout[{i}]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]').all()
                    for tmpEle in lstNode:
                        tmpNode = tmpEle.elem.getchildren()
                        for child in tmpNode:
                            tmpName = child.get("text")
                            print(f'goBackMain device[{i}]', tmpName)
                            if tmpName == bleName:
                                findPathIndex = i
                                boFindDevice = True
                                boFindXPath = f'//*[@resource-id="com.android.settings:id/list"]/android.widget.LinearLayout[{i}]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]'
                                break
                        if boFindDevice:
                            break
            if boFindDevice:
                print(f'找到了配对的蓝牙设备{bleName}')
                xpathName = f'//*[@resource-id="com.android.settings:id/list"]/android.widget.LinearLayout[{findPathIndex}]/android.widget.LinearLayout[1]'
                # 配对蓝牙的设置按钮点击
                device.xpath(xpathName).click()

                time.sleep(2)
                # 取消配对按钮点击
                device(resourceId="com.android.settings:id/unpair_btn").click()

                # 取消配对后会返回到上一个界面，不需要再调用返回按钮功能
                # time.sleep(2)
                # 返回蓝牙界面
                # device(description="向上导航").click()
                # device(resourceId="com.android.systemui:id/back").click()
            else:
                print(f'没有找到配对的蓝牙设备{bleName}')
        except Exception as e:
            print(repr(e))

        time.sleep(2)
        # 关闭蓝牙
        if device(resourceId='com.android.settings:id/switch_widget').exists:
            print('关闭蓝牙')
            device(resourceId='com.android.settings:id/switch_widget').click()

        # 返回到设置界面
        device.press('back')

        time.sleep(2)
        # 返回到主界面
        device.press('back')

        time.sleep(2)
        # 熄屏
        device.screen_off()
    except Exception as e:
        print(repr(e))

# 打开蓝牙界面
def openBluetoothMain(device: u2.Device):
    try:
        # device.xpath(
        #     '//*[@resource-id="com.android.settings:id/dashboard_container"]/android.widget.LinearLayout[4]').click()
        device(resourceId="android:id/title", text="蓝牙").click()

        time.sleep(2)
        # 开启蓝牙按钮
        # 这里先判断蓝牙按钮是否是开启状态
        # 如果不是开启状态，则开启蓝牙按钮
        if device(resourceId='com.android.settings:id/switch_widget').info['checked'] == False:
            device(resourceId='com.android.settings:id/switch_widget').click()

        bleName = 'HUAWEI FreeLace Pro'
        '''
        time.sleep(2)
        boFindDevice = False
        boFindXPath = ''
        # 遍历蓝牙设备列表(查找蓝牙设备)
        # 获得最上层父类
        try:
            rootNode = device.xpath('//*[@resource-id="com.android.settings:id/list"]')
            if rootNode and rootNode.info['childCount'] > 2:
                childCnt = rootNode.info['childCount']
                for i in range(2, childCnt):
                    # 获得子类控件
                    lstNode = device.xpath(
                        f'//*[@resource-id="com.android.settings:id/list"]/android.widget.LinearLayout[{i}]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]').all()
                    for tmpEle in lstNode:
                        tmpNode = tmpEle.elem.getchildren()
                        for child in tmpNode:
                            tmpName = child.get("text")
                            print(f'device[{i}]', tmpName)
                            if tmpName == bleName:
                                boFindDevice = True
                                boFindXPath = f'//*[@resource-id="com.android.settings:id/list"]/android.widget.LinearLayout[{i}]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]'
                                break
        except Exception as e:
            print(repr(e))

        if boFindDevice:
            print(f'找到了要配对的蓝牙耳机:{bleName}')
        else:
            print(f'没有要配对的蓝牙耳机:{bleName}')
        '''

        time.sleep(2)
        '''
        配对界面相关
        标题 d(resourceId="com.android.settings:id/message_subhead")
        配对 d(resourceId="android:id/button1")
        取消 d(resourceId="android:id/button2")
        连接界面相关
        标题 d(resourceId="com.huawei.iconnect:id/custom_title")
        连接 d(resourceId="com.huawei.iconnect:id/ear_click_button")
        取消 d(resourceId="com.huawei.iconnect:id/left_button_text_ear")
        '''

        # 分析是否有弹出配对界面,如果存在执行配对点击事件
        boIsPaired = False
        boFindPairPnl = False
        findPnlIndex = -1
        waitCnt = 0
        while True:
            # 找到了配对按钮，则认为当前弹出了配对界面
            if device(resourceId="com.huawei.iconnect:id/ear_click_button").exists:
                boFindPairPnl = True
                findPnlIndex = 1
                break
            if device(resourceId="android:id/button1").exists:
                boFindPairPnl = True
                findPnlIndex = 2
                break
            time.sleep(1)
            waitCnt += 1
            if waitCnt > 2:
                break

        print(f'查找蓝牙连接状态,boFindPairPnl={boFindPairPnl} findPnlIndex={findPnlIndex}')
        if findPnlIndex == 1:
            # 查找到了连接界面，分析是否是指定的耳机类型。如果是则连接，否则取消连接
            if boFindPairPnl:
                tmpTxt = device(resourceId="com.huawei.iconnect:id/custom_title").get_text()
                if tmpTxt == bleName:
                    time.sleep(2)
                    print('是指定的蓝牙耳机连接,可执行连接操作')
                    device(resourceId="com.huawei.iconnect:id/ear_click_button").click()
                    boIsPaired = True
                else:
                    time.sleep(2)
                    print('不是指定的蓝牙耳机连接,取消连接操作')
                    device(resourceId="com.huawei.iconnect:id/left_button_text_ear").click()
            else:
                print('没有找到连接面板,蓝牙连接取消')
        elif findPnlIndex == 2:
            # 找到了配对界面
            tmpTxt = device(resourceId="com.android.settings:id/message_subhead").get_text()
            if tmpTxt == bleName:
                time.sleep(2)
                print('是指定的蓝牙耳机配对,可执行配对操作')
                device(resourceId="android:id/button1").click()
                boIsPaired = True
            else:
                time.sleep(2)
                print('不是指定的蓝牙耳机配对,取消配对操作')
                device(resourceId="android:id/button2").click()

        # 配对成功播放音乐
        if boIsPaired:
            time.sleep(5)
            print('关闭当前应用')
            curApp = getCurrentApp(device)
            # {'package': 'com.android.settings', 'activity': '.Settings$BluetoothSettingsActivity', 'pid': 21752}
            device.app_stop(curApp['package'])

            time.sleep(1)
            print('配对成功，开始播放音乐')
            startMusicApp(device)
        else:
            print('没有配对成功,不能播放音乐')
            print('当前运行的app:', getCurrentApp(device))
            time.sleep(2)
            # 关闭蓝牙
            if device(resourceId='com.android.settings:id/switch_widget').info['checked']:
                device(resourceId='com.android.settings:id/switch_widget').click()

            time.sleep(2)
            # 返回到设置界面
            device.press('back')

            time.sleep(2)
            # 返回到主界面
            device.press('back')

            time.sleep(2)
            # 熄屏
            device.screen_off()
    except Exception as e:
        print(repr(e))


# 打开设置面板
def openSettings(device: u2.Device):
    try:
        device(description='设置').click()
        # com.android.settings
    except Exception as e:
        print(str(e))


# 解锁屏幕图案
def unlockScreen(device: u2.Device):
    try:
        # 滑动调出解锁面板
        device.swipe(540, 1576, 540, 676)
        time.sleep(2)

        # 解锁图案(需要参考解锁屏幕方案,获得解锁坐标)
        p1 = [236, 1261]
        p2 = [232, 1565]
        p3 = [537, 1874]
        p4 = [842, 1565]
        p5 = [842, 1869]
        device.swipe_points(points=[p1, p2, p3, p4, p5], duration=0.125)

        # 按返回按钮
        # time.sleep(2)
        # device(text='返回').click()
    except Exception as e:
        print(repr(e))


def setLoggingPath():
    '''
    %(name)s Logger的名字
    %(levelno)s 数字形式的日志级别
    %(levelname)s 文本形式的日志级别
    %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
    %(filename)s 调用日志输出函数的模块的文件名
    %(module)s 调用日志输出函数的模块名
    %(funcName)s 调用日志输出函数的函数名
    %(lineno)d 调用日志输出函数的语句所在的代码行
    %(created)f 当前时间，用UNIX标准的表示时间的浮点数表示
    %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
    %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
    %(thread)d 线程ID。可能没有
    %(threadName)s 线程名。可能没有
    %(process)d 进程ID。可能没有
    %(message)s 用户输出的消息
    '''
    # now = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
    now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    curdir = os.path.dirname(__file__)
    filePath = curdir + '\\' + 'logs\\'
    if not os.path.exists(filePath):
        os.makedirs(filePath)
    fileName = filePath + f'{now}.txt'
    print(curdir, filePath, fileName)
    # 用例测试日志配置
    # fmt = '%(asctime)s - %(pathname)s[line:%(lineno)d] -. %(levelname)s: %(message)s'
    fmt = '[%(asctime)s] [%(filename)s line:%(lineno)d] [%(levelname)s] %(message)s'
    logging.basicConfig(level=logging.DEBUG, filename=fileName, filemode='w+',
                            format=fmt, encoding='utf-8')
    # logging.log(level=logging.DEBUG, msg='测试 this!!!')
    # logging.error(msg='error 测试!!!')
    # logging.info(msg='info 测试')

    # 开始打印Android手机日志
    androidLogFile = filePath + f'android_{now}.txt'
    os.popen(f"adb -s {ProjectConfig.phone_SN} logcat >" + androidLogFile)


def testDeviceConnect():
    device = u2.connect(ProjectConfig.phone_SN)  # 连接手机
    if device is not None:
        try:
            print("测试函数前执行")
            rlt = os.popen("adb devices")
            print('rlt1', rlt.read())

            time.sleep(1)
            os.popen("adb start-server")

            time.sleep(1)
            device.screen_off()

            time.sleep(1)
            device.screen_on()

            time.sleep(1)
            # # 获取基本信息
            # dinfo = device.info
            # print(dinfo)
            print(device.window_size())

            # 获取当前屏幕状态
            screenState = device.info.get('screenOn')
            print(screenState)

            # 解锁屏幕
            unlockScreen(device)

            # 设备日志信息
            setLoggingPath()

            time.sleep(1)
            openSettings(device)

            time.sleep(1)
            openBluetoothMain(device)
        except Exception as e:
            print(str(e))
        finally:
            os.popen("adb kill-server")  # 停止Android手机日志打印
    else:
        print("connect to device fail")


if __name__ == '__main__':
    testDeviceConnect()