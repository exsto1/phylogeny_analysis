from matplotlib import pyplot as plt
import argparse
import os


def main():
    def get_data(input_file, min_gen):
        data = open(input_file).readlines()
        data = [i for i in data if "[" not in i]
        data = data[1:]
        data = [i.split("\t") for i in data]

        x_data = []
        y_data = []
        for i in data:
            x_data.append(float(i[0]))
            y_data.append(float(i[-1]))

        min_index = None
        for i in range(len(x_data)):
            if x_data[i] > min_gen:
                min_index = i
                break

        return x_data, y_data, min_index

    output = "full_plot_1.png"
    min_gen_val = 2500000
    figure_size = [15, 6]
    description = ""

    xdatas = []
    ydatas = []
    min_indexs = []
    for i in range(100):
        x_temp, y_temp, min_index_temp = get_data(f"bayes_test_2_result/test_{i}/final.nexus.mcmc", min_gen_val)
        xdatas.append(x_temp)
        ydatas.append(y_temp)
        min_indexs.append(min_index_temp)

    plt.figure(figsize=(int(figure_size[0]), int(figure_size[1])))
    # plt.title("Average standard deviation of split frequencies\n%s" % description)
    # plt.xlabel("Generation")
    # plt.ylabel("Standard deviation")
    plt.rc('font', size=20)
    # plt.title("Średnie odchylenie standardowe\n%s" % description)
    plt.xlabel("Numer generacji")
    plt.ylabel("Odchylenie standardowe")
    plt.margins(x=0)
    for i in range(len(xdatas)):
    #     if i in [8, 9, 10, 11, 12]:
            plt.plot(xdatas[i][min_indexs[i]:], ydatas[i][min_indexs[i]:], alpha=0.9, zorder=1)
    plt.hlines(0.05, min_gen_val, 10000000, colors='k', linestyles='dashed', linewidth=4, zorder=2)
    plt.tight_layout()
    plt.savefig(output)
    plt.show()


if __name__ == "__main__":
    main()
