import tkinter as tk;

window = tk.Tk();
window.title("my window");
window.geometry("200x200");


labl=tk.Label(window,bg='yellow',text='empty');
labl.pack();

def print_value(x):
    labl.config(text='you have selected'+x)

s=tk.Scale(window,label='try me',from_=5,to_=15,orient=tk.HORIZONTAL,length=200,
           showvalue=1,tickinterval=3,resolution=0.01,command=print_value)
s.pack();

window.mainloop();

