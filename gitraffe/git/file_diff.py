from os.path import isdir
from output import getoutput_lines
from log import save_log

def remove_html(line):
    new = line.replace('<', '&lt;')
    new = new.replace('>', '&gt;')
    return new

def get_file_changes(base_command, flag, path, commit=None, comparsion=None):
    try:
        out = '<pre>'
        if 'M' in flag:
            if commit:
                command = base_command + '%s:%s %s:%s' % (comparsion, path, commit, path)
            else:
                command = base_command + path
            #print(base_command, flag, path, commit, comparsion)
            output = getoutput_lines(command)
            save_log(command, output[0])
            if not output[1][4:] and 'Binary' in "".join(output[1]): return "Cannot decode this file"
            #print(output[1][2])
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
        elif 'A' in flag or flag == '??':
            if commit: 
                command = 'git show %s:%s' % (commit, path)
                output = getoutput_lines(command)
                save_log(command, output[0])
            else:
                if isdir(path):
                    save_log('isdir(path)', 'True')
                    return '<pre>This is a directory</pre>'
                output = open(path).read()
                save_log("open(path).read()", output)
                output = [None, output.split("\n")]
            for line in output[1]:
                line = remove_html(line)
                line = '<font color="GREEN"> + %s </font>' % (line)
                out += line + '\n'
            out += '</pre>'
            return out
        elif 'D' in flag:
            command = 'git show %s:%s' % (comparsion, path)
            output = getoutput_lines(command)
            save_log(command, output[0])
            for line in output[1]:
                line = remove_html(line)
                line = '<font color="RED"> - %s </font>' % (line)
                out += line + '\n'
            out += '</pre>'
            return out
    except UnicodeDecodeError:
        return "Cannot decode this file"

def get_staged_file_changes(flag, path, commit=None, comparsion=None):
    return get_file_changes('git diff --cached ', flag, path, commit, comparsion)

def get_unstaged_file_changes(flag, path, commit=None, comparsion=None):
    return get_file_changes('git diff ', flag, path, commit, comparsion)
