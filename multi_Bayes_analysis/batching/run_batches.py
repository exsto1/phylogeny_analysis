import os
from multiprocessing import Pool

CPU = 150


def run_func(i):
    os.system(f"./working_folder/test_{i}/script_{i}.batch")

def main():
    pool = Pool(CPU+1)
    pool.map(run_func, list(range(CPU)))


if __name__ == "__main__":
    main()