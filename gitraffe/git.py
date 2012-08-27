import os
import subprocess
from symbol import comparison
from log import save_log

def get_output_lines(command):
    output = subprocess.getoutput(command)
    lines = output.split('\n')
    return [output, lines]

def check_repository(path):
    os.chdir(path)
    command = 'git rev-parse --git-dir'
    output = subprocess.getoutput(command)
    save_log(command, output)
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
    save_log(command, subprocess.getoutput(command))

def get_commits():
    command = 'git log --graph --pretty=format:"%h\n%s\n%an <%ae>\n%ad"'
    output = get_output_lines(command)
    save_log(command, output[0])
    commits = []
    i = 0
    commit = []
    for line in output[1]:
        j = 0
        for char in line:
            if char == '*' or char == '|' or char == '\\' or char == '/' or char == '_' or char == ' ':
                j += 1
            else:
                break
        commit.append(line[j:])
        i += 1
        if i == 4:
            i = 0
            commits.append(commit)
            commit = []
    return commits

def get_graph():
    command = 'git log --graph --pretty=format:""'
    output = get_output_lines(command)
    save_log(command, output[0])
    commits = get_commits()
    graph = []
    graph_log = ''
    i = 0
    for line in output[1]:
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
    save_log(command, output)
    return output

# TODO -> HERE WE HAVE TO HANDLE PASS REQUESTS
def pull():
    command = 'git pull'
    output = subprocess.getoutput(command)
    save_log(command, output)
    return output

def commit(message):
    command = 'git commit -m "' + message + '"'
    output = subprocess.getoutput(command)
    save_log(command, output)
    return output

# TODO -> HERE WE HAVE TO HANDLE PASS REQUESTS
def push():
    command = 'git push'
    output = subprocess.getoutput(command)
    save_log(command, output)
    return output

def get_local_chanegs():
#    os.chdir(path)
    command = 'git status --short'
    output = get_output_lines(command)
    save_log(command, output[0])
    changes = []
    for line in output[1]:
        changes.append(line)
    return changes

def get_files(commit):
    command = 'git show --pretty="format:" --name-status ' +  commit
    output = get_output_lines(command)
    save_log(command, output[0])
    files = []
    for line in output[1][1:]:
        files.append(line.split('\t'))
    return files

def get_local_branches():
    command = 'git branch'
    output = get_output_lines(command)
    save_log(command, output[0])
    branches = []
    for line in output[1]:
        branches.append(line[2:])
    return branches

def get_remote_branches():
    command = 'git branch -r'
    output = get_output_lines(command)
    save_log(command, output[0])
    branches = []
    for line in output[1]:
        branches.append(line[2:].split(' ')[0])
    return branches

def get_current_branch():
    command = 'git branch'
    output = get_output_lines(command)
    save_log(command, output[0])
    for line in output[1]:
        if '*' in line:
            return line[2:]

def change_local_branch(branch):
    command = 'git checkout ' + branch
    save_log(command, subprocess.getoutput(command))
    
def change_remote_branch(branch, new_name):
    command = 'git checkout -b ' + new_name + ' ' + branch
    save_log(command, subprocess.getoutput(command))

def delete_branch(branch):
    command = 'git branch -d ' + branch
    save_log(subprocess.getoutput(command))

def get_settings():
    command_username = 'git config --global user.name'
    command_email = 'git config --global user.email'
    settings = []
    output_username = subprocess.getoutput(command_username)
    output_email = subprocess.getoutput(command_email)
    save_log(command_username, output_username)
    save_log(command_email, output_email)
    settings.append(output_username)
    settings.append(output_email)
    return settings

def set_settings(username, email):
    os.system('git config --global user.name "' + username + '" && git config --global user.email "' + email + '"')

def remove_html(line):
    new = line.replace('<', '&lt;')
    new = new.replace('>', '&gt;')
    return new

def get_file_changes(flag, path ,commit, comparsion=None):
    out = '<pre>'
    if flag == 'M' or flag == 'MM':
        command = 'git diff '+ comparsion + ':' +path + ' '+ commit +':'+path
        output = get_output_lines(command)
        save_log(command, output[0])
        for line in output[1][4:]:
            line = remove_html(line)
            if line[0]=='-':
                line = '<font color="RED"> '+ line + '</font>'
            elif line[0]=='+':
                line = '<font color="GREEN"> '+ line + '</font>'
            out += line + '\n'
        out += '</pre>'
        return out
    elif flag=='A':
        command = 'git show ' + commit + ':' + path
        output = get_output_lines(command)
        save_log(command, output[0])
        for line in output[1]:
            line = remove_html(line)
            line = '<font color="GREEN"> + ' + line + ' </font>'
            out += line + '\n'
        out += '</pre>'
        return out
    elif flag=='D':
        command = 'git show ' + comparsion + ':' + path
        output = get_output_lines(command)
        save_log(command, output[0])
        for line in output[1]:
            line = remove_html(line)
            line = '<font color="RED"> - ' + line + ' </font>'
            out += line + '\n'
        out += '</pre>'
        return out
