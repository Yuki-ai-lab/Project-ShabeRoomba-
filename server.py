import subprocess
import sys

def Talk(CardNo, DeviceNo):
    cmd = '/home/pi/src/julius-4.4.2.1/julius/julius -C /home/pi/src/julius-4.4.2.1/dictation-kit-v4.4/am-gmm.jconf -nostrip -gram /home/pi/Desktop/Python_PJ/Greeting/greeting -input mic -module'
    subprocess.call(cmd.split())

if __name__ == "__main__":
    try:
        Talk(0,0)
    except KeyboardInterrupt:
        print("finish")
            
