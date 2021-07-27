def extract_extra_struct():
    file = open("macierz_struktury_dodatkowe/FeatureMatrix - Strukt.tsv").readlines()
    file = [i.rstrip().split("\t") for i in file[1:]]
    file = [[file[i][i1] for i1 in range(len(file[i])) if i1 in [1, 11, 12, 13, 17]] for i in range(len(file))]
    for i in range(len(file)):
        if " " in file[i][0]:
            file[i][0] = file[i][0].split(" ")[0]

    for i in range(len(file)):
        if len(file[i]) != 5:
            file[i] = [file[i][0], "?", "?", "?", "?"]
    result = {i[0]: i[1:] for i in file}
    return result

if __name__ == "__main__":
    extract_extra_struct()
