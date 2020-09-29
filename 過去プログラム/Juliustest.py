# coding: utf-8
from subprocess  import call

def Talk(CardNo, DeviceNo):
    #cmd = "ALSADEV=plughw:" + str(CardNo) + "," + str(DeviceNo) + " /home/pi/julius/julius-4.4.2.1/julius/julius -C home/pi/julius/julius-kit/dictation-kit-v4.4/main.jconf -C home/pi/julius/julius-kit/dictation-kit-v4.4/am-gmm.jconf -nostrip"
    cmd = "ALSADEV='plughw:0,0' ~/julius/julius-4.5/julius/julius -C ~/julius/julius-kit/dictation-kit-4.5/main.jconf -C ~/julius/julius-kit/dictation-kit-4.5/am-gmm.jconf  -nostrip -charconv UTF-8 eucjp"
    call(cmd.split())
         

if __name__ == "__main__":
    Talk(0,0)


