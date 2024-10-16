#include <windows.h>
#include <stdio.h>

#define SHARED_MEMORY_NAME L"my_define_data"
#define SHARED_MEMORY_SIZE 1024 * 1024

#pragma pack(1)
struct MyMsgInfo {
    unsigned short curIndex;    // 当前索引值
    unsigned char isEnd;        // 是否结束
    unsigned char reserved;     // 保存数据位
};

struct MyMsgData {
    unsigned short index;       // 当前数据索引位
    unsigned char len;          // 消息长度
    char buffer[61];            // 消息内容
};
#pragma pack()

static char* mmShareName = NULL;
static int mmMemorySize = 0;

int main(int cnt, char * args[]) {
    if (cnt != 3) {
        printf("参数数目不对!\n");
    }
    mmShareName = args[1];
    mmMemorySize = atoi(args[2]);
    printf("共享内存名:%s\n", mmShareName);
    printf("内存缓存区大小:%d\n", mmMemorySize);
     
    WCHAR wcBuffer[60];
    int size = sizeof(wcBuffer) / sizeof(WCHAR) - 1;
    printf("wcBuffer.size=%d\n", size);
    memset(wcBuffer, 0, size);
    MultiByteToWideChar(CP_UTF8, 0, mmShareName, -1, wcBuffer, size);
    printf("wcBuffer=%ls\n", wcBuffer);

    //// 创建或打开共享内存
    //HANDLE hMapFile = CreateFileMapping(
    //    INVALID_HANDLE_VALUE,    // 使用分页文件
    //    NULL,                    // 默认安全性
    //    PAGE_READWRITE,          // 可读写访问权限
    //    0,                       // 最大对象大小（高位）
    //    SHARED_MEMORY_SIZE,      // 最大对象大小（低位）
    //    (LPCWSTR) (&SHARED_MEMORY_NAME));  // 共享内存的名称

    // 创建或打开共享内存
    HANDLE hMapFile = CreateFileMapping(
        INVALID_HANDLE_VALUE,    // 使用分页文件
        NULL,                    // 默认安全性
        PAGE_READWRITE,          // 可读写访问权限
        0,                       // 最大对象大小（高位）
        SHARED_MEMORY_SIZE,      // 最大对象大小（低位）
        (LPCWSTR) (&wcBuffer[0]));  // 共享内存的名称

    if (hMapFile == NULL) {
        printf("Could not create file mapping object (%d).\n", GetLastError());
        return 1;
    }

    // 将共享内存映射到进程地址空间
    PCHAR pBuf = (PCHAR)MapViewOfFile(
        hMapFile,               // 映射对象的句柄
        FILE_MAP_ALL_ACCESS,    // 读写权限
        0,                      // 文件偏移的高位
        0,                      // 文件偏移的低位
        SHARED_MEMORY_SIZE);    // 要映射的字节数

    if (pBuf == NULL) {
        printf("Could not map view of file (%d).\n", GetLastError());
        CloseHandle(hMapFile);
        return 1;
    }

    // 向共享内存写入数据
    MyMsgInfo msgInfo;
    int msgInfoSize = sizeof(msgInfo);
    memset(&msgInfo, 0, msgInfoSize);

    int offset = msgInfoSize;
    int writeSize = 0;
    int index = 0;
    char tmpBuffer[128];
    for (int i = 0; i < 400; i++) {
        MyMsgData msgData;
        
        int tmpSize = sizeof(msgData);
        memset(&msgData, 0, tmpSize);
        msgData.index = index;
        memset(tmpBuffer, 0, sizeof(tmpBuffer));
        sprintf_s(tmpBuffer, "#<%d>数据:%d", i, i);
        int tmpLen = strlen(tmpBuffer);
        if (tmpLen <= sizeof(msgData.buffer)) {
            memcpy(msgData.buffer, tmpBuffer, tmpLen);
        } else {
            memcpy(msgData.buffer, tmpBuffer, sizeof(msgData.buffer));
        }

        msgData.len = strlen(msgData.buffer);
        writeSize += tmpSize;

        // 写数据内容
        printf("[%d] cur_size=%d offset=%d writeSize=%d ctx=%s\n", i, tmpSize, offset, writeSize, msgData.buffer);
        memcpy((PVOID)(pBuf+offset), &msgData, tmpSize);

       
        offset += tmpSize;
        index++;
        if (index < 200) {
            // 写消息休内容
            msgInfo.curIndex = index;
            msgInfo.isEnd = 0;
            msgInfo.reserved = tmpSize;
            memcpy((PVOID)(pBuf), &msgInfo, msgInfoSize);
        }
        else {
            // 写消息休内容(结束状态)
            msgInfo.curIndex = index;
            msgInfo.isEnd = 1;
            msgInfo.reserved = tmpSize;
            memcpy((PVOID)(pBuf), &msgInfo, msgInfoSize);
            break;
        }
        Sleep(500);
    }


    //char c = getchar();
    //printf("input:%d\n", c);
    Sleep(5000);

    // 清理资源
    UnmapViewOfFile(pBuf);
    CloseHandle(hMapFile);

    printf("Data written to shared memory.\n");

    return 0;
}
