import time
from datetime import datetime


shift =25
day = datetime.today().strftime('%d')
def reset():
    incomplete = 'incomplete'
    with open('results.txt','w') as f:
        for i in range(1,26):
            f.write(f'Day {str(i).zfill(2)} Part 1: {incomplete.ljust(shift)} seconds Part 2: {incomplete.ljust(shift)} seconds\n')


def update(day = datetime.today().strftime('%d')):
    day = str(day)
    if day[0] == '0':
        day = day[1]
    with open('results.txt','r') as f:
        data = f.read().split('\n')
    with open('results.txt','w') as f:
        for i, line in enumerate(data):
            if str(i+1) == day:
                test = __import__(f'AOC_2022_{day}')
                t_0 = time.perf_counter()
                test.part_1()
                t_1 = time.perf_counter()
                test.part_2()
                t_2 = time.perf_counter()
                f.write(f'Day {str(i+1).zfill(2)} Part 1: {str(t_1-t_0).ljust(shift)} seconds Part 2: {str(t_2-t_1).ljust(shift)} seconds\n')
            else:
                f.write(line+'\n')
update()