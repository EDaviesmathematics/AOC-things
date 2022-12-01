#bunch of function that take common text files and process them into the helpful way
import heapq
import re
from datetime import datetime


import requests
from datetime import datetime



def collect(year ='20'+ datetime.today().strftime('%y'),day = datetime.today().strftime('%d') ):
    #Collects AOC input for me, Eric if you're reading this - Sorry!
    year = str(year)
    day = str(day)
    if day[0]=='0':
        day = day[1]
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    headers = {'Email': 'edaviesmathematics@gmail.com','git' :'https://github.com/EDaviesmathematics/AOC-things/edit/main/process.py'}
    #dump resulting text to file
    try:
        f = open('AOC_'+str(year)+'_'+str(day)+'_input.txt','x') #Fails if file already downloaded
        cookies = {'_gid': '',
                   'session': '',
                   '_ga': ''}
        data = requests.get(url, cookies=cookies, header = header)
        f.write(data.text)
        f.close()
    except:
        pass
    return 'AOC_'+str(year)+'_'+str(day)+'_input.txt'

def grid_get(file_name):
    f = open(file_name,'r')
    input_list = f.read().split('\n')
    f.close()
    n = len(input_list)
    grid = {}
    for y in range(n):
        for x in range(len(input_list[y])):
            try:
                grid[(y, x)] = int(input_list[y][x])
            except:
                grid[(y, x)] = input_list[y][x]


    return grid

def grid_print(grid):
    max_y =max([item[0] for item in grid])
    for y in range(max_y+1):
        string = ''
        if len([item[1] for item in grid if item[0]==y]) >0:
            max_x = max([item[1] for item in grid if item[0]==y])
            for x in range(max_x+1):
                try:
                    string += grid[(y,x)]
                except:
                    string += str(grid[(y,x)])
        print(string)
def list_line(file_name ):
    f = open(file_name,'r')
    input_list = f.read().split('\n')
    f.close()
    return input_list

def djikstra(start,end,get_neighbours,get_score,grid):
    #needs score functions, neighbours
    reached = {start:0}
    queue = [(0,start)]
    heapq.heapify(queue)
    while len(queue) > 0:
        score, state = heapq.heappop(queue)
        if state == end:
            print(score)
            return score, reached
        neighbours = get_neighbours(state,grid)
        for neighbour in neighbours:
            if neighbour not in reached:
                cost = get_score(state,neighbour,grid)
                reached[neighbour] = score + cost
                heapq.heappush(queue, (score+cost,neighbour))
    return False

def num_list(file_name):
    f = open(file_name,'r')
    input_list = f.read()
    f.close()
    numbers = [int(x) for x in re.findall(re.compile(r'-?\d+'),input_list)]
    return numbers

def word_and_numbers(file_name,wanted = r'([a-z]+|-?\d+)'):
    f = open(file_name,'r')
    things_to_keep = re.compile(wanted)
    pattern = re.compile(things_to_keep)
    numbers = re.compile(r'-?\d+')
    input_list =f.read().split('\n')
    f.close()
    data = []
    for line in input_list:
        x = pattern.findall(line)
        for i in range(len(x)):
            if numbers.match(x[i]):
                x[i] = int(x[i])
        data.append(x)
    return data

def lines(file_name):
    f = open(file_name,'r')
    input_list = f.read().split('\n')
    f.close()
    return input_list

def multiple_lines(header,file_name):
    data = []
    f = open(file_name,'r')
    input_list = f.read().split('\n')
    f.close()
    print(input_list)
    things = r'([a-z]+|-?\d+)'
    numbers = re.compile(r'-?\d+')
    header = re.compile(header)
    things = re.compile(things)
    current_block = []
    for i,line in enumerate(input_list):
        if header.search(line):
            if len(current_block)>0:
                data.append(current_block)
            current_block = []
        else:
            new_line = things.findall(line)
            for i in range(len(new_line)):
                if numbers.match(new_line[i]):
                    new_line[i] = int(new_line[i])
            if len(new_line) > 0:
                current_block.append(new_line)
    if len(current_block) > 0:
        data.append(current_block)
    return data

def split_lines(splitting_symbol, file_name):
    f = open(file_name,'r')
    input_list = f.read().split('\n')
    f.close()
    pattern = re.compile(r'[\S]+')
    data = [pattern.findall(line) for line in input_list]
    for i,line in enumerate(data):
        if line:
            print(line)
            x = line.index(splitting_symbol)
            data[i] = [data[i][:x],data[i][x+1:]]
    try:
        data.remove([])
    except:
        pass
    return data

def get_string(file_name):
    f = open(file_name)
    input_string = f.read()
    f.close()
    return input_string

def assembly_code(dic_rules,register,instructions):
    n = len(instructions)
    pointer = 0
    while 0 <= pointer < n:
        register, pointer = dic_rules[instructions[pointer][0]]((register, pointer,instructions[pointer]))
    return register

def dictionary(file_name,input_num = False,output_num = False,reflexive = False):
    with open(file_name) as f:
        text = f.read().split('\n')
    dictionary ={}
    for line in text:
        if line:
            items = re.findall(r'[a-zA-Z0-9]+',line)
            if input_num:
                x = int(items[0])
            else:
                x = items[0]
            if output_num:
                y = int(items[1])
            else:
                y = items[1]
            dictionary[x] = y
            if reflexive:
                dictionary[y] = x
    return dictionary
