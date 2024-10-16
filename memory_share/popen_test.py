import os
import subprocess
import threading
import time
import traceback
import tempfile

def test_1():
    try:
        cmd = "dir"
        out_temp = tempfile.SpooledTemporaryFile(max_size=10 * 1000)
        fileno = out_temp.fileno()
        obj = subprocess.Popen(cmd, stdout=fileno, stderr=fileno, shell=True)
        obj.wait()

        size = out_temp.tell()
        print(f"size={size}")

        out_temp.seek(0)
        # lines = out_temp.readlines()
        # print(lines)

        tmpbuf = out_temp.read(size)
        infos = tmpbuf.decode("GBK")
        lines = infos.split("\r\n")
        print(lines)

    except Exception as e:
        print(traceback.format_exc())
    finally:
        if out_temp:
            out_temp.close()

def test_2():
    execPath = os.getcwd() + "\\cmodel\\std_out_demo.exe"
    print(f"C++模块目录:{execPath}")

    out_temp = None
    try:
        out_temp = tempfile.SpooledTemporaryFile(max_size=10 * 1000)
        fileno = out_temp.fileno()

        lasttime = time.time()
        # 使用subprocess.Popen来启动程序并捕获输出
        process = subprocess.Popen(
            [execPath] + ["p1", "p2"],
            stdout=fileno,
            stderr=fileno,
            text=True,
            bufsize=1  # 行缓冲
        )

        process.wait()

        curtime = time.time()
        print(f"dtime={curtime - lasttime}")

        size = out_temp.tell()
        print(f"size={size}")

        out_temp.seek(0)

        # tmpbuf = out_temp.read(size)
        # infos = tmpbuf.decode("GBK")
        # lines = infos.split("\r\n")
        # for tmpLine in lines:
        #     print(tmpLine)
    except Exception as e:
        print(repr(e))
    finally:
        if out_temp is not None:
            out_temp.close()

def inner_process(p1):
    execPath = os.getcwd() + "\\cmodel\\std_out_demo.exe"
    print(f"C++模块目录:{execPath}")

    # 使用无缓冲的方式创建子进程
    p = subprocess.Popen([execPath],
                         stdout=subprocess.PIPE,
                         universal_newlines=True,
                         creationflags = subprocess.CREATE_NO_WINDOW  # 隐藏控制台窗口
                         )

    (stdout, stderr) = p.communicate()
    print(stdout)

    # 等待子进程结束
    p.wait()

def test_3():
    t1 = threading.Thread(target=inner_process, args=([0]))
    t1.start()

if __name__ == "__main__":
    # test_2()
    test_3()