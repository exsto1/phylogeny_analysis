from urllib import request
from tqdm import tqdm
import argparse
import os

'''
Przykladowy plik inputowy:

NIR_SIR_ferr
NIR_SIR
RHH_1
SAP
DUF1778
'''

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", default='input.txt')
parser.add_argument("-o", "--output", default="output")
parser.add_argument("-l", "--log", default="errors_not_downloaded.txt")
args = parser.parse_args()

PLIK_Z_RODZINAMI = args.input
FOLDER_DO_ZAPISU = os.path.abspath(args.output)
PLIK_Z_LOGAMI = args.log

try:
    os.mkdir(FOLDER_DO_ZAPISU)
except FileExistsError:
    pass


def pobieranie(PLIK_Z_RODZINAMI, PLIK_Z_LOGAMI, FOLDER_DO_ZAPISU):
    outgrupy_dane = open(PLIK_Z_RODZINAMI).readlines()
    outgrupy = []
    for i in outgrupy_dane:
        outgrupy.append(i.rstrip())

    exceptions = open(FOLDER_DO_ZAPISU + "/" + PLIK_Z_LOGAMI, 'w')
    errors = []
    for i in tqdm(outgrupy):
        try:
            link = f'http://pfam.xfam.org/family/{i}/alignment/full/format?format=fasta&alnType=full&order=t&case=u&gaps=none&download=0'
            tekst = request.urlopen(link).read().decode('utf-8')
            if tekst:
                output = open(FOLDER_DO_ZAPISU + f'/{i}_seq.fasta', 'w')
                output.write(tekst)
                output.close()
            else:
                link1 = f'http://pfam.xfam.org/family/{i}/alignment/seed/format?format=fasta&alnType=seed&order=t&case=u&gaps=none&download=0'
                tekst1 = request.urlopen(link1).read().decode('utf-8')
                if tekst1:
                    output1 = open(FOLDER_DO_ZAPISU + f'/{i}_seq_seed.fasta', 'w')
                    output1.write(tekst1)
                    output1.close()
                else:
                    exceptions.write(f'{i}\n')
                    errors.append(i)
        except:
            # print('ERROR!!! No file downloaded')
            exceptions.write(f'{i}\n')
            errors.append(i)
            continue
    exceptions.close()

    if errors:
        print('---Error list:---')
        for i in errors:
            print(i)


if __name__ == "__main__":
    pobieranie(PLIK_Z_RODZINAMI, PLIK_Z_LOGAMI, FOLDER_DO_ZAPISU)