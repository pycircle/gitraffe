from os import system
import pexpect
from subprocess import Popen, PIPE, STDOUT
from output import getoutput
from log import save_log
from wrappers.authorization_wrapper import AuthorizationWrapper

def get_url():
    command = "git config --get remote.origin.url"
    output = getoutput(command)
    save_log(command, output)
    return output

def pull(window):
    child = pexpect.spawn('git pull')
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
            url = get_url()
            if url.startswith('https://') and '@' in url:
                info = 'Timeout error!'
            else:
                info = getoutput('git pull')
    save_log('git pull', info)
    return info

def push(window, additional_args=None):
    child = pexpect.spawn('git push')
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
            if get_url().startswith('https://'):
                info = 'Timeout error!'
            else:
                info = getoutput('git push')
    save_log('git push', info)
    return info