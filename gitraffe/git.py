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

# DEPRECATED!!! BUT WE HAVE TO USE IT :(
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

def graph_convert_spaces(line):
    i = 0
    while line[i] != '*':
        i += 1
    i += 1
    line_lst = list(line)
    while i < len(line_lst):
        if line_lst[i] == ' ':
            line_lst[i] = '-'
        i +=1
    return ''.join(line_lst)

# THIS TRY FAILS, UNFORTUNATELLY, BUT MAY BE USEFUL
'''def get_graph():
    command = 'git log --graph --pretty=format:""'
    output = get_output_lines(command)
    save_log(command, output[0])
    graph = output[1]
    # debug
    print('>>RAW>>')
    for line in graph:
        print(line)
    j = 0
    for i in range(len(graph)):
        if not '*' in graph[i-j]:
            del graph[i-j]
            j += 1
        while graph[i-j][-1] == ' ':
            graph[i-j] = graph[i-j][:-1]
    if len(graph[0]) < len(graph[1]):
        graph[0] = graph_convert_spaces(graph[0])
        graph[0] += '-\\'
    for i in range(1, len(graph)-1):
        if len(graph[i]) < len(graph[i+1]) and len(graph[i+1]) == len(graph[i-1]) and (graph[i+1][-1] == '|' or graph[i+1][-1] == '*') and (graph[i-1][-1] == '|' or graph[i-1][-1] == '*'):
            graph[i] = graph_convert_spaces(graph[i])
            graph[i] += '_D'
        elif len(graph[i]) < len(graph[i+1]):
            graph[i] = graph_convert_spaces(graph[i])
            graph[i] += '-\\'
        elif len(graph[i]) < len(graph[i-1]):
            if graph[i-1][-1] != '/' or len(graph[i-1]) > len(graph[i])+2:
                graph[i] = graph_convert_spaces(graph[i])
                graph[i] += '-/'
    # debug
    print('>>MODIFIED>>')
    for i in range(len(graph)):
        print(graph[i])
    commits = get_commits()
    graph_with_data = []
    for i in range(len(graph)):
        commits[i].insert(0, graph[i])
        graph_with_data.append(commits[i])
    return graph_with_data'''

# ANOTHER TRY
'''def get_graph():
    command = 'git log --graph --pretty=format:""'
    output = get_output_lines(command)
    save_log(command, output[0])
    graph = output[1]
    # debug
    print('>>RAW>>')
    i = 0
    for line in graph:
        if '*' in line:
            print(str(i) + ' ' + line)
            i += 1
        else:
            print(line)
    for i in range(len(graph)):
        while graph[i][-1] == ' ':
            graph[i] = graph[i][:-1]
    # FIRST ROW
    next_line = graph[1]
    if not '*' in next_line:
        line_lst = list(graph[0])
        for j in range(1, len(next_line)):
            if next_line[j] == '\\':
                print('JAK TAM POLSKIE KUHWY?')
                if len(line_lst) == j and line_lst[-1] == '\\':
                    line_lst[-1] = '-'
                if j >= len(line_lst):
                    line_lst.append('-')
                    line_lst.append('\\')
                else:
                    line_lst[j-2] = '-'
                    line_lst[j-1] = '\\'
        graph[0] = ''.join(line_lst)
    # MIDDLE ROWS
    for i in range(1, len(graph)-1):
        previous_line = graph[i-1]
        next_line = graph[i+1]
        if not '*' in previous_line:
            line_lst = list(graph[i])
            for j in reversed(range(1, len(previous_line))):
                if previous_line[j] == '/':
                    if len(line_lst) == j and line_lst[-1] == '\\':
                        line_lst[-1] = '-'
                    if j >= len(line_lst):
                        line_lst.append('-')
                        line_lst.append('\\')
                    else:
                        line_lst[j-2] = '-'
                        line_lst[j-1] = '\\'
            graph[i] = ''.join(line_lst)
        if not '*' in next_line:
            line_lst = list(graph[i])
            for j in range(1, len(next_line)):
                if next_line[j] == '\\':
                    if len(line_lst) == j and line_lst[-1] == '\\':
                        line_lst[-1] = '-'
                    if j >= len(line_lst):
                        line_lst.append('-')
                        line_lst.append('\\')
                    else:
                        line_lst[j-2] = '-'
                        line_lst[j-1] = '\\'
            graph[i] = ''.join(line_lst)
    # LAST ROW TODO
    j = 0
    for i in range(len(graph)):
        if not '*' in graph[i-j]:
            del graph[i-j]
            j += 1
    # debug
    print('>>MODIFIED>>')
    for i in range(len(graph)):
        print(str(i) + ' ' + graph[i])
    commits = get_commits()
    graph_with_data = []
    for i in range(len(graph)):
        commits[i].insert(0, graph[i])
        graph_with_data.append(commits[i])
    return graph_with_data'''

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

def get_unstaged_files():
#    os.chdir(path)
    command = 'git diff --name-status'
    output = get_output_lines(command)
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
    command = 'git checkout -b ' + new_name + ' ' + branch
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
    system('git config --global user.name "' + username + '" && git config --global user.email "' + email + '"')

def remove_html(line):
    new = line.replace('<', '&lt;')
    new = new.replace('>', '&gt;')
    return new

def get_file_changes(flag, path ,commit, comparsion=None):
    try:
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
    except UnicodeDecodeError:
        return "Cannot decode this file"
    
def to_string(files, command):
    strfiles = " ".join(files)
    command += strfiles
    output = get_output_lines(command)
    save_log(command, output[0])

def git_add(files):
    to_string(files, 'git add ')
    
def git_check_out(files):
    to_string(files, 'git checkout ')
    