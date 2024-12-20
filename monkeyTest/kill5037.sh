#!/bin/bash

# 关闭回显
exec 1>/dev/null 2>&1

# 设置终端颜色和标题
tput setaf 1
echo "ReleaseAdbPort"
tput sgr0
echo "============================="
echo "*** liyu 2015-01-15 ***"
echo "***     v1.0.0     ***"
echo "============================="
echo "---------------------------"
echo "Checking adb port..."

# 检查 5037 端口是否被占用，并杀掉占用的进程
adb_port=$(lsof -i :5037 | grep "LISTEN" | awk '{print $2}')
if [ -n "$adb_port" ]; then
    for pid in $adb_port; do
        if [ "$pid" != "0" ]; then
            echo "Killing process with PID: $pid"
            kill -9 $pid
        fi
    done
fi

echo "---------------------------"
echo "adb port has been released!"
echo "---------------------------"

# 退出脚本
exit 0