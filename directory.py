#! /usr/bi/python


import os
import os.path
import logging


def make_pull_fetch(path):
    for item in _get_dirs_path(path):
        if '.git' in os.listdir(item):
            os.system('git fetch')
            os.system('git pull')
            # return str(os.system('git remote -v'))

def _check_if_dir(path):
    if os.path.isdir(path):
        return True
    else:
        # logging
        return 'Insert correct path'


def _get_list_of_dirs(path):
    try:
        if _check_if_dir(path):
            return os.listdir(path)
    except OSError:
        return []


def _get_dirs_path(path):
    return (path + item for item in _get_list_of_dirs(path)
            if not item.startswith('.'))



if __name__ == '__main__':
    make_pull_fetch('/Users/vboiko/workspace/')