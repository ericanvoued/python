import tkinter as tk;

window = tk.Tk();
window.title("my window");
window.geometry("200x200");


labl=tk.Label(window,bg='yellow',text='empty');
labl.pack();

def print_value():
    if (var1.get()==1)&(var2.get()==0):
        labl.config(text="I love only Python");
    elif (var1.get()==0)&(var2.get()==1):
        labl.config(text="I love only C++")
    elif (var1.get()==0)&(var2.get()==0):
        labl.config(text="I do not love either")
    else :
        labl.config(text="I love both")

var1=tk.IntVar();
var2=tk.IntVar();
c1=tk.Checkbutton(window,text='Python',variable=var1,onvalue=1,offvalue=0,
                  command=print_value)
c1.pack();
c2=tk.Checkbutton(window,text='C++',variable=var2,onvalue=1,offvalue=0,
                  command=print_value)
c2.pack();

window.mainloop();

