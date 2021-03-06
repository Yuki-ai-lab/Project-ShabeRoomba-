# coding: utf-8
import subprocess 
from datetime import datetime

def jtalk(txt):
    open_jtalk = ["open_jtalk"]
    mech = ["-x" , "/var/lib/mecab/dic/open-jtalk/naist-jdic"]
    htsvoice = ["-m" , "/usr/share/hts-voice/nitech-jp-atr503-m001/nitech_jp_atr503_m001.htsvoice"]
    speed = ["-r" ,  "1.0"]
    outwav = ["-ow" , "/home/pi/Downloads/open_jtalk_test.wav"]
    volume = ["-fm" , "1.0"]

    cmd = open_jtalk + mech + htsvoice + speed + outwav + volume
    c = subprocess.Popen(cmd, stdin=subprocess.PIPE)      #標準入力許可
    c.stdin.write(txt)
    c.stdin.close()
    c.wait()
    aplay = ["aplay", "-q", "/home/pi/Downloads/open_jtalk_test.wav"]
    wr = subprocess.Popen(aplay)


def say_datetime():
    d = datetime.now()
    text = "%s月%s日、%s時%s分%s秒" % (d.month, d.day, d.hour, d.minute, d.second)
    jtalk(text)

if __name__ == "__main__":
    say_datetime()
    
