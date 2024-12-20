import os

import time

__author__ = 'shikun'
import re
import subprocess

# from PyQt5.QtGui.QIcon import pixmap


def stop_monkey(dev):
    monkey_name = "com.android.commands.monkey"
    print("--------------------")
    pid = subprocess.Popen("adb -s " + dev + " shell ps | findstr " + monkey_name, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout.readlines()
    if pid =="":
        print("No monkey running in %s" % dev)
    else:
        for item in pid:
            if item.split()[8].decode() == monkey_name:
                monkey_pid = item.split()[1].decode()
                cmd_monkey = "adb -s " + dev + " shell kill %s" % (monkey_pid)
                os.popen(cmd_monkey)
                print("Monkey in %s was killed" % dev)
                time.sleep(2)
    subprocess.Popen("taskkill /f /t /im python.exe", shell=True)

def reboot(dev):
    cmd_reboot = "adb -s " + dev + " reboot"
    os.popen(cmd_reboot)


def getModel(devices):
    result = {}
    try:
        # 获取Android系统版本
        cmd_version = f"adb -s {devices} shell getprop ro.build.version.release"
        result["release"] = subprocess.check_output(cmd_version, shell=True).decode().strip()

        # 获取手机型号
        cmd_model = f"adb -s {devices} shell getprop ro.product.model"
        result["phone_name"] = subprocess.check_output(cmd_model, shell=True).decode().strip()

        # 获取手机品牌
        cmd_brand = f"adb -s {devices} shell getprop ro.product.brand"
        result["phone_model"] = subprocess.check_output(cmd_brand, shell=True).decode().strip()

        return result
    except subprocess.CalledProcessError as e:
        print(f"命令执行失败：{e}")
    except Exception as e:
        print(f"发生错误：{e}")


def get_men_total(devices):
    cmd = "adb -s " + devices + " shell cat /proc/meminfo"
    print(cmd)
    # output = subprocess.check_output(cmd).split()
    # # item = [x.decode() for x in output]
    # return  int(output[1].decode())

    output = subprocess.check_output(cmd, shell=True)

    # 将输出的字节串解码为字符串，然后分割
    output_str = output.decode().split()

    # 提取第二项并转换为整数
    # 假设output_str[1]是您想要转换为整数的项
    item = int(output_str[1])
    return item

# # 得到几核cpu
# def get_cpu_kel(devices):
#     cmd = "adb -s " + devices +" shell cat /proc/cpuinfo"
#     print(cmd)
#     output = subprocess.check_output(cmd).split()
#     sitem = ".".join([x.decode() for x in output]) # 转换为string
#     return str(len(re.findall("processor", sitem))) + "核"

#

def get_cpu_kel(devices):
    cmd = ["adb", "-s", devices, "shell", "cat", "/proc/cpuinfo"]
    try:
        # 执行命令并捕获输出
        output = subprocess.check_output(cmd).decode('utf-8')
        # 使用正则表达式查找所有包含 "processor" 的行
        processor_lines = re.findall(r"^processor", output, re.MULTILINE)
        # 返回核心数
        return str(len(processor_lines))
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the command: {e}")
        return "Error"


# def get_app_pix(devices):
#     # 构建命令，避免使用 shell=True
#     cmd = ["adb", "-s", devices, "shell", "wm", "size"]
#
#     try:
#         # 执行命令并获取输出
#         output = subprocess.check_output(cmd)
#
#         # 分割输出并获取屏幕尺寸
#         # 假设输出格式为 "width height"，例如 "1080 1920"
#         width, height = output.decode().split()[:2]
#
#         # 返回屏幕尺寸，这里假设只需要返回宽度
#         return width
#     except subprocess.CalledProcessError as e:
#         print(f"An error occurred while executing the command: {e}")
#         return None
#     except IndexError:
#         print("Unexpected output format.")
#         return None
def get_android_version(devices):
    cmd = ["adb", "-s", devices, "shell", "getprop", "ro.build.version.sdk"]
    try:
        output = subprocess.check_output(cmd).decode().strip()
        return int(output)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while getting Android version: {e}")
        return None

# 获取屏幕尺寸
def get_app_pix(devices):
    cmd = ["adb", "-s", devices, "shell", "wm", "size"]
    try:
        # 执行命令并获取输出
        output = subprocess.check_output(cmd).decode()

        # 如果Android版本大于10，使用新的解析逻辑
        if get_android_version(devices) > 29:  # 29 对应 Android 10
            # 使用正则表达式匹配分辨率
            match = re.search(r"Physical size: (\d+)x(\d+)", output)
            if match:
                width, height = match.groups()
                return width
            else:
                print("Unexpected output format for Android version > 10.")
                return None
        else:
            # 旧版本Android解析逻辑
            width, height = output.split()[:2]
            return width
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing the command: {e}")
        return None

#
def get_phone_Kernel(devices):
    pix = get_app_pix(devices)
    men_total = get_men_total(devices)
    phone_msg = getModel(devices)
    cpu_sum = get_cpu_kel(devices)
    return phone_msg, men_total, cpu_sum,pix
if __name__ == '__main__':
    # get_app_pix("emulator-5554")
    stop_monkey("DU2TAN15AJ049163")