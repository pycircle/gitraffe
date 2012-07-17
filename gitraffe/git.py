import os
import subprocess

def check_repository(path):
    os.chdir(path)
    output = subprocess.getoutput('git rev-parse --git-dir')
    if output == '.git':
        return (True, path)
    elif output[-4:] == '.git': 
        return (True, output[:-5])
    else: return (False, '')

def open_repository(path):
    os.chdir(path)

def change_branch(branch):
    command = 'git checkout ' + branch
    os.system(command)

def parse_branch(line):
    i = 0
    for x in line:
        if x != ' ' and x != '*':
            return line[i:]
        else:
            i += 1

def get_local_branches():
    command = 'git branch'
    output = subprocess.getoutput(command)
    lines = output.split('\n')
    branches = []
    for line in lines:
        branches.append(parse_branch(line))
    return branches

def get_branches():
    branches = []
    branches.append(get_local_branches())
    return branches

def parse_graph_line(line):
    tree = ''
    i = 0
    for x in line:
        if x == '*' or x == '|' or x == '\\' or x == '/' or x == ' ':
            tree += x
            i += 1
        else:
            break
    tree = tree[:-1]
    line = line[i:]
    commit = line.split(' ', 1)
    commit.insert(0, tree)
    return commit

def get_graph():
    command = 'git log --graph --oneline'
    output = subprocess.getoutput(command)
    lines = output.split('\n')
    commits = []
    for line in lines:
        commit = parse_graph_line(line)
        commits.append(commit)
    return commits

def diff(filename):
    command = 'git diff ' + filename
    output = subprocess.getoutput(command)
    return output

# TODO -> HERE WE HAVE TO HANDLE MERGES
def pull():
    command = 'git pull'
    output = subprocess.getoutput(command)

def commit(message):
    command = 'git commit -m "' + message + '"'
    output = subprocess.getoutput(command)

# TODO -> HERE WE HAVE TO HANDLE MERGES
def push(branch):
    command = 'git push ' + branch
    output = subprocess.getoutput(command)
