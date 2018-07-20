import tkinter as tk;

window = tk.Tk();
window.title("my window");
window.geometry("200x200");

var=tk.StringVar();
labl=tk.Label(window,bg='yellow',text='empty');
labl.pack();

def radio_select():
    labl.config(text='you have selected'+var.get())
r1=tk.Radiobutton(window,text='Option A',
            variable=var,value='A',
                  command=radio_select)
r1.pack()
r2=tk.Radiobutton(window,text='Option B',
            variable=var,value='B',
                  command=radio_select)
r2.pack()
r3=tk.Radiobutton(window,text='Option C',
            variable=var,value='C',
                  command=radio_select)
r3.pack()


window.mainloop();

