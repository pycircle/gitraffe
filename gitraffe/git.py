import os
import subprocess

def get_output_lines(command):
    output = subprocess.getoutput(command)
    lines = output.split('\n')
    return lines

def check_repository(path):
    os.chdir(path)
    output = subprocess.getoutput('git rev-parse --git-dir')
    if output == '.git':
        return (True, path)
    elif output.endswith('.git'):
        return (True, output[:-5])
    else: return (False, '')

def open_repository(path):
    os.chdir(path)

def clone_repository(source, destination):
    args = ['git' ,'clone', source, destination]
    child = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    child.wait()
    if child.returncode!=0:
        info = ""
        for x in child.stdout.readlines():
            info += x.decode("utf-8")
        return (False, info)
    else: return (True, "")

def change_branch(branch):
    command = 'git checkout ' + branch
    os.system(command)

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
    lines = get_output_lines(command)
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

def get_modified(path):
    os.chdir(path)
    command = 'git status'
    lines = get_output_lines(command)
    modified_files = []
    for line in lines:
        if 'modified:' in line:
            words = line.split()
            modified_files.append(words[words.index('modified:')+1])
    return modified_files

def get_local_branches():
    command = 'git branch'
    lines = get_output_lines(command)
    branches = []
    for line in lines:
        branches.append(line[2:])
    return branches

def get_remote_branches():
    command = 'git branch -r'
    lines = get_output_lines(command)
    branches = []
    for line in lines:
        branches.append(line[2:].split(' ')[0])
    return branches
    
