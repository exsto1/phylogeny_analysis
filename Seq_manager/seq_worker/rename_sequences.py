import argparse
import re
import os

parser = argparse.ArgumentParser()

parser.add_argument("-F", help='File name')
parser.add_argument("-R", help='Recursive search')

args = parser.parse_args()

# ---------------------------------------------------------------------------------------------


def renaming_process(filename):
    prefix = os.path.splitext(filename)[0]
    description = os.path.basename(prefix)
    zapis = open('%s_renamed%s' % (prefix, os.path.splitext(filename)[1]), 'w')
    num_lines = sum(1 for line in open(filename))
    with open(filename) as file:
        for i in range(num_lines):
            line = file.readline()
            if '>' in line:
                newline = re.sub('>', '>%s_' % description, line)
                zapis.write(newline)
            else:
                zapis.write(line)
    zapis.close()


# ---------------------------------------------------------------------------------------------

if args.F:
    renaming_process(os.path.abspath(args.F))
elif args.R:
    list_of_files = os.listdir(os.path.abspath(args.R))
    for i in list_of_files:
        if 'renamed' not in os.path.basename(i):
            renaming_process(os.path.abspath('%s/%s' % (args.R, i)))
