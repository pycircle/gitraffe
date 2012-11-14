from output import getoutput, getoutput_lines
from log import save_log

def get_splited(output):
    files = []
    for line in output[1]:
        files.append(line.split())
    return files

def to_string(files, command):
    strfiles = " ".join(files)
    command += strfiles
    output = getoutput(command)
    save_log(command, output)

def get_unstaged_files():
    command = 'git status -s'
    output = getoutput_lines(command)
    files = output[1]
    j = 0
    if len(files) > 0 and files[0] != '':
        for i in range(len(files)):
            if files[i-j][0] != ' ' and files[i-j][0] != '?':
                del files[i-j]
                j += 1
    save_log(command, output[0])
    return get_splited(output)

def get_staged_files():
    command = 'git diff --name-status --cached'
    output = getoutput_lines(command)
    save_log(command, output[0])
    return get_splited(output)

def git_add(file):
    command = 'git add ' + file
    output = getoutput(command)
    save_log(command, output)

def git_rm(files):
    command = 'git rm ' + file
    output = getoutput(command)
    save_log(command, output)

def git_reset_head(files):
    to_string(files, 'git reset HEAD ')

def git_rm_cached(files):
    to_string(files, 'git rm --cached ')

def git_check_out(file):
    command = 'git checkout -- ' + file
    output = getoutput(command)
    save_log(command, output)

def clean(file):
    command = 'git clean -f ' + file
    output = getoutput(command)
    save_log(command, output)

def commit(message):
    command = 'git commit -m "%s"' % message
    output = getoutput(command)
    save_log(command, output)
    return output