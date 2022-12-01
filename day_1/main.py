
f = open('input.txt')
lines = [x.replace('\n','') for x in f]
f.close()

elves = []
i = 0
for line in lines:
    if len(elves) <= i:
        elves.append(0)
    if line == '':
        i += 1
    else:
        elves[i] += int(line)

e_sorted = sorted(elves)

print(e_sorted[-1] + e_sorted[-2]+ e_sorted[-3])