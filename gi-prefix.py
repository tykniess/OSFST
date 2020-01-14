import csv

Prefixes = ['â', 'af', 'an', 'ana', 'and', 'for', 'furi', 'gegin', 'thurh', 'um', \
            'umbi', 'und', 'with', 'bi', 'far', 'thana', 'te', 'of', 'nitha',\
            'in', 'ful', 'gi', 'ût', 'up', 'ênfar', 'tô', 'ovar']
Lines = []

prefixable_Lines = []

def check(line):
    for prefix in Prefixes:
        if prefix in line[:len(prefix)]:
            return False
    return True

with open('forms.txt','r') as to_read:
    for line in to_read:
        if 'pastpart' in line:
            Lines.append(line)
    for line in Lines:
        if check(line):
            prefixable_Lines.append(line)

with open('forms-prefixed.txt','w+') as to_write:
    with open('forms.txt','r') as to_read:
        for line in to_read:
            if line in prefixable_Lines:
                to_write.write('gi'+line+'ge'+line)
            else:
                to_write.write(line)
