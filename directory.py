#! /usr/bi/python


import commands
import logging
import os


logging.basicConfig(level=logging.DEBUG)


def make_pull_fetch(path):
    try:
        for item in _get_dirs_path(path):
            if os.path.isdir(item):
                os.chdir(item)
                if '.git' in os.listdir(item):
                    git_link = commands.getoutput('git config --get remote.'
                                                  'origin.url')
                    if not _get_diff(item):
                        os.system('git fetch')
                    pull_command = 'git pull ' + git_link
                    os.system(pull_command)
                else:
                    make_pull_fetch(item + '/')
    except TypeError:
        logging.error('Please insert a correct path')


def _get_list_of_dirs(path):
    """Gets list of the directories are the main directory
    Args:
        path: path to the main directory
    Return:
        list of the directories
    """
    try:
        if os.path.isdir(path):
            return os.listdir(path)
    except OSError:
        return []


def _get_dirs_path(path):
    """Gets paths to the directories are the main directory
    Args:
        path: path to the main directory
    Return:
        list of the paths
    """
    return [path + item for item in _get_list_of_dirs(path)
            if not item.startswith('.')]


def _get_local_branches(path):
    command = 'cd ' + path
    os.system(command)
    lst = []
    for item in (commands.getoutput('git branch')).split('\n  '):
        if item.startswith('* '):
            lst.append(item[2:])
        else:
            lst.append(item)
    return lst


def _get_remote_branches(path):
    command = 'cd ' + path
    os.system(command)
    return [item.split('/')[1] for item in commands.getoutput('git branch -r').split('\n  ')]


def _get_diff(path):
    if _get_local_branches(path) == _get_remote_branches(path):
        return True
    else:
        return False


if __name__ == '__main__':
    make_pull_fetch('/Users/vboiko/workspace/')
    # print _get_local_branches('/Users/vboiko/workspace/daemon_git_python/')
