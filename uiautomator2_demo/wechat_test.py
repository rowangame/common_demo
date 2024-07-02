# -*- coding: UTF-8 -*-

import os
import time
import logging
import uiautomator2 as u2
import myconfig


# 设置日志目录
def setLoggingFile():
    now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    curdir = os.path.dirname(__file__)
    filePath = curdir + '\\' + 'Logs\\'
    if not os.path.exists(filePath):
        os.makedirs(filePath)
    fileName = filePath + f'{now}.txt'
    print(curdir, filePath, fileName)

    fmt = '[%(asctime)s] [%(filename)s line:%(lineno)d] [%(levelname)s] %(message)s'
    logging.basicConfig(level=logging.DEBUG, filename=fileName, filemode='w+',
                        format=fmt, encoding='utf-8')

    # 开始打印Android手机日志
    androidLogFile = filePath + f'android_{now}.txt'
    os.popen(f"adb -s {myconfig.Phone_SN} logcat >" + androidLogFile)


# 解锁屏幕
def unlockScreen(device: u2.Device):
    try:
        # 获得屏幕状态(如果是关闭状态,则需要开屏)
        state = device.info.get('screenOn')
        print(f'屏幕状态:{state}')
        if not state:
            device.screen_on()  # 开启屏幕

        if not device(resourceId="com.android.systemui:id/hw_keyguard_indication_text").exists:
            print('不需要解锁')
            return

        print('开始解锁屏幕')
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
    except Exception as e:
        print(repr(e))


# 打开微信app
def openWechatApp(device: u2.Device):
    print('打开微信app...')
    pckName = 'com.tencent.mm'
    try:
        device.app_start(pckName)
    except Exception as e:
        print(repr(e))


# 发送消息测试
def sendMessageTest(device: u2.Device):
    try:
        time.sleep(1)
        # 点击到发送面板
        device.xpath('//*[@resource-id="com.tencent.mm:id/dg2"]/android.widget.LinearLayout[2]').click()

        time.sleep(2)
        print(device(resourceId="com.tencent.mm:id/g78").info)

        # time.sleep(2)
        # device(resourceId="com.tencent.mm:id/g78").click()  # 聊天页面输入框
        # device.set_fastinput_ime(True)  # 设置输入法
        #
        # device.send_keys(f'自动化发送文字测试,不需要回复')  # 赋值文字
        # device(resourceId="com.tencent.mm:id/anv").click()  # 点击发送
        #
        # for i in range(2):
        #     device.send_keys(f'橙子好吃[{i}]', clear=True)  # 输入消息
        #     device(resourceId="com.tencent.mm:id/anv").click()  # 点击发送
        #     time.sleep(0.5)
    except Exception as e:
        print(repr(e))


# 结束测试
def doEndTest(device: u2.Device):
    try:
        time.sleep(2)
        pckName = 'com.tencent.mm'
        device.app_stop(pckName)

        time.sleep(1)
        device.screen_off()
    except Exception as e:
        print(repr(e))

def doProcess():
    # 设置日志文件
    setLoggingFile()

    # 连接手机
    device = u2.connect(myconfig.Phone_SN)
    if device:
        try:
            dvs = os.popen('adb devices')
            print('dvs=', dvs)

            time.sleep(1)
            os.popen('adb start-server')

            # 解锁屏幕
            time.sleep(1)
            unlockScreen(device)

            # 打开微信
            time.sleep(1)
            openWechatApp(device)

            # 发送消息测试
            time.sleep(1)
            sendMessageTest(device)

            # 结束测试
            doEndTest(device)
        except Exception as e:
            print(repr(e))
        finally:
            os.popen('adb kill-server')
    else:
        print('连接手机设备失败')

if __name__ == '__main__':
    doProcess()
