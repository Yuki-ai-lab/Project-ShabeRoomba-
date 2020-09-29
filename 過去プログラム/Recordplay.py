# coding: utf-8
from subprocess  import call

def CheckNo():
    cmd = "arecord -l"
    call(cmd.split())

def CheckVo():
    cmd = "alsamixer"
    call(cmd.split())    


def Record(Name, Dir, CardNo, DeviceNo, Time):
    if Time != 0:
        cmd = "arecord -D plughw:" + str(CardNo) + "," + str(DeviceNo) + " -d " + str(Time) + " -f cd " + Dir + "/" + Name + ".wav"
    else:
        cmd = "arecord -D plughw:" + str(CardNo) + "," + str(DeviceNo) + " -f cd " + Dir + "/" + Name + ".wav"
    call(cmd.split())


def Play(Name, Dir):
    cmd = "aplay " + Dir + "/" + Name + ".wav"
    call(cmd.split())




if __name__ == "__main__":
    
    #Record("Recordtest01", "/home/pi/Music", 0,0,15)
    #Play("Recordtest01", "/home/pi/Music")
    #CheckNo()

    Play("2019.0507.225406","/home/pi/Desktop")
