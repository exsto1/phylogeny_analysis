from random import randint

used_h = open("data/used_seeds.txt")
used = used_h.readlines()
used = [int(i.rstrip()) for i in used]
used_h.close()

CPU = 150

for i in range(CPU):
    temp_file_h = open(f"working_folder/test_{i}/final.nexus")
    temp_file = temp_file_h.readlines()
    temp_file_h.close()

    state = False
    while not state:
        new_seed = randint(1, 100000)
        if new_seed not in used:
            used.append(new_seed)
            state = True

    for i1 in range(len(temp_file)):
        if "set autoclose=" in temp_file[i1]:
            temp_file[i1] = f"set autoclose=yes nowarn=yes seed={new_seed} swapseed={new_seed}; \n"

    new_file = open(f"working_folder/test_{i}/final.nexus", "w")
    new_file.write("".join(temp_file))
    new_file.close()


used = [str(i) for i in used]
update = open("data/used_seeds.txt", "w")
update.write("\n".join(used))


