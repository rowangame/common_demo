// std_out_demo.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//
#include <stdio.h>
#include <chrono>
#include <thread>

int main()
{
    for (int i = 0; i < 300; i++) {
        printf("[%d]输出测试:line=%d\n", i + 1, i + 1);
        std::this_thread::sleep_for(std::chrono::milliseconds(10));
    }
}
