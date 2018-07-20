import tkinter as tk;

window = tk.Tk();
window.title("my window");
window.geometry("200x300");

def moveit() :
    canvas.move(rect,0,2);

    
canvas=tk.Canvas(window,bg='blue',height=150,width=200)
image_file=tk.PhotoImage(file='int.gif')
image=canvas.create_image(20,20,anchor='nw',image=image_file);
x0,y0,x1,y1=50,50,80,80;
line=canvas.create_line(x0,y0,x1,y1)
oval=canvas.create_oval(x0,y0,x1,y1,fill='red');
arc=canvas.create_arc(x0+30,y0+30,x1+30,y1+30,fill='green',start=30,extent=210);
rect = canvas.create_rectangle(100,30,120,50,fill='yellow')

canvas.pack();
b=tk.Button(window,text='move',command=moveit).pack();

window.mainloop();

