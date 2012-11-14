import subprocess

def getoutput(command):
    try:
        output = subprocess.getoutput(command)
        return output
    except IOError:
        return getoutput(command)

def getoutput_lines(command):
    output = getoutput(command)
    lines = output.split('\n')
    return [output, lines]