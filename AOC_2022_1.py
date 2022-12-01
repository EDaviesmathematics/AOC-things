from process import *
def part_1():
    file_name = collect()
    with open(file_name) as f:
        text = f.read().split('\n')
        elves = []
        elf =[]
        for line in text:
            if line:
                elf.append(int(line))
            else:
                elves.append(elf)
                elf = []
        if elf:
            elves.append(elf)
    print(f'Answer to part 1 is: {max([sum(elf) for elf in elves])}')
    return

def part_2():
    file_name = collect()
    with open(file_name) as f:
        text = f.read().split('\n')
        elves = []
        elf =[]
        for line in text:
            if line:
                elf.append(int(line))
            else:
                elves.append(elf)
                elf = []
        if elf:
            elves.append(elf)
    print(f'Answer to part 2 is: {sum(sorted([sum(elf) for elf in elves])[-3:])}')
    return

if __name__ == '__main__':
    part_1()
    part_2()