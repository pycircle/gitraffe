from output import getoutput, getoutput_lines
from log import save_log

def stash():
    command = 'git stash'
    output = getoutput(command)
    save_log(command, output)
    return output

def stashes_list():
    command = 'git stash list'
    output = getoutput_lines(command)
    save_log(command, output[0])
    return output[1]

def apply_stash(stash):
    command = 'git stash apply ' + stash 
    save_log(command, getoutput(command))

def drop_stash(stash):
    command = 'git stash drop ' + stash
    output = getoutput(command)
    save_log(command, output)
    return output