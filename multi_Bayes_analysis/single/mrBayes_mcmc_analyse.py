from matplotlib import pyplot as plt
import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", help="path to .mcmc file from MrBayes")
parser.add_argument("-o", "--output", help="output file name with extension (.png, .svg, .pdf)")
parser.add_argument("-s", "--start", help="start plot X-axis from this generation number", type=int, default=1000000)
parser.add_argument("-f", "--figsize", help='matplotlib figure size. Format: "15,8" See matplotlib manual for more info', default="15,8")
parser.add_argument("-d", "--description", help="subtitle for plot", default="")

args = parser.parse_args()

input_file = os.path.abspath(args.input)
output = os.path.abspath(args.output)
min_gen = args.start
figure_size = args.figsize.split(",")
description = args.description

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


plt.figure(figsize=(int(figure_size[0]), int(figure_size[1])))
# plt.title("Average standard deviation of split frequencies\n%s" % description)
plt.rc('font', size=20)
plt.xlabel("Numer generacji")
plt.ylabel("Odchylenie standardowe")

plt.plot(x_data[min_index:], y_data[min_index:])
plt.margins(x=0)
plt.tight_layout()
plt.savefig(output)
plt.show()
