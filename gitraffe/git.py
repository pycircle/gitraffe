from os import chdir, system
from subprocess import getoutput, Popen, PIPE, STDOUT
from symbol import comparison
from log import save_log

def get_output_lines(command):
    output = getoutput(command)
    lines = output.split('\n')
    return [output, lines]

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

def change_branch(branch):
    command = 'git checkout ' + branch
    save_log(command, getoutput(command))

def get_commits():
    command = 'git log --graph --pretty=format:"%h\n%s\n%an\n%ad"'
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
    graph_output = output[1]
    graph = []
    graph_log = ''
    i = 0
    graph_commit = []
    graph_commit.append(graph_output[0])
    for i in range(1, len(graph_output)):
        if '*' in graph_output[i]:
            graph.append(graph_commit)
            graph_commit = []
        graph_commit.append(graph_output[i])
    graph.append(graph_commit)
    for commit in graph:
        for line in commit:
            print(line)
    return graph

def diff(filename):
    command = 'git diff ' + filename
    output = getoutput(command)
    save_log(command, output)
    return output

# TODO -> HERE WE HAVE TO HANDLE PASS REQUESTS
def pull():
    command = 'git pull'
    output = getoutput(command)
    save_log(command, output)
    return output

def commit(message):
    command = 'git commit -m "%s"' % message
    output = getoutput(command)
    save_log(command, output)
    return output

# TODO -> HERE WE HAVE TO HANDLE PASS REQUESTS
def push():
    command = 'git push'
    output = getoutput(command)
    save_log(command, output)
    return output

def get_splited(output):
    files = []
    for line in output[1]:
        files.append(line.split())
    return files

def cherry_pick(branch, commit):
    change_branch(branch)
    command = 'git cherry-pick ' + commit
    output = getoutput(command)
    save_log(command, output)
    return output

def get_unstaged_files():
#    os.chdir(path)
    #command = 'git diff --name-status'
    command = 'git status -s'
    output = get_output_lines(command)
    files = output[1]
    print(files)
    print(len(files))
    j = 0
    for i in range(len(files)):
        if files[i-j][0] != ' ' and files[i-j][0] != '?':
            del files[i-j]
            j += 1
    save_log(command, output[0])
    return get_splited(output)

def get_staged_files():
    command = 'git diff --name-status --cached'
    output = get_output_lines(command)
    save_log(command, output[0])
    return get_splited(output)

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
    save_log(command, getoutput(command))
    
def change_remote_branch(branch, new_name):
    command = 'git checkout -b %s %s' % (new_name, branch)
    save_log(command, getoutput(command))

def delete_branch(branch):
    command = 'git branch -d ' + branch
    save_log(getoutput(command))

def get_settings():
    command_username = 'git config --global user.name'
    command_email = 'git config --global user.email'
    settings = []
    output_username = getoutput(command_username)
    output_email = getoutput(command_email)
    save_log(command_username, output_username)
    save_log(command_email, output_email)
    settings.append(output_username)
    settings.append(output_email)
    return settings

def set_settings(username, email):
    system('git config --global user.name "%s" && git config --global user.email "%s"' % (username, email))

def remove_html(line):
    new = line.replace('<', '&lt;')
    new = new.replace('>', '&gt;')
    return new

def get_file_changes(flag, path ,commit, comparsion=None):
    try:
        out = '<pre>'
        if flag == 'M' or flag == 'MM':
            command = 'git diff %s:%s %s:%s' % (comparsion, path, commit, path)
            output = get_output_lines(command)
            save_log(command, output[0])
            for line in output[1][4:]:
                line = remove_html(line)
                if line[0]=='-':
                    line = '<font color="RED"> %s</font>' % (line)
                elif line[0]=='+':
                    line = '<font color="GREEN"> %s</font>' % (line)
                out += line + '\n'
            out += '</pre>'
            return out
        elif flag=='A':
            command = 'git show %s:%s' % (commit, path)
            output = get_output_lines(command)
            save_log(command, output[0])
            for line in output[1]:
                line = remove_html(line)
                line = '<font color="GREEN"> + %s </font>' % (line)
                out += line + '\n'
            out += '</pre>'
            return out
        elif flag=='D':
            command = 'git show %s:%s' % (comparsion, path)
            output = get_output_lines(command)
            save_log(command, output[0])
            for line in output[1]:
                line = remove_html(line)
                line = '<font color="RED"> - %s </font>' % (line)
                out += line + '\n'
            out += '</pre>'
            return out
    except UnicodeDecodeError:
        return "Cannot decode this file"
    
def to_string(files, command):
    strfiles = " ".join(files)
    command += strfiles
    output = getoutput(command)
    save_log(command, output)

def git_add(file):
    #to_string(files, 'git add ')
    command = 'git add ' + file
    output = getoutput(command)
    save_log(command, output)

def git_rm(files):
    #to_string(files, 'git rm ')
    command = 'git rm ' + file
    output = getoutput(command)
    save_log(command, output)

def git_reset_head(files):
    to_string(files, 'git reset HEAD ')

def git_rm_cached(files):
    to_string(files, 'git rm --cached ')

def git_check_out(files):
    to_string(files, 'git checkout ')
    
