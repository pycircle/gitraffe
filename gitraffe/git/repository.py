from os import chdir
from subprocess import Popen, PIPE, STDOUT
from output import getoutput
from log import save_log

def check_repository(path):
    chdir(path)
    command = 'git rev-parse --git-dir'
    output = getoutput(command)
    save_log(command, output)
    if output == '.git':
        return (True, path)
    elif output.endswith('.git'):
        return (True, output[:-5])
    else: return (False, '')

def open_repository(path):
    chdir(path)

def clone_repository(source, destination):
    args = ['git' ,'clone', source, destination]
    child = Popen(args, stdout=PIPE, stderr=STDOUT)
    child.wait()
    if child.returncode!=0:
        info = ""
        for x in child.stdout.readlines():
            info += x.decode("utf-8")
        return (False, info)
    else: return (True, "")