import csv
import sys

heliand_unique_words  = []
heliand_total_words = []
muspilli_total_words = []
covered_unique_words  = []
covered_total_words = []
words_not_covered = []

heliand = 'heliand/hel-unique-tokens.txt'
heliand_total = 'heliand/clean.txt'
muspilli = 'forms-prefixed.txt'

with open(muspilli, 'r', newline='\n') as mfile:
    reader=csv.reader(mfile, delimiter='\t')
    for row in reader:
        muspilli_total_words.append(row[0].strip())

with open(heliand, 'r', newline='\n') as hfile:
    for row in hfile:
        heliand_unique_words.append(row.strip())

for token in heliand_unique_words:
    if token.lower() in muspilli_total_words:
        covered_unique_words.append(token)

with open(heliand_total, 'r', newline='\n') as tfile:
    for row in tfile:
        heliand_total_words.append(row.lower().strip())
        if row.lower().strip() in muspilli_total_words:
            covered_total_words.append(row.lower().strip())
        else:
            words_not_covered.append(row.lower().strip())

unique_coverage = str(round((len(covered_unique_words)/len(heliand_unique_words)*100),3))
total_coverage = str(round((len(covered_total_words)/len(heliand_total_words)*100),3))


print("The Hêliand contains a total of " + str(len(heliand_total_words)) + " forms, "+str(len(heliand_unique_words))+" of which are unique.")
print("Muspilli currently contains "+str(len(muspilli_total_words))+" synthetically-generated forms.")
print("Of the "+str(len(heliand_unique_words))+" unique tokens in the Hêliand, Muspilli contains " +\
      str(len(covered_unique_words)) + " forms, or "+str(unique_coverage)+"%\n") 
print("Of the "+str(len(heliand_total_words))+" total tokens in the Hêliand, Muspilli contains " +\
      str(len(covered_total_words)) + " forms, or "+str(total_coverage)+"%\n")

with open('coverage.txt', 'w') as to_write:
    to_write.write("The Hêliand contains a total of " + str(len(heliand_total_words)) + " forms, "+str(len(heliand_unique_words))+" of which are unique.\n\n")
    to_write.write("Muspilli currently contains "+str(len(muspilli_total_words))+" synthetically-generated forms.\n\n")
    to_write.write("Of the "+str(len(heliand_unique_words))+" unique tokens in the Hêliand, Muspilli contains " +\
      str(len(covered_unique_words)) + " forms, or "+str(unique_coverage)+"%\n\n") 
    to_write.write("Of the "+str(len(heliand_total_words))+" total tokens in the Hêliand, Muspilli contains " +\
      str(len(covered_total_words)) + " forms, or "+str(total_coverage)+"%\n\n")

with open('words_not_covered.txt','w+') as to_write:
    for word in words_not_covered:
        to_write.write(word+'\n')


#cat hel-tokenized.txt | gsed s/'ë'/'e'/g | gsed s/'ī'/'î'/g |gsed s/'ē'/'ê'/g | gsed s/'ō'/'ô'/g | gsed s/'ā'/'â'/g | gsed s/'ė'/'e'/g | gsed s/'ū'/'û'/g | gsed s/'uu'/'w'/g > hel-tokenized-clean.txt
