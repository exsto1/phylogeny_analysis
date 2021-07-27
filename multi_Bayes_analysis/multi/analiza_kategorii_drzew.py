file_h = open("drzewa_nazwy.txt")
file = file_h.readlines()
file_h.close()
drzewa = [i.strip().split(",") for i in file]

file2_h = open("brush.txt")
file2 = file2_h.readlines()
file2_h.close()
brush = [i.strip().split(", ") for i in file2]

instruction = """
KATEGORIE:
[ OBSERWOWANE <- PRZED_NIM ]
1. PF01402_0 <- PF10802_7
2. PF01402_0 <- PF13443_0
3. PF09957_0 <- PF14384_7
4. PF09957_0 <- PF10802_7
5. PF10802_0 <- PF13443_0
6. PF10802_0 <- PF14384_7
7. PF01402_7 <- PF16762_2
8. PF01402_7 <- PF09386_1
9. PF07704_0 <- PF09386_1
10. PF07704_0 <- PF13467_7
11. PF07764_0 <- PF13467_7
12. PF07764_0 <- PF16762_2
"""

parse_instruction = [i for i in instruction.split("\n")[3:]]
parse_instruction = [i for i in parse_instruction if i]
parse_instruction = [[i.split(" ")[1], i.split(" ")[3]] for i in parse_instruction]
# print(parse_instruction)

result = []
for i in range(len(drzewa)):
    temp = []
    for i1 in range(len(parse_instruction)):
        for i2 in range(len(drzewa[i])):
            if drzewa[i][i2] == parse_instruction[i1][0]:
                if drzewa[i][i2-1] == parse_instruction[i1][1]:
                    temp.append(1)
                else:
                    temp.append(0)
    result.append(temp)

result2 = {}
for i in range(len(result)):
    result[i] = [str(i1) for i1 in result[i]]
    if "".join(result[i]) in result2:
        result2["".join(result[i])][0] += 1
        result2["".join(result[i])][1].append(int(brush[i][1]))
        result2["".join(result[i])][2].append(i)
    else:
        result2["".join(result[i])] = [1, [int(brush[i][1])], [i]]


for i in result2:
    print(i, result2[i][0], sum(result2[i][1]) / len(result2[i][1]), len(result2[i][2]))

# newfile = open("kategorie.txt", "w")
# for i in result2:
#     newfile.write(f"{i};{','.join([str(i1) for i1 in result2[i][2]])}\n")
# newfile.close()




