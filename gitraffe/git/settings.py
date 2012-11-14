from os import system
from output import getoutput
from log import save_log

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
    system('git config --global user.name "%s" && git config --global user.email "%s"' % (username, email))