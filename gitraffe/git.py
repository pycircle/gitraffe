from os import chdir, system
from subprocess import getoutput, Popen, PIPE, STDOUT
from symbol import comparison
from log import save_log
import sys
from threading import Thread
from queue import Queue, Empty

def ext_getoutput(command):
    try:
        output = getoutput(command)
        return output
    except IOError:
        return ext_getoutput(command)

def get_output_lines(command):
    output = ext_getoutput(command)
    lines = output.split('\n')
    return [output, lines]

def check_repository(path):
    chdir(path)
    command = 'git rev-parse --git-dir'
    output = ext_getoutput(command)
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
    i = 0
    while i < len(commits):
        command = 'git branch -r --contains ' + commits[i][0]
        output = ext_getoutput(command)
        if output != '':
            break
        commits[i][1] = '[not pushed] ' + commits[i][1]
        i += 1
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
    return graph

def diff(filename):
    command = 'git diff ' + filename
    output = ext_getoutput(command)
    save_log(command, output)
    return output

# TODO -> HERE WE HAVE TO HANDLE PASS REQUESTS
def pull():
    command = 'git pull'
    output = ext_getoutput(command)
    save_log(command, output)
    return output

def commit(message):
    command = 'git commit -m "%s"' % message
    output = ext_getoutput(command)
    save_log(command, output)
    return output

def get_url():
    command = "git config --get remote.origin.url"
    output = ext_getoutput(command)
    save_log(command, output)
    return output

def push(window, additional_args=None):
    from wrappers.authorization_wrapper import AuthorizationWrapper
    output = get_url()
    args = ['git', 'push']
    if output.startswith("git@"):
        pass
    elif '@' in output:
        dialog = AuthorizationWrapper(window)
        dialog.ui.Username_lineEdit.setText("Not needed")
        dialog.ui.Username_lineEdit.setReadOnly(True)
        dialog.exec_()
        splited = output.split('@')
        url = "%s:%s@%s" % (splited[0], dialog.password, splited[1])
        if dialog.password == "":
            return "Password is needed"
        args.append(url)
    else:
        splited = output.split('//')
        dialog = AuthorizationWrapper(window)
        dialog.exec_()
        url = "%s//%s:%s@%s" % (splited[0], dialog.username, dialog.password, splited[1])
        if dialog.username == "" or dialog.password == "":
            return "Password or username is needed"
        args.append(url)
    if additional_args != None:
        for arg in additional_args:
            args.append(arg)
    child = Popen(args, stdout=PIPE, stderr=STDOUT)
    child.wait()
    info = ""
    for x in child.stdout.readlines()[1:]:
        info += x.decode("utf-8")
    if info == "":
        info = "Everything up-to-date"
    save_log(" ".join(args[:-1]), info)
    return info

def get_splited(output):
    files = []
    for line in output[1]:
        files.append(line.split())
    return files

def cherry_pick(window, branch, commit):
    change_branch(branch)
    command = 'git cherry-pick ' + commit
    output = ext_getoutput(command)
    save_log(command, output)
    return output

def get_unstaged_files():
    command = 'git status -s'
    output = get_output_lines(command)
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
    save_log(command, ext_getoutput(command))

def change_remote_branch(branch, new_name):
    command = 'git checkout -b %s %s' % (new_name, branch)
    save_log(command, ext_getoutput(command))

def delete_branch(branch):
    command = 'git branch -d ' + branch
    save_log(command, ext_getoutput(command))

def create_branch(window, branch):
    command = 'git checkout -b ' + branch
    save_log(command, ext_getoutput(command))
    url = get_url()
    additional_args = []
    if url.startswith("git@"):
        additional_args.append('origin')
    additional_args.append(branch)
    return push(window, additional_args)

def get_settings():
    command_username = 'git config --global user.name'
    command_email = 'git config --global user.email'
    settings = []
    output_username = ext_getoutput(command_username)
    output_email = ext_getoutput(command_email)
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
                if len(line) > 0:
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
    output = ext_getoutput(command)
    save_log(command, output)

def git_add(file):
    command = 'git add ' + file
    output = ext_getoutput(command)
    save_log(command, output)

def git_rm(files):
    command = 'git rm ' + file
    output = ext_getoutput(command)
    save_log(command, output)

def git_reset_head(files):
    to_string(files, 'git reset HEAD ')

def git_rm_cached(files):
    to_string(files, 'git rm --cached ')

def git_check_out(file):
    command = 'git checkout -- ' + file
    output = ext_getoutput(command)
    save_log(command, output)

def clean(file):
    command = 'git clean -f ' + file
    output = ext_getoutput(command)
    save_log(command, output)

def stashes_list():
    command = 'git stash list'
    output = get_output_lines(command)
    save_log(command, output[0])
    return output[1]

def apply_stash(stash):
    command = 'git stash apply ' + stash 
    save_log(command, ext_getoutput(command))

def drop_stash(stash):
    command = 'git stash drop ' + stash
    output = ext_getoutput(command)
    save_log(command, output)
    return output