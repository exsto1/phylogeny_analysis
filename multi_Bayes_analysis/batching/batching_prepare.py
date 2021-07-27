import os
from shutil import copyfile

CPU = 25
all_files = 150

# ----------------folders
for i in range(all_files):
    os.makedirs(f"./working_folder/test_{i}", exist_ok=True)
    os.chmod(f"./working_folder/test_{i}", int("775"))
    copyfile("./data/final.nexus", f"./working_folder/test_{i}/final.nexus")
    batch_script = open(f"./working_folder/test_{i}/script_{i}.batch", "w")
    batch_script.write(f"""#!/bin/bash

#SBATCH --job-name=bayes_{i}
#SBATCH --partition=ogr
#SBATCH --ntasks=1

./bayes/mb ./test_{i}/final.nexus > ./test_{i}/log_{i}.txt

    """)


res = []
temp = []
counter = 0
for i in range(all_files):
    if i % CPU == 0:
        res.append(" & ".join(temp))
        counter += 1
        temp = []
    temp.append(f"./bayes/mb ./test_{i}/final.nexus > ./test_{i}/log_{i}.txt")

res.append(" & ".join(temp))
res = res[1:]

batch_file = open("working_folder/bayes_commands.batch", "w")
intro = """#!/bin/bash -l
#SBATCH --ntasks=25
#SBATCH --mem=50G
#SBATCH --partition=ogr
#SBATCH --job-name="sikora_mrbayes_statistical_tests"

"""

batch_file.write(intro)
for i in res:
    batch_file.write(i + "\n")
batch_file.close()

