import argparse
import subprocess
import time
import datetime

parser = argparse.ArgumentParser(description="This script read logfile defined in command line arg and print them")
parser.add_argument('-t', action='store_true')
parser.add_argument('--file', action='store')
arg = parser.parse_args()

with open(arg.file) as f:
    while(1):
        last_line = subprocess.check_output(['tail', '-1', f.name])

        if(arg.t):
            now = datetime.datetime.now()
            datetime_str = now.strftime(r"%Y-%m-%d %H:%M:%S")
            print(last_line + datetime_str)
        else:
            print(last_line)
        time.sleep(2)