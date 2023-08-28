#!/usr/bin/env python3

import os
import subprocess
from setuptools import setup
from setuptools.command.install import install


def command_exists(command):
    from shutil import which
    return which(command) is not None


class CustomInstall(install):
    def run(self):
        # install python requirements
        try:
            subprocess.run('pip3 install -r requirements.txt'.split(' '))
        except Exception as e:
            print(f'Error: {e}')
            return

        # install os requirements
        platform = os.uname().sysname
        if platform == 'Linux':
            try:
                if command_exists('brew'):
                    subprocess.run('brew install ffmpeg'.split(' '))
                elif command_exists('apt-get'):
                    subprocess.run('sudo apt-get install ffmpeg'.split(' '))
                elif command_exists('dnf'):
                    subprocess.run('sudo dnf install ffmpeg'.split(' '))
                elif command_exists('yum'):
                    subprocess.run('sudo yum install ffmpeg'.split(' '))
                elif command_exists('pacman'):
                    subprocess.run('sudo pacman -S ffmpeg'.split(' '))
                elif command_exists('zypper'):
                    subprocess.run('sudo zypper install ffmpeg'.split(' '))
                elif command_exists('emerge'):
                    subprocess.run('sudo emerge ffmpeg'.split(' '))
                else:
                    print(f'No package manager found, see https://ffmpeg.org to install ffmpeg manually')
            except Exception as e:
                print(f'Error: {e}')
                return
        elif platform == 'Darwin':
            try:
                subprocess.run('brew install ffmpeg'.split(' '))
            except FileNotFoundError:
                print('Error: brew required but not found, see https://brew.sh to install it first')
                return
            except Exception as e:
                print(f'Error: {e}')
                return
        else:
            print(f'No package manager found, see https://ffmpeg.org to install ffmpeg manually')

        install.run(self)


setup(
    name='PyTranscriber',
    version='1.0',
    cmdclass={'install': CustomInstall},
)
