from subprocess import getoutput
from os import system
from os.path import exists, expanduser

def get_ssh_key():
    if exists((expanduser('~/.ssh/id_rsa.pub'))):
        command = 'cat ~/.ssh/id_rsa.pub'
        output = getoutput(command)
        return output
    return 'You don\'t have SSH key. Click \"Generate new key\"!'

def backup():
    system('mkdir ~/.ssh/backup')
    system('cp ~/.ssh/id_rsa* ~/.ssh/backup')
    system('rm -f ~/.ssh/id_rsa*')
    

def generate_new_ssh_key(email, password):
    print(type(email))
    print(type(password))
    #if exists((expanduser('~/.ssh/id_rsa.pub'))) or exists((expanduser('~/.ssh/id_rsa.pub'))):
    output = getoutput('ssh-keygen -t rsa -C "%s" -f ~/.ssh/id_rsa -N %s' % (email, password))
    return output
