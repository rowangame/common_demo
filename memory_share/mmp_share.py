import mmap
import os
import time

# SHARED_MEMORY_NAME = "my_define_data"
# SHARED_MEMORY_SIZE = 1024 * 1024

SHARED_MEMORY_NAME = "MY_SHARE_0808"
SHARED_MEMORY_SIZE = 512 * 1024

def mmap_test():
    shared_memory = None
    try:
        readIndex = 0

        msgInfoSize = 4
        startIndex = msgInfoSize
        # perSize = 64
        perSize = 128

        lastTick = time.time()
        max_retry_time = 50

        # 打开共享内存
        shared_memory = mmap.mmap(-1, SHARED_MEMORY_SIZE, tagname=SHARED_MEMORY_NAME, access=mmap.ACCESS_READ)
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
                    strInfo = data[3:3+strMsgLen].decode("GBK")
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

if __name__ == "__main__":
    mmap_test()