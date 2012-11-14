from output import getoutput, getoutput_lines
from log import save_log

def change_branch(branch):
    command = 'git checkout ' + branch
    save_log(command, getoutput(command))

def cherry_pick(window, branch, commit):
    change_branch(branch)
    command = 'git cherry-pick ' + commit
    output = getoutput(command)
    save_log(command, output)
    return output

def get_local_branches():
    command = 'git branch'
    output = getoutput_lines(command)
    save_log(command, output[0])
    branches = []
    for line in output[1]:
        branches.append(line[2:])
    return branches

def get_remote_branches():
    command = 'git branch -r'
    output = getoutput_lines(command)
    save_log(command, output[0])
    branches = []
    for line in output[1]:
        branches.append(line[2:].split(' ')[0])
    return branches

def get_current_branch():
    command = 'git branch'
    output = getoutput_lines(command)
    save_log(command, output[0])
    for line in output[1]:
        if '*' in line:
            return line[2:]

def change_local_branch(branch):
    command = 'git checkout ' + branch
    save_log(command, getoutput(command))

def change_remote_branch(branch, new_name):
    command = 'git checkout -b %s %s' % (new_name, branch)
    output = getoutput(command)
    save_log(command, output)
    return output

def delete_branch(branch):
    command = 'git branch -d ' + branch
    output = getoutput(command)
    save_log(command, output)
    return output

def create_branch(window, branch):
    command = 'git checkout -b ' + branch
    save_log(command, getoutput(command))
    url = get_url()
    additional_args = []
    if url.startswith("git@"):
        additional_args.append('origin')
    additional_args.append(branch)
    return push(window, additional_args)