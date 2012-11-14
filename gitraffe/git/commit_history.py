from output import getoutput, getoutput_lines
from log import save_log

def get_commits():
    command = 'git log --graph --pretty=format:"%h\n%s\n%an\n%ad"'
    output = getoutput_lines(command)
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
        output = getoutput(command)
        if output != '':
            break
        commits[i][1] = '[not pushed] ' + commits[i][1]
        i += 1
    return commits

def get_graph():
    command = 'git log --graph --pretty=format:""'
    output = getoutput_lines(command)
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
    output = getoutput(command)
    save_log(command, output)
    return output

def get_files(commit):
    command = 'git show --pretty="format:" --name-status ' +  commit
    output = getoutput_lines(command)
    save_log(command, output[0])
    files = []
    for line in output[1][1:]:
        files.append(line.split('\t'))
    return files