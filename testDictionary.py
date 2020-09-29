# coding: utf-8
import subprocess
import sys

def Talk(CardNo, DeviceNo):
    cmd = '/home/pi/src/julius-4.4.2.1/julius/julius -C /home/pi/src/julius-4.4.2.1/dictation-kit-v4.4/am-gmm.jconf -nostrip -gram /home/pi/Desktop/Python_PJ/Greeting/greeting -input mic'
    subprocess.call(cmd.split())

if __name__ == "__main__":
    Talk(0,0)






