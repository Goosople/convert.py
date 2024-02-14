#!/usr/bin/env python3
import os
import sys
import re
errstr = "\033[31m"
sucstr = "\033[32m"
rststr = "\033[0m"
print("Checking ffmpeg version...")

if os.system("ffmpeg -version"):
    print(errstr+"Error: ffmpeg not installed"+rststr)
    if sys.platform.startswith('win32'):
        if sys.getwindowsversion().major >= 10:
            print("Trying to install ffmpeg...")
            if os.system("winget install ffmpeg"):
                print("Please install ffmpeg from https://ffmpeg.org/download.html#build-windows")
        else:
            print("Please install ffmpeg from https://ffmpeg.org/download.html#build-windows")
    elif sys.platform.startswith('linux'):
        print("Trying to install ffmpeg...")
        if os.system("sudo apt install ffmpeg"):
            if os.system("sudo yum install ffmpeg"):
                print("Please install ffmpeg from https://ffmpeg.org/download.html#build-linux")
    elif sys.platform.startswith('darwin'):
        print("Please install ffmpeg from https://ffmpeg.org/download.html#build-mac")

else:
    if len(sys.argv) == 1:
        print(errstr+'Error: no input dirs'+rststr +
              '\nUsage: %s <dir> <format>'%sys.argv[0])
    elif len(sys.argv) == 2:
        print(errstr+'Error: no format specified' +
              rststr+'\nUsage: %s <dir> <format>'%sys.argv[0])
    elif len(sys.argv) == 3:
        ol = os.listdir(sys.argv[1])
        os.chdir(sys.argv[1])
        try:
            if input("Remove all existing %s files? [y/N] " % sys.argv[2]) in 'yY':
                for f in ol:
                    if f.endswith(sys.argv[2]):
                        os.remove(f)
                ol = os.listdir(sys.argv[1])
                print(sucstr+"All existing %s files is removed." % sys.argv[2]+rststr)
        except KeyboardInterrupt:
            exit()
        print("Files to be converted: ", ol)
        for o in ol:
            p = re.sub("\.....?$", '.'+sys.argv[2], o)
            os.system("ffmpeg -i \"%s\" -c:v copy -q:a 0 \"%s\"" % (o, p))
        print(sucstr+"Process complete."+rststr)
    else:
        print(errstr+'Error: too many arguments' +
              rststr+'\nUsage: %s <dir> <format>'%sys.argv[0])
