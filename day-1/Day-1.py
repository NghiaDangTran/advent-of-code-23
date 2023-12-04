import re

file_path = './day-1/input.txt'  

total=0
with open(file_path, 'r') as file:
    for line in file:
        numbers = re.findall(r'\d', line)
        if len(numbers)==1:
            total+=int(numbers[0]+numbers[0])
        elif len(numbers)>1:
            total+=int(numbers[0]+ numbers[-1])


print(total)
