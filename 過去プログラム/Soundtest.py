from subprocess  import call

cmd = "mpg321 /home/pi/Downloads/BGMtest.mp3"
call(cmd.split())
