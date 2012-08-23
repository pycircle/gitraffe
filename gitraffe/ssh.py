import subprocess
import os

def get_ssh_key():
    if os.path.exists((os.path.expanduser('~/.ssh/id_rsa.pub'))):
        command = 'cat ~/.ssh/id_rsa.pub'
        output = subprocess.getoutput(command)
        return output
    return 'You don\'t have SSH key. Click \"Generate new key\"!' 

# TODO -> HERE WE MUST HANDLE PASS REQUEST
def generate_new_ssh_key(email):
    if os.path.exists((os.path.expanduser('~/.ssh/id_rsa.pub'))) or os.path.exists((os.path.expanduser('~/.ssh/id_rsa.pub'))):
        os.system('mkdir ~/.ssh/backup')
        os.system('cp ~/.ssh/id_rsa* ~/.ssh/backup')
    output = subprocess.getoutput('ssh-keygen -t rsa -C "' + email + '"')
    return output
