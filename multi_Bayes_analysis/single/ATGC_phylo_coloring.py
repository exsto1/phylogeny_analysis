import os
import argparse
import random

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", help="path to tree file")
parser.add_argument("-o", "--output", help="output file name")

args = parser.parse_args()

input_file = open(os.path.abspath(args.input)).read().strip()
output_file = open(os.path.abspath(args.output), "w")
parts = input_file.split(":")

used = []
number = list(range(len(parts)))
random.shuffle(number)
print(number)

for i0 in range(len(parts)):
    if "PF" in parts[i0]:
        for i in range(len(parts[i0])):
            if parts[i0][i] == "P" and parts[i0][i+1] == "F":
                if parts[i0][i:i+7] not in used:
                    used.append(parts[i0][i:i+7])
                parts[i0] = parts[i0] + f"[&family={number[used.index(parts[i0][i:i+7])]}]"

print(used)


output_file.write("#NEXUS\n" + "begin" + " trees;\n\ttree tree_1 = [&U] ")

output_file.write(":".join(parts))

output_file.write("\nend;")