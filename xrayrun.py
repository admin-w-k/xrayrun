import re
import os
import sys
import time

for line in open("urls.txt"):
    name = line.replace('https://', '').replace('http://', '').replace('/', '').replace('\n', '').replace(':', '-')
    print(name)
    os.mkdir('scan_report')
    cmd = 'xray.exe webscan --basic-crawler {0}/ --html-output {1}.html'.format(line.replace('\n', ''), './scan_report/' + name)
    os.system(cmd.replace('\n', ''))
    time.sleep(0.2)
    



'''
def scan():
    file = open("urls.txt")
    urls = []
    for line in file:
        lines = line.strip('\n')
        urls.append(lines)
    file.close()
    for url in urls:
        name = url.replace('https://', '').replace('http://', '').replace('/', '').replace('\n', '').replace(':', '-')
        try:
            os.mkdir('scan_report')
        except:
            pass
        cmd = 'xray.exe webscan --basic-crawler {0}/ --html-output {1}.html'.format(url.replace('\n', ''), './scan_report/' + name)
        os.system(cmd.replace('\n', ''))
        time.sleep(0.2)

if __name__ == "__main__":
    scan()
'''
