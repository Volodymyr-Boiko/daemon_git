#! /usr/bi/python


import os
import os.path
import logging


def check_if_dir(path):
    if os.path.isdir(path):
        return True
    else:
        # logging
        return 'Insert correct path'


def get_list_of_dirs(path):
    try:
        if check_if_dir(path):
            return os.listdir(path)
    except OSError:
        return []


def get_dirs_path(path):
    return (path + item for item in get_list_of_dirs(path)
            if not item.startswith('.'))


def ffff(path):
    for item in get_dirs_path(path):
        if '.git' in os.listdir(item):
            os.system('git pull')


if __name__ == '__main__':
    ffff('/Users/vboiko/workspace/')