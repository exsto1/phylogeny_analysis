from urllib import request
from tqdm import tqdm

'''
PF00000,12
PF00000,20
'''

outgrupy_dane = open('temp_files/outgroups.txt').readlines()
outgrupy = []
for i in outgrupy_dane:
    outgrupy.append(i.rstrip())


save_path = 'pfam_files'

exceptions = open(save_path + '/errors_not_downloaded.txt', 'w')
errors = []
for i in tqdm(outgrupy):
    try:
        link = f'http://pfam.xfam.org/family/INVALID/alignment/full/format?format=fasta&alnType=full&order=t&case=u&gaps=none&download=0'
        tekst = request.urlopen(link).read().decode('utf-8')
        if tekst:
            output = open(save_path + f'/{i}_seq.fasta', 'w')
            output.write(tekst)
            output.close()
        else:
            link1 = f'http://pfam.xfam.org/family/{i}/alignment/seed/format?format=fasta&alnType=seed&order=t&case=u&gaps=none&download=0'
            tekst1 = request.urlopen(link1).read().decode('utf-8')
            if tekst1:
                output1 = open(save_path + f'/{i}_seq_seed.fasta', 'w')
                output1.write(tekst1)
                output1.close()
            else:
                exceptions.write(f'{i}\n')
                errors.append(i)
    except:
        print('ERROR!!! No file downloaded')
        exceptions.write(f'{i}\n')
        errors.append(i)
        continue
exceptions.close()

if errors:
    print('---Error list:---')
    for i in errors:
        print(i)
