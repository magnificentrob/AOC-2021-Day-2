import csv
directions = []
with open('input.txt') as csvfile:
    inputtxt = csv.reader(csvfile, delimiter =' ')
    for row in inputtxt:
        directions.append(row)
        
horizontalPosition = 0
depth = 0
aim = 0
for i in directions:
    if i[0] == 'forward':
        horizontalPosition+= int(i[1])
        depth+= aim * int(i[1])
    if i[0] == 'down':
        aim+= int(i[1])
    if i[0] == 'up':
        aim-= int(i[1])
print(horizontalPosition*depth)