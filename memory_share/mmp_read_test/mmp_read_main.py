# -*- coding: UTF-8 -*-
# @Time    : 2024/10/98:50
# @Author  : xielunguo
# @Email   : xielunguo@cosonic.com
# @File    : mmp_read_main.py
# @IDE     : PyCharm
import mmap
import os.path
import subprocess
import threading
import time


class MMP_Test:
    SHARED_MEMORY_NAME = "my_define_data"
    SHARED_MEMORY_SIZE = 1024 * 1024
    isRunning = False

    @classmethod
    def getCurPath(cls):
        return os.path.dirname(__file__)

    @classmethod
    def getCModuleDemoPath(cls):
        exePath = cls.getCurPath() + "\\cmodule_demo\\mmap_demo.exe"
        return exePath

    @classmethod
    def getCModuleToolPath(cls):
        exePath = cls.getCurPath() + "\\cmodule_tool\\Burn_Tool.exe"
        return exePath

    @classmethod
    def mmpDemoReadProcess(cls, mmpName, mmpSize):
        print(f"name={mmpName} size={mmpSize}")
        time.sleep(6)
        print("reading process....")

        shared_memory = None
        try:
            readIndex = 0

            msgInfoSize = 4
            startIndex = msgInfoSize
            perSize = 64

            lastTick = time.time()
            max_retry_time = 60

            # 打开共享内存
            shared_memory = mmap.mmap(-1, cls.SHARED_MEMORY_SIZE, tagname=cls.SHARED_MEMORY_NAME, access=mmap.ACCESS_READ)
            while True:
                shared_memory.seek(0)

                btMsgInfo = shared_memory.read(msgInfoSize)
                curIndex = int.from_bytes(btMsgInfo[0:2], byteorder="little", signed=False)
                isEnd = int.from_bytes(btMsgInfo[2:3], byteorder="little", signed=False)
                reserved = int.from_bytes(btMsgInfo[3:4], byteorder="little", signed=False)

                if readIndex < curIndex:
                    # 移动到指定的起始位置
                    shared_memory.seek(startIndex)
                    # 从该位置读取指定长度的数据
                    data = shared_memory.read(perSize)

                    idxMsgData = data[0:2]
                    curIndex = int.from_bytes(idxMsgData, byteorder="little", signed=False)
                    strMsgLen = int(data[2:3][0])
                    strInfo = ""
                    if strMsgLen > 0:
                        strInfo = data[3:3 + strMsgLen].decode("GBK")
                    print(f"curIndex={curIndex}, strLen={strMsgLen} strInfo={strInfo}")
                    startIndex += perSize
                    readIndex += 1

                    lastTick = time.time()

                # 结束标记
                if isEnd > 0:
                    print(f"正常结束状态:{isEnd} totalIndex={curIndex}")
                    break

                curTick = time.time()
                dtime = curTick - lastTick
                if dtime > max_retry_time:
                    print(f"读取数据超时:dtime={dtime}>{max_retry_time}(s),关闭")
                    break
                time.sleep(0.2)
        finally:
            # 确保共享内存对象被正确关闭
            shared_memory.close()

    @classmethod
    def openExeDemo(cls):
        try:
            execPath = cls.getCModuleDemoPath()
            print(execPath)

            cls.isRunning = True
            # cModuleThread = threading.Thread(target=cls.mmpDemoReadProcess, args=(cls.SHARED_MEMORY_NAME, cls.SHARED_MEMORY_SIZE))
            # cModuleThread.start()

            # 使用无缓冲的方式创建子进程
            p = subprocess.Popen([execPath] + [cls.SHARED_MEMORY_NAME, str(cls.SHARED_MEMORY_SIZE)],
                                 stdout=subprocess.PIPE,
                                 universal_newlines=True,
                                 creationflags=subprocess.CREATE_NO_WINDOW  # 隐藏控制台窗口
                                 )

            stdout, stderr = p.communicate()
            print("------------------stdout-------------------")
            print(stdout)
            p.wait()

            cls.isRunning = False
        except Exception as e:
            print(repr(e))

    @classmethod
    def mmpToolReadProcess(cls, mmpName, mmpSize):
        time.sleep(6)

        shared_memory = None
        try:
            readIndex = 0

            msgInfoSize = 4
            startIndex = msgInfoSize
            perSize = 128  # sizeof(unsigned short) + sizeof(unsigned char) + sizeof(char buffer[125])

            lastTick = time.time()
            max_retry_time = 50
            print("mmname=?", mmpName)

            # 打开共享内存
            shared_memory = mmap.mmap(-1, mmpSize, tagname=mmpName, access=mmap.ACCESS_READ)
            while True:
                shared_memory.seek(0)

                btMsgInfo = shared_memory.read(msgInfoSize)
                curIndex = int.from_bytes(btMsgInfo[0:2], byteorder="little", signed=False)
                isEnd = int.from_bytes(btMsgInfo[2:3], byteorder="little", signed=False)
                reserved = int.from_bytes(btMsgInfo[3:4], byteorder="little", signed=False)

                if readIndex < curIndex:
                    # 移动到指定的起始位置
                    shared_memory.seek(startIndex)
                    # 从该位置读取指定长度的数据
                    data = shared_memory.read(perSize)

                    idxMsgData = data[0:2]
                    curSize = int.from_bytes(idxMsgData, byteorder="little", signed=False)
                    strMsgLen = int(data[2:3][0])
                    line = ""
                    if strMsgLen > 0:
                        line = data[3:3 + strMsgLen].decode("GBK")
                    print(f"read-> curIndex={curSize}, strLen={strMsgLen} strInfo={line}")

                    startIndex += perSize
                    readIndex += 1

                    lastTick = time.time()

                # 当共享数据缓冲区有数据时，直接读取(不需要判断,结束标记,解决读取数据不同步的问题)
                if readIndex < curIndex:
                    time.sleep(0.2)
                    continue

                # 结束标记
                if isEnd > 0:
                    print(f"正常结束状态:{isEnd} totalIndex={curIndex}")
                    break

                curTick = time.time()
                dtime = curTick - lastTick
                if dtime > max_retry_time:
                    print(f"读取数据超时:dtime={dtime}>{max_retry_time}(s),关闭")
                    break
                if not cls.isRunning:
                    break
                time.sleep(0.2)
        except Exception as e:
            print("showCModuleState.process error?" + repr(e))
        finally:
            if shared_memory is not None:
                # 确保共享内存对象被正确关闭
                shared_memory.close()

    @classmethod
    def openExeTool(cls):
        try:
            comType = "com4"
            fwPath = "F:\\CE_7587_7588\\bins\\XG_BT_FW_241008_0745_Test_DFU.bin"
            binTypeValue = 0
            mmShareName = "MY_SHARE_0808"
            mmShareSize = 512 * 1024

            execPath = cls.getCModuleToolPath()
            print(execPath)

            cls.isRunning = True

            # 使用无缓冲的方式创建子进程
            p = subprocess.Popen([execPath] + [comType, fwPath, str(binTypeValue), mmShareName],
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 universal_newlines=True,
                                 creationflags=subprocess.CREATE_NO_WINDOW  # 隐藏控制台窗口
                                 )
            time.sleep(2)

            cModuleThread = threading.Thread(target=cls.mmpToolReadProcess, args=(mmShareName, mmShareSize))
            cModuleThread.start()

            stdout, stderr = p.communicate()
            print("------------------stdout-------------------")
            print(stdout)
            print(stderr)
            p.wait()

            cls.isRunning = False
        except Exception as e:
            print(repr(e))


def start_mmp_demo_test():
    MMP_Test.openExeDemo()


def start_mmp_tool_test():
    MMP_Test.openExeTool()

if __name__ == "__main__":
    # threadTest = threading.Thread(target=start_mmp_demo_test, args=())
    # threadTest.start()
    threadTest = threading.Thread(target=start_mmp_tool_test, args=())
    threadTest.start()