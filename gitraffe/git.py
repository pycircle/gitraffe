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

def get_commits():
    command = 'git log --pretty=format:"%h\n%s\n%an <%ae>\n%ad"'
    lines = get_output_lines(command)
    commits = []
    i = 0
    commit = []
    for line in lines:
        commit.append(line)
        i += 1
        if i == 4:
            i = 0
            commits.append(commit)
            commit = []
    return commits

def get_graph():
    command = 'git log --graph --pretty=format:""'
    lines = get_output_lines(command)
    commits = get_commits()
    graph = []
    i = 0
    for line in lines:
        if '*' in line:
            commits[i].insert(0, line)
            graph.append(commits[i])
            i += 1
        else:
            graph.append([line, '', '', '', ''])
    return graph

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
#    os.chdir(path)
    command = 'git status'
    lines = get_output_lines(command)
    modified_files = []
    for line in lines:
        if 'modified:' in line:
            words = line.split()
            modified_files.append(words[words.index('modified:')+1])
    return modified_files

def get_files(commit):
    command = 'git show --pretty="format:" --name-status ' +  commit
    lines = get_output_lines(command)
    files = []
    for line in lines[1:]:
        files.append(line.split('\t'))
    return files

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

def get_current_branch():
    command = 'git branch'
    lines = get_output_lines(command)
    for line in lines:
        if '*' in line:
            return line[2:]

def change_local_branch(branch):
    command = 'git checkout ' + branch
    subprocess.getoutput(command)
    
def change_remote_branch(branch, new_name):
    command = 'git checkout -b ' + new_name + ' ' + branch
    subprocess.getoutput(command)

def delete_branch(branch):
    command = 'git branch -d ' + branch
    subprocess.getoutput(command)
