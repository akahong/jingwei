# coding=utf-8
import urllib2
import os, time

# 解析短信验证码
os.system("adb logcat -c")
cmd = "adb logcat -d |findstr E/SmsRec"
# time.sleep(30);
while (1):
    smscode = os.popen(cmd).read()
    # print smscode
    if (smscode != ""):
        smscode = smscode.split("验证码：")[1].split("，")[0]
        break;

print "验证码是:" + smscode