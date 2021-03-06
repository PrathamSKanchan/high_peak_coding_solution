#!/usr/bin/env python3
# coded by - pratham s kanchan
MAX = 100000000
fhand = open('input.txt')
# taking input from file
lines1 = fhand.readlines()
lines = []
for line in lines1:
    line = line.strip('\n')
    if line != '':
        lines.append(line)
# print(lines)

no_of_employees = int(lines[0][-1])
goodies = []
for i in range(2, len(lines)):
    goodie, price = lines[i].split(':')
    goodies.append([goodie, int(price)])
goodies = sorted(goodies, key=lambda x: x[1])
# print(goodies)
min_dif = MAX
for i in range(0, len(goodies)-no_of_employees+1):
    dif = goodies[i+no_of_employees-1][1]-goodies[i][1]
    if dif < min_dif:
        min_index = i
        min_dif = dif
fhand.close()

file2 = open('output.txt', 'w')
file2.write("The goodies selected for distribution are:\n\n")
for i in range(min_index, min_index+no_of_employees):
    a = goodies[i]
    file2.write(a[0]+': '+str(a[1])+"\n")
file2.write('And the difference between the chosen goodie with highest price and the lowest price is '+str(min_dif))
file2.close()
