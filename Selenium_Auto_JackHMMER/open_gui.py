import os
from tkinter import *
from tkinter import filedialog
import file_precheck

WEBBROWSER = open('config/config.txt').readlines()[1].rstrip()
xsize = 800
ysize = 300


def add_file():
    directory = filedialog.askopenfilenames()
    for i in directory:
        box.insert(END, i)


def remove_file():
    try:
        selection = box.curselection()
        box.delete(selection)
    except:
        pass


def start_run():
    list_of_files = []
    stan = True
    i = 0
    while stan:
        if box.get(i):
            list_of_files.append(box.get(i))
            i += 1
        else:
            stan = False
    if len(list_of_files) > 0:
        root.destroy()
        for i in list_of_files:
            print(i)
            base = i
            if '/' in base:
                base = base.split('/')[-1]
            if '.' in base:
                base = base.split('.')[0]
            temp_list = file_precheck.check(i)
            # os.system(f'python3 file_process.py -W {WEBBROWSER} -F {temp_list[0]} -B {base} -I 3')
            for i1 in temp_list:
                os.system(f'python3 file_process.py -W {WEBBROWSER} -F {i1} -B {base} -I 3')
                break


root = Tk()
root.geometry(f'{xsize}x{ysize}')
root.title('JackHMMER automatic search')


top = Frame(root)
bottom = Frame(root)
top.pack(side=TOP, fill=BOTH, expand=True)
bottom.pack(side=BOTTOM)


box = Listbox(root)
box.pack(in_=top, fill=BOTH, expand=1)


add_button = Button(text="Add file", command=add_file).pack(in_=bottom, side=LEFT)


remove_button = Button(text="Remove file", command=remove_file).pack(in_=bottom, side=LEFT)


start = Button(text="Start search", command=start_run).pack(in_=bottom, side=RIGHT)
root.mainloop()
