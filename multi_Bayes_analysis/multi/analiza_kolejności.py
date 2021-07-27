import re

file_h = open("merged_trees.con.tre")
file = file_h.read()
file_h.close()

file = file.split("begin trees;")[1]

trees = file.split(";")[1:]
trees = [i.strip() for i in trees]
# -------------
# file = ["".join(list(re.split("&prob=.*?\"]", i))) for i in file]
# file = ["".join(list(re.split("[.*?]", i))) for i in file]
# file = [[i1.split(",")[0].split("[&family=") for i1 in i.split("(")[1:] if i1] for i in file]
# -------------

trees = [i.split("&family") for i in trees]
seq = [[i1.split(",")[-1].split("(")[-1].rstrip("[") for i1 in i[:-1]] for i in trees]
seq = [i for i in seq if i]

translate = file.split(";")[0].split("\n")
translate = [i.strip().rstrip(",").split("\t") for i in translate[2:] if i]
translate = [i for i in translate[:-1]]

seq_names = []
for i in seq:
    temp = []
    for i1 in i:
        for i2 in translate:
            if i2[0] == i1:
                temp.append(i2[1])
    seq_names.append(temp)

newfile = open("drzewa_nazwy.txt", "w")
for i in seq_names:
    newfile.write(",".join(i) + "\n")
newfile.close()

# print(len(seq_names))
result = {i[1]: {} for i in translate}
for i in range(len(seq_names)):
    for i1 in range(len(seq_names[i])):
        if seq_names[i][i1-1] not in result[seq_names[i][i1]]:
            result[seq_names[i][i1]][seq_names[i][i1-1]] = 1
        else:
            result[seq_names[i][i1]][seq_names[i][i1 - 1]] += 1

newfile2 = open("exceptions.txt", "w")
counter = 0
for i in result:
    if len(result[i]) > 1:
        print(i, result[i])
        newfile2.write(f"{i} ;")
        for i1 in result[i]:
            newfile2.write(f"{i1}-{result[i][i1]}, ")
        newfile2.write("\n")
    else:
        counter += 1
newfile2.close()

print(counter)




