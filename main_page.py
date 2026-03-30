import tkinter as tk
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from all_functions import *
root = tk.Tk()
root.title("yuval first app")

easy_word_list=[]
hard_word_list=[]

var_word = tk.StringVar()
var_interpetasion=tk.StringVar()
var_level = tk.StringVar()


def clear_after_submit():
    save_data( easy_word_list,
    hard_word_list,
    var_level.get(),
    var_word.get(),
    var_interpetasion.get())
    var_interpetasion.set("")
    var_level.set("")
    var_word.set("")
    
    
    

save_word = tk.Button(root, text="Save word", command=lambda: clear_after_submit())


entry_word= tk.Entry(root, textvariable=var_word, width=30)
entry_word.grid(row=1, column=0)

word_lable = tk.Label(root, text="word")
word_lable.grid(row=0, column=0)


entry_interpetaion=tk.Entry(root, textvariable=var_interpetasion, width=30)
entry_interpetaion.grid(row=1, column=1)
interpetasion_lable = tk.Label(root, text="interpetasion")
interpetasion_lable.grid(row=0, column=1)


entry_level=tk.Entry(root, textvariable=var_level, width=30)
entry_level.grid(row=1, column=2)
level_lable = tk.Label(root, text="level")
level_lable.grid(row=0, column=2)
save_word.grid(row=5, column=4)

show_list = tk.Button(root, text="show list", command=lambda: show_hard_list(hard_word_list))
show_list.grid(row=6, column=4)



root.mainloop()










