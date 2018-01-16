import random
file = '/Users/gaowei/Documents/词典/大辞典.txt'
dictionary = []
with open(file) as t:
    for line in t:
        dictionary.append(line.rstrip('\n'))

for i in range(0,10):
    print(random.choice(dictionary))