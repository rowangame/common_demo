# -*- coding: UTF-8 -*-

# automaker2 基础测试
import os
import time
import logging
import uiautomator2 as u2
import myconfig


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


def baseTest():
    # 连接手机
    device = u2.connect(myconfig.Phone_SN)
    if device:
        print(f'连接手机设备成功,sn={myconfig.Phone_SN}')
        try:
            dvs = os.popen('adb devices')
            print('dvs=', dvs)

            time.sleep(1)
            os.popen('adb start-server')

            time.sleep(1)
            unlockScreen(device)
        except Exception as e:
            print(repr(e))
        finally:
            os.popen('adb kill-server')
    else:
        print(f'连接手机设备失败,sn={myconfig.Phone_SN}')


if __name__ == '__main__':
    baseTest()
