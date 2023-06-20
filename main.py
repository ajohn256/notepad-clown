from textwrap import fill
from tkinter import *
import tkinter
from tkinter.messagebox import showwarning,showinfo,askyesnocancel
import tkinter.messagebox
from tkinter import filedialog
from datetime import  datetime
from turtle import width
from tkcode import CodeEditor



path_to_file = ''
root = Tk()
root.title("Notepad!")

root.geometry("800x600")
saved_file_info = False

main_menu = Menu(root,relief="raised")
root.config(menu=main_menu)

frame = Frame(root)
frame2 = Frame(frame)
frame3 = Frame(frame)
frame.pack(fill='both',expand=True)
frame2.pack(side='right',fill=Y)
frame3.pack(side='bottom',fill=X)


#textarea
scroll_bar = Scrollbar(frame2,activebackground="#000")
scroll_bar_horizontal = Scrollbar(frame3,activebackground="#000",orient='horizontal')

text_area = Text(frame,font=("Consolas",14),bg="#fff",fg="green",highlightbackground='green',highlightcolor="yellow",yscrollcommand=scroll_bar.set,xscrollcommand=scroll_bar_horizontal.set)
text_area.pack(fill='both',expand=True,padx=6,pady=4)

scroll_bar.pack(side='right',fill=Y,expand=True)
scroll_bar_horizontal.pack(side='bottom',fill=X,expand=True)
scroll_bar.config(command=text_area.yview)
scroll_bar_horizontal.config(command=text_area.xview)

def insert_date_time():
    date_ = str(datetime.now())
    text_area.insert(END,date_)

def save_file():
    global saved_file_info
    path = filedialog.asksaveasfilename(filetypes=[("Text file",("*.txt", "*.js","*.py")),("All files",("*"))])
    if path:
        print(path)
        data = text_area.get(0.0,END)
        with open(path,"wb") as file:
            file.write(data.encode('utf-8'))
            saved_file_info = True
            file.close()
            print("Done saving")

            root.title(str(path_to_file) + " saved!")
    
    else:
        pass

def save():
    global saved_file_info,path_to_file

    if path_to_file == '':
        save_file()
        
    else:
        with open(path_to_file,"wb") as file:
            new_data = text_area.get(0.0,END)
            file.write(new_data.encode('utf-8'))
            saved_file_info = True
            file.close()
            root.title(str(path_to_file) + " saved!")
        
        print("done")

def close_notepad():
    global path_to_file,saved_file_info

    if saved_file_info:
        root.destroy()
    
    else:
        dialog = askyesnocancel("Save","Would you like to save your changes!")
        if dialog:
            save()
            root.destroy()
        else:
            print(dialog)
            root.destroy()
        

def create_new_file():
    global path_to_file
    new_file = filedialog.asksaveasfile(filetypes=[("Text file",("*.txt", "*.js","*.py")),("All files",("*"))])
    path_to_file = new_file.name
    print(new_file.name)
    text_area.delete(1.0,END)
    root.title(str(new_file.name))




def open_file():    
    global path_to_file
    file_path = filedialog.askopenfilename(filetypes=[("Text file",("*.txt", "*.js","*.py","*.log")),("All files",("*"))])
    if file_path:
        print(file_path)
        root.title(str(file_path))
        path_to_file = file_path
        file_contents = open(file_path,"r")
        data = file_contents.read()
        text_area.delete(1.0,END)
        text_area.insert(1.0,data)
    
    else:
        pass


file_menu = Menu(main_menu,tearoff=0)
edit_menu = Menu(main_menu,tearoff=0)
help_menu = Menu(main_menu,tearoff=0)
about_menu = Menu(main_menu,tearoff=0)
# preferences_menu = Menu(main_menu,tearoff=0)

new_icon = PhotoImage(file="./file.png")
save_icon = PhotoImage(file="./save.png")
saveas_icon = PhotoImage(file="./saveas.png")
exit_icon = PhotoImage(file="./cancel.png")

edit_icon = PhotoImage(file="./edit.png")
copy_icon = PhotoImage(file="./copy.png")
paste_icon = PhotoImage(file="./paste.png")
cut_icon = PhotoImage(file="./cut.png")



main_menu.add_cascade(label="files",menu=file_menu)
main_menu.add_cascade(label="Edit",menu=edit_menu)
main_menu.add_cascade(label="Help",menu=help_menu)
main_menu.add_cascade(label="About",menu=about_menu)
# main_menu.add_cascade(label="Preferences",menu=preferences_menu)

file_menu.add_command(label="New",command=lambda:create_new_file(),image=new_icon,compound="left")
file_menu.add_command(label="Open file",command=lambda:open_file(),image=new_icon,compound="left")
file_menu.add_separator()
file_menu.add_command(label="Save",command=lambda:save(),image=save_icon,compound="left")
file_menu.add_command(label="Save as",command=lambda:save_file(),image=saveas_icon,compound="left")
file_menu.add_separator()
file_menu.add_command(label="Close",command=lambda:close_notepad(),image=exit_icon,compound="left")


edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")
edit_menu.add_separator()
edit_menu.add_command(label="Copy",image=copy_icon,compound="left")
edit_menu.add_command(label="Paste",image=paste_icon,compound="left")
edit_menu.add_command(label="Cut",image=cut_icon,compound="left")
edit_menu.add_separator()
edit_menu.add_command(label="Date/time",command=lambda:insert_date_time())

about_menu.add_command(label="Visit our website")
help_menu.add_command(label="help")

# preferences_menu.add_command(label="background")
# preferences_menu.add_separator()
# preferences_menu.add_command(label="font color")
# preferences_menu.add_command(label="font size")
# preferences_menu.add_command(label="font family")






root.mainloop()
        
   




