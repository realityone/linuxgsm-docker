#!/usr/bin/env python
import os
import subprocess
import ConfigParser

GAME = 'DoNotStarveTogether'
HOME = os.path.expanduser('~')
SETTING_DIRECTORY = os.path.join(HOME, '.klei', GAME)

SETTING_FILE = os.path.join(SETTING_DIRECTORY, 'settings.ini')
TOKEN_FILE = os.path.join(SETTING_DIRECTORY, 'server_token.txt')
MANAGER_FILE = os.path.join(HOME, 'dstserver')
BIN_DIRECTORY = os.path.join(HOME, 'serverfiles', 'bin')
BIN_FILE = os.path.join(
    BIN_DIRECTORY, 'dontstarve_dedicated_server_nullrenderer'
)

SERVER_TOKEN = os.environ.get('SERVER_TOKEN')
SERVER_NAME = os.environ.get('SERVER_NAME', 'Do Not Starve Together')
SERVER_DESCRIPTION = os.environ.get(
    'SERVER_DESCRIPTION', 'Welcome to %s' % SERVER_NAME
)
SERVER_PASSWORD = os.environ.get(
    'SERVER_PASSWORD', os.urandom(4).encode('hex')
)


def prepare_game():
    subprocess.call([MANAGER_FILE, 'auto-install'])


def main():
    config = ConfigParser.ConfigParser()

    with open(SETTING_FILE, 'rb') as config_file:
        config.readfp(config_file)

    if SERVER_TOKEN:
        config.set('account', 'dedicated_lan_server', 'false')
        with open(TOKEN_FILE, 'wb') as token_file:
            token_file.write(SERVER_TOKEN)
    else:
        config.set('account', 'dedicated_lan_server', 'true')

    config.set('network', 'default_server_name', SERVER_NAME)
    config.set('network', 'default_server_description', SERVER_DESCRIPTION)
    config.set('network', 'server_password', SERVER_PASSWORD)

    with open(SETTING_FILE, 'wb') as config_file:
        config.write(config_file)

    print 'Your world\'s password is %s' % SERVER_PASSWORD
    subprocess.call([BIN_FILE], cwd=BIN_DIRECTORY)


if __name__ == '__main__':
    prepare_game()
    main()
