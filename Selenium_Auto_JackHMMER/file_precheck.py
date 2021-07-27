import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument('-F', help='Filename')
# parser.add_argument('-D', help='Delete files', action='store_true')

args = parser.parse_args()

def check(file_to_check):
    plik = open(file_to_check).readlines()
    new_file_name = file_to_check
    new_file_name = new_file_name.split('/')[-1].split('.')[0]
    licznik = 1
    nr = 1
    temp = []
    list_of_files = []
    for i in plik:
        if '>' in i:
            licznik += 1
        if licznik % 450 == 0:
            new_f = open(f'temp_files/{new_file_name}_part_{nr}_temp', 'w')
            list_of_files.append(os.path.abspath(f'temp_files/{new_file_name}_part_{nr}_temp'))
            for i1 in temp:
                new_f.write(i1)
            temp = []
            nr += 1
            licznik = 1
            print(f'File is too big! - Cutting {new_file_name}')
            break
        temp.append(i)
    new_f = open(f'temp_files/{new_file_name}_part_0_temp', 'w')
    list_of_files.append(os.path.abspath(f'temp_files/{new_file_name}_part_0_temp'))
    for i1 in temp:
        new_f.write(i1)
    return list_of_files
