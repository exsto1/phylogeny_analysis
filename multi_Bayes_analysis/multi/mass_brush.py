import os
import copy
import re
import numpy
from matplotlib import pyplot as plt

def analiza_drzewa(plik):
    file_h = open(plik)
    file = file_h.read()
    file_h.close()

    names = file.split("translate")[1].split(";")[0].split("\n")
    names = [i.strip().rstrip(",").split("\t") for i in names]
    names = [i[1] for i in names if len(i) == 2]

    file = file.split("tree con_50_majrule = [&U] ")[1].split("\nend;")[0]
    file = "".join(re.split("&prob=.*?,", file))
    file = "".join(re.split("prob_stddev=.*?,", file))
    file = "".join(re.split("prob_range={.*?}", file))
    file = "".join(re.split("prob.percent.=.*?,", file))
    file = "".join(re.split("length_95%HPD={.*?}", file))
    file = "".join(re.split("prob.-sd=.*?\".*?\"", file))
    file = "".join(re.split("&length_mean=.*?,", file))
    file = "".join(re.split("length_median=.*?,", file))
    file = "".join(re.split("\[,]", file))
    file = "".join(re.split("\[]", file))

    file = file.split(",")
    # file = [i.split(":")[1].split("[")[0] for i in file if ":" in i]
    # for i in file:
    #     print(i)

    # print(file)
    result = {}
    counter = 0
    old_counter = 0
    for i in file:
        # print(i)
        connections = i.split(":")
        for i1 in range(len(connections)):
            if "(" in connections[i1]:
                counter += len(connections[i1].split("("))-1
            if i1 != 0:
                result[f"{connections[i1].rstrip(');').rstrip(')')}___{old_counter}"] = counter
                # print(connections[i1].rstrip(');').rstrip(')'), old_counter)
                old_counter = copy.copy(counter)

            if ")" in connections[i1]:
                counter -= len(connections[i1].split(")"))-1

    result2 = {}

    for i in result:
        if result[i] not in result2:
            result2[result[i]] = [i]
        else:
            result2[result[i]].append(i)

    # for i in result2:
    #     print(i, len(result2[i]), result2[i])

    return result2


if __name__ == "__main__":
    # file_name = [f"drzewa/{i}" for i in os.listdir("drzewa")]
    folder = "./bayes_test_2_result"
    file_name = [f"./{folder}/test_{i}/final.nexus.con.tre"for i in range(150)]

    result = []
    for i in file_name:
        wynik = analiza_drzewa(i)
        result.append([i.split("/")[3], len(wynik[2])])

    # for i in result:
        # print(i)
    print("----------")
    print("MAX: ", max(result, key=lambda i: i[1]))
    print("MIN: ", min(result, key=lambda i: i[1]))
    print("ŚREDNIA: ", sum([i[1] for i in result]) / len(result))
    print("ODCHYLENIE: ", numpy.std([i[1] for i in result]))

    raw = [i[1] for i in result]
    data_pl = {}
    for i in raw:
        if i not in data_pl:
            data_pl[i] = 1
        else:
            data_pl[i] += 1


    plt.figure(figsize=(14,6))
    plt.rc('font', size=20)
    # plt.rc('axes.spines', right=False, top=False)
    # plt.hist([i[1] for i in result], bins=7)
    plt.bar(data_pl.keys(), data_pl.values())
    plt.margins(x=0.01)
    plt.xlabel("Liczba odgałęzień")
    plt.ylabel("Liczba drzew")
    plt.tight_layout()
    plt.savefig("brush.png")
    plt.show()


    newfile = open("brush.txt", "w")
    result = [[str(i1) for i1 in i] for i in result]
    for i in range(len(result)):
        newfile.write(", ".join(result[i]) + "\n")
    newfile.close()

