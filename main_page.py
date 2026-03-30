import tkinter as tk
from all_functions import *
root = tk.Tk()
root.title("yuval first app")

easy_word_list=[]
hard_word_list=[]

save_word = tk.Button(root, text="Save word", command=lambda: save_data(
    easy_word_list,
    hard_word_list,
    var_level.get(),
    var_word.get(),
    var_interpetasion.get()
))

var_word = tk.StringVar()
var_interpetasion=tk.StringVar()
var_level = tk.StringVar()

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

save_word.grid(row=1, column=3)



root.mainloop()










