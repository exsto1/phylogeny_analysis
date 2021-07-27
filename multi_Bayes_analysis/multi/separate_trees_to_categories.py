file_h = open("kategorie.txt")
file = file_h.readlines()
file_h.close()

categ = [[int(i1) for i1 in i.strip().split(";")[1].split(",")] for i in file[:-1]]


file2_h = open("merged_trees.con.tre")
file2 = file2_h.read()
file2_h.close()

intro = file2.split("   tree test_0")[0]
end = "end;"
trees = "   tree test_0" + file2.split("   tree test_0")[1].rstrip(end)
trees = trees.split("\n")
trees = [i for i in trees if i]

for i in range(len(categ)):
    newfile = open(f"merged_trees_cat_{i}.con.tre", "w")
    newfile.write(intro)
    for i1 in categ[i]:
        newfile.write(trees[i1] + "\n")
    newfile.write(end)
    newfile.close()

