import random
import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", help="path to .con.tre file from MrBayes (sumt command after finished run - more in MrBayes manual)")
parser.add_argument("-o", "--output", help="output file name")

args = parser.parse_args()


input_file = open(os.path.abspath(args.input)).readlines()
output_file = open(os.path.abspath(args.output), "w")

tree_index = 0  # Get line with tree
for i in range(len(input_file)):
    if "tree con_50_majrule" in input_file[i]:
        full_tree = list(input_file[i])
        tree_index = i
        break


for i in range(tree_index):  # Write beginning
    output_file.write(input_file[i])


###
ids = []
families = []
for i in range(len(input_file)):  # Get families ids and names
    if "translate" in input_file[i]:
        i1 = 1
        stan = True
        while stan:
            if ";" in input_file[i + i1]:
                stan = False
            else:
                temp = input_file[i + i1].strip()
                ids.append(temp.split("\t")[0])
                families.append(temp.split("\t")[1])
            i1 += 1
###


###
same_chars = 7  # Compare names
keymap = {}
for i in range(len(ids)):
    temp = families[i][:same_chars]
    if temp in keymap:
        keymap[temp].append(ids[i])
    else:
        keymap[temp] = [ids[i]]

code = {}
for i in keymap:
    code[i] = random.choice(range(len(ids)))
###


###
for i in range(len(full_tree)):  # Append family info to first leaf
    if full_tree[i] == "(":
        stan = True
        i1 = 1
        number = ""
        code_to_write = None
        while stan:
            if full_tree[i + i1] == "[":
                number = number.lstrip(",").lstrip("(")
                for i0 in keymap:
                    if number in keymap[i0]:
                        code_to_write = code[i0]
                full_tree.insert(i + i1 + 1, "&family=%s," % code_to_write)
                stan = False
            else:
                number += full_tree[i + i1]
            i1 += 1
        break

for i in range(len(full_tree) - 1):  # Append family info to other leaves
    if full_tree[i] == "]" and full_tree[i+1] == ",":
        stan = True
        i1 = 1
        number = ""
        code_to_write = ""
        while stan:
            if full_tree[i + i1] == "[":
                number = number.lstrip(",").lstrip("(")
                for i0 in keymap:
                    if number in keymap[i0]:
                        code_to_write = code[i0]
                full_tree.insert(i + i1 + 1, "&family=%s," % code_to_write)
                stan = False
            else:
                number += full_tree[i + i1]
            i1 += 1

output_file.write("".join(full_tree))
###


for i in range(tree_index + 1, len(input_file)):  # write end
    output_file.write(input_file[i])

output_file.close()
