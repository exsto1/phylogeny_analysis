import os

file = open('all_sequences_CL0057_unaligned').readlines()
result = {}
for i in range(len(file)):
    if '>' in file[i]:
        text = file[i][1:8]
        if 'PF' in text:
            if text not in result:
                result[text] = []

# dir = '/home/exsto/PROJEKT/sekwencje/correct_files'
# new = os.listdir(dir)
# for i in new:
#     if i[:7] not in result:
#         result[i[:7]] = []


file = open('pdbmap').readlines()
for i in range(len(file)):
    temp_name = file[i].split(';')[3].lstrip()
    if temp_name in result:
        temp_pdb = file[i].split(';')[0].lstrip()
        temp_chain = file[i].split(';')[1].lstrip()
        result[temp_name].append('_'.join([temp_pdb, temp_chain]))


print(' '.join([' '.join(i) for i in result.values()]))
new_r = []
for i in list(result.values()):
    new_r.extend(i)

print(len(new_r), new_r)

