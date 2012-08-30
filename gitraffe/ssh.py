from subprocess import getoutput
from os import system
from os.path import exists, expanduser

def get_ssh_key():
    if exists((expanduser('~/.ssh/id_rsa.pub'))):
        command = 'cat ~/.ssh/id_rsa.pub'
        output = getoutput(command)
        return output
    return 'You don\'t have SSH key. Click \"Generate new key\"!' 

# TODO -> HERE WE MUST HANDLE PASS REQUEST
def generate_new_ssh_key(email):
    if exists((expanduser('~/.ssh/id_rsa.pub'))) or exists((expanduser('~/.ssh/id_rsa.pub'))):
        system('mkdir ~/.ssh/backup')
        system('cp ~/.ssh/id_rsa* ~/.ssh/backup')
    output = getoutput('ssh-keygen -t rsa -C "' + email + '"')
    return output
