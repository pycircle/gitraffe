from os import system
from subprocess import Popen, PIPE, STDOUT
from output import getoutput
from log import save_log

def get_url():
    command = "git config --get remote.origin.url"
    output = getoutput(command)
    save_log(command, output)
    return output

def pull():
    command = 'git pull'
    output = getoutput(command)
    save_log(command, output)
    return output

def push_ssh():
    return getoutput('git push')

def push(window, additional_args=None):
    from wrappers.authorization_wrapper import AuthorizationWrapper
    import pexpect
    output = get_url()
    child = pexpect.spawn('git push')
    notUser = False
    try:
        child.expect("Username*", timeout=2)
        dialog = AuthorizationWrapper(window)
        dialog.exec_()
        child.sendline(dialog.username)
        child.expect("Password*", timeout=2)
        child.sendline(dialog.password)
        child.expect(pexpect.EOF)
        info = child.before
    except (pexpect.TIMEOUT, pexpect.EOF):
        notUser = True
        if notUser:
            try:
                child.expect("Password*", timeout=2)
                dialog = AuthorizationWrapper(window)
                dialog.ui.Username_lineEdit.setText("Not needed")
                dialog.ui.Username_lineEdit.setReadOnly(True)
                dialog.exec_()
                child.sendline(dialog.password)
                child.expect(pexpect.EOF)
                info = child.before
            except (pexpect.TIMEOUT, pexpect.EOF):
                info = push_ssh()
    save_log('git push', info)
    return info
