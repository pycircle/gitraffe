from os.path import expanduser
from datetime import datetime

def clear_log():
    log_file = open(expanduser('~/.gitraffe/log'), 'w')
    log_file.close()

def save_log(command, output):
    log_file = open(expanduser('~/.gitraffe/log'), 'a')
    log_file.write(datetime.now().strftime("%Y-%m-%d %H:%M") + '\n>> COMMAND >>\n' + command + '\n>> OUTPUT >>\n' + output + '\n\n')
    log_file.close()

def get_log():
    log_file = open(expanduser('~/.gitraffe/log'), 'r')
    contents = log_file.read()
    log_file.close()
    return contents
