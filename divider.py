from tkinter import *
from tkinter import messagebox,filedialog,Entry

# ---------------------------- CONSTANTS ------------------------------- #
YELLOW = "#f7f5dd"
GREEN = "#9bdeac"
FONT_NAME = "Courier"
MAX_LENGTH = 0
FILE_PATH = None
OUTPUT_PATH = None

# ---------------------------- DIVIDE MECHANISM ------------------------------- # 
def write_to_file(filename,rows):
    with open(OUTPUT_PATH + '/' + filename,'w+') as file:
        for row in rows:
            file.write(row)

def divide():
    global MAX_LENGTH

    if FILE_PATH is None:
        messagebox.showerror(title='Error', message='Please add a file to divide!')
    elif MAX_LENGTH == 0:
        messagebox.showerror(title='Error', message='Please submit the length!')
    elif OUTPUT_PATH is None:
        messagebox.showerror(title='Error', message='Please add an output path!')

    row_counter = 0
    file_counter = 0
    with open(FILE_PATH,'r') as file:
        rows = []
        data = file.readlines()
                        
        for row in data:
            rows.append(row)
            row_counter+=1
            
            #Check that the limit has been reached
            if row_counter == MAX_LENGTH:
                write_to_file(f'divided_{file_counter}.txt',rows)
                file_counter+=1
                row_counter=0 
                rows.clear()
                #Check that the remained lines in the file is greater than requested length or not
                #if not put them to a file
                if MAX_LENGTH > len(data)-(file_counter*MAX_LENGTH):
                    MAX_LENGTH = len(data)-(file_counter*MAX_LENGTH)

def upload_text():
    global FILE_PATH
    f_types = [('Text files', '*.txt')]
    filename = filedialog.askopenfile(filetypes=f_types)
    file_path.insert(0, filename.name)
    FILE_PATH = filename.name

def set_file_length():
    global MAX_LENGTH
    value = length_val.get()
    try:
        MAX_LENGTH = int(value)
    except ValueError:
        messagebox.showerror(title='Error', message='Please ad an integer value!')

def set_output_path():
    global OUTPUT_PATH
    dir = filedialog.askdirectory()
    output_path.insert(0, dir)
    OUTPUT_PATH = dir


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Divider")
window.config(padx=100, pady=50, bg=YELLOW)
window.resizable(0,0)

title_label = Label(text="Divider", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

file_label = Label(text="File:",bg=YELLOW, font=(FONT_NAME, 18))
file_label.grid(column=0, row=1)

file_path = Entry(window,width=50)
file_path.grid(column=1, row=1)

txt_browse = Button(text="Browse", highlightthickness=0,command=upload_text)
txt_browse.grid(column=2, row=1)

length_label = Label(text="Length:",bg=YELLOW, font=(FONT_NAME, 18))
length_label.grid(column=0, row=2)

length_val = Entry(window,width=50)
length_val.grid(column=1, row=2)

length_save = Button(text="Submit", highlightthickness=0,command=set_file_length)
length_save.grid(column=2, row=2)

output_label = Label(text="Output:",bg=YELLOW, font=(FONT_NAME, 18))
output_label.grid(column=0, row=3)

output_path = Entry(window,width=50)
output_path.grid(column=1, row=3)

output_browse = Button(text="Browse", highlightthickness=0,command=set_output_path)
output_browse.grid(column=2, row=3)

divide_button = Button(text="Divide it!", highlightthickness=0, command=divide)
divide_button.grid(column=1, row=4)

window.mainloop()
