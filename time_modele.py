#! /usr/bin/python


import time
from directory import make_pull_fetch


seconds = 0
minutes = 0
hours = 0

while seconds <= 60:
    print (hours, 'Hours', minutes, 'Minutes', seconds, 'Seconds')
    time.sleep(1)
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes, seconds = 0, 0
    if hours == 24:
        hours, seconds, minutes = 0, 0, 0
    if seconds % 10 == 0:
        make_pull_fetch('/Users/vboiko/workspace/')

