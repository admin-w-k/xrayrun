import re
import os
import sys
import time

for line in open("urls.txt"):
    name = line.replace('https://', '').replace('http://', '').replace('/', '').replace('\n', '').replace(':', '-')
    print(name)
    try:
        os.mkdir('scan_report')
    except:
        pass
    cmd = 'xray.exe webscan --basic-crawler {0}/ --html-output {1}.html'.format(line.replace('\n', ''), './scan_report/' + name)
    os.system(cmd.replace('\n', ''))
    time.sleep(0.2)
