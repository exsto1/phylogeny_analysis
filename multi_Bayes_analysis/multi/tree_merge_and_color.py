import random


def main():
    def generate_random_family_codes(input_file):
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

        return code, keymap

    def merge_trees():
        code = ""
        keymap = ""
        intro = ""
        outro = "end;"
        all_trees = []
        for i in range(150):
            filename = f"bayes_test_2_result/test_{i}/final.nexus.con.tre"
            file_temp_h = open(filename)
            file_temp = file_temp_h.readlines()
            file_temp_h.close()
            if i == 0:
                intro = "".join(file_temp[:-2])
                code, keymap = generate_random_family_codes(file_temp)
            all_trees.append(color_merged_tree(list(file_temp[-2]), code, keymap))

        all_trees = [f"test_{i}".join(all_trees[i].split("con_50_majrule")) for i in range(len(all_trees))]

        newfile = open("merged_trees.con.tre", "w")
        newfile.write(intro)
        newfile.write("".join(all_trees))
        newfile.write(outro)

    def color_merged_tree(full_tree, code, keymap):
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
            if full_tree[i] == "]" and full_tree[i + 1] == ",":
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

        return "".join(full_tree)

    merge_trees()


if __name__ == "__main__":
    main()