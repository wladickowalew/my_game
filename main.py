import tkinter
from random import randint


def move_oval(event):
    pos = canvas.coords(oval)
    if event.keysym in ("Up", "w"):
        canvas.move(oval, 0, -step)
        if pos[1] + 2 * r <= 0:
            canvas.move(oval, 0, h + pos[1] + 2 * r - pos[1])
    elif event.keysym in ("Down", "s"):
        canvas.move(oval, 0, step)
        if pos[1] >= h:
            canvas.move(oval, 0, -(h + pos[1] + 2 * r - pos[1]))
    elif event.keysym in ("Left", "a"):
        if pos[0] > 0:
            canvas.move(oval, -step, 0)
    elif event.keysym in ("Right", "d"):
        if pos[0] + 2 * r < w:
            canvas.move(oval, step, 0)


def key_pressed(event):
    # print(event)
    move_keys = (37, 38, 39, 40, 87, 65, 83, 68) # коды клавиш, отвечающие за wasd и стрелочки
    if event.keycode in move_keys:             
        move_oval(event)           # вызываем функцию, отвечающую за движение объекта
    

master = tkinter.Tk()
w, h = 800, 600
r = 25
step = 20

fone_pic = tkinter.PhotoImage(file="images/forest.png")
pika_pic = tkinter.PhotoImage(file="images/pika.png")
carrot_pic = tkinter.PhotoImage(file="images/carrot.png")

canvas = tkinter.Canvas(master, bg='white', height=h, width=w)
canvas.create_image((0, 0), image=fone_pic, anchor='nw')

oval = canvas.create_image((w // 2 - r, h // 2 - r), 
                           image=pika_pic, anchor='nw')

coords = (randint(0, w - 50), randint(0, h - 50))
carrot = canvas.create_image(coords, image=carrot_pic, anchor='nw')

canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
