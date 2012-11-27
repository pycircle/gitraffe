from os import chdir, system
import pexpect
from subprocess import Popen, PIPE, STDOUT
from output import getoutput
from log import save_log
from wrappers.authorization_wrapper import AuthorizationWrapper

def check_repository(path):
    chdir(path)
    command = 'git rev-parse --git-dir'
    output = getoutput(command)
    save_log(command, output)
    if 'fatal' in output:
        return False
    return True

def open_repository(path):
    chdir(path)

def clone_repository(window, source, destination):
    cloning_timeout = 5
    command = 'git clone %s %s' % (source, destination)
    child = pexpect.spawn(command)
    try:
        child.expect("Username*", timeout=cloning_timeout)
        dialog = AuthorizationWrapper(window)
        dialog.exec_()
        child.sendline(dialog.username)
        child.expect("Password*", timeout=cloning_timeout)
        child.sendline(dialog.password)
        child.expect(pexpect.EOF)
        info = child.before
    except (pexpect.TIMEOUT, pexpect.EOF):
        rm_command = 'rm -rf ' + destination
        system(rm_command)
        try:
            child.expect("Password*", timeout=cloning_timeout)
            dialog = AuthorizationWrapper(window)
            dialog.ui.Username_lineEdit.setText("Not needed")
            dialog.ui.Username_lineEdit.setReadOnly(True)
            dialog.exec_()
            child.sendline(dialog.password)
            child.expect(pexpect.EOF)
            info = child.before
        except (pexpect.TIMEOUT, pexpect.EOF):
            system(rm_command)
            if source.startswith('https://') and '@' in source:
                return (False, 'Timeout error!')
            else:
                info = getoutput(command)
    save_log(command, info)
    return (True, info)