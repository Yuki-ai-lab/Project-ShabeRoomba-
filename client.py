# coding: utf-8
# python 2.7.13
import socket
import string
import sys,codecs

import subprocess 
from datetime import datetime

def jtalk(txt):
    open_jtalk = ["open_jtalk"]
    mech = ["-x" , "/var/lib/mecab/dic/open-jtalk/naist-jdic"]
    htsvoice = ["-m" , "/usr/share/hts-voice/miku/miku2.htsvoice"]
    speed = ["-r" ,  "1.0"]
    outwav = ["-ow" , "/home/pi/Downloads/open_jtalk_test.wav"]
    tone = ["-fm" , "5.0"]
    intonation=["-jf" , "0.5"]

    cmd = open_jtalk + mech + htsvoice + speed + outwav + tone + intonation
    c = subprocess.Popen(cmd, stdin=subprocess.PIPE)    
    c.stdin.write(txt)
    c.stdin.close()
    c.wait()
    aplay = ["aplay", "-q", "/home/pi/Downloads/open_jtalk_test.wav"]
    wr = subprocess.Popen(aplay)

def say_datetime():
    d = datetime.now()
    text = "%s月%s日、%s時%s分%s秒" % (d.month, d.day, d.hour, d.minute, d.second)
    jtalk(text)

def say_comment(c):
    jtalk(c)

host = "127.0.0.1"
port = 10500
buffer = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

try:
    while True:
        data = ""
        while (string.find(data, "\n.") == -1 ):
            data = data + sock.recv(buffer)

        strTemp = ""
        for line in data.split('\n'):
            index = line.find('WORD="')
            if index != -1:
                line = line[index+6:line.find('"',index+6)]
                strTemp = strTemp + line
                
            #str文字列(utf-8)→unicode文字列→str文字列(eucjp)
        if "こんばんは".decode('utf-8').encode('eucjp') in strTemp:
            #str文字列(utf-8)
            say_comment("こんばんは。夕食は食べましたか？")
        
        elif "こんにちは".decode('utf-8').encode('eucjp') in strTemp:
            say_comment("こんにちは。体調はいかがですか？")
            
        elif "さよなら".decode('utf-8').encode('eucjp') in strTemp:
            say_comment("また会える日を楽しみにしております。")
                
except KeyboardInterrupt:
    print("finish")