#!/usr/bin/env python3

import os
import subprocess
from setuptools import setup
from setuptools.command.install import install


def command_exists(command):
    try:
        subprocess.run([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except subprocess.CalledProcessError:
        return False


class CustomInstall(install):
    def run(self):
        # install python requirements
        with open('requirements.txt') as req_file:
            requirements = req_file.readlines()
            for req in requirements:
                req = req.strip()
                if req:
                    subprocess.run(['pip3', 'install', req])

        # install os requirements
        platform = os.uname().sysname
        if platform == 'Linux':
            if command_exists('apt-get'):
                try:
                    subprocess.run(['sudo', 'apt-get', 'install', 'ffmpeg'])
                except Exception as e:
                    print(f'Error: {e}')
            elif command_exists('dnf'):
                try:
                    subprocess.run(['sudo', 'dnf', 'install', 'ffmpeg'])
                except Exception as e:
                    print(f'Error: {e}')
            elif command_exists('yum'):
                try:
                    subprocess.run(['sudo', 'yum', 'install', 'ffmpeg'])
                except Exception as e:
                    print(f'Error: {e}')
            elif command_exists('pacman'):
                try:
                    subprocess.run(['sudo', 'pacman', '-S', 'ffmpeg'])
                except Exception as e:
                    print(f'Error: {e}')
            elif command_exists('zypper'):
                try:
                    subprocess.run(['sudo', 'zypper', 'install', 'ffmpeg'])
                except Exception as e:
                    print(f'Error: {e}')
            elif command_exists('emerge'):
                try:
                    subprocess.run(['sudo', 'emerge', 'ffmpeg'])
                except Exception as e:
                    print(f'Error: {e}')
            else:
                print(f'Error: Unknown Linux distribution \'{platform}\', '
                      f'see https://ffmpeg.org to install \'ffmpeg\' manually')
        elif platform == 'Darwin':
            try:
                subprocess.run(['brew', 'install', 'ffmpeg'])
            except FileNotFoundError:
                print('Error: \'brew\' required but not found, see https://brew.sh to install it first')
            except Exception as e:
                print(f'Error: {e}')
        else:
            print(f'No package manager found, see https://ffmpeg.org to install \'ffmpeg\' manually')

        install.run(self)


setup(
    name='PyTranscriber',
    version='1.0',
    cmdclass={'install': CustomInstall},
)
