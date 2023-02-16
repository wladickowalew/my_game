import tkinter
from random import randint


def move_player(event):
    pos = canvas.coords(player)
    if event.keysym in ("Up", "w"):
        canvas.move(player, 0, -step)
        if pos[1] + cell_h <= 0:
            canvas.move(player, 0, h + pos[1] + cell_h - pos[1])
    elif event.keysym in ("Down", "s"):
        canvas.move(player, 0, step)
        if pos[1] >= h:
            canvas.move(player, 0, -(h + pos[1] + cell_h - pos[1]))
    elif event.keysym in ("Left", "a"):
        if pos[0] > 0:
            canvas.move(player, -step, 0)
    elif event.keysym in ("Right", "d"):
        if pos[0] + cell_w < w:
            canvas.move(player, step, 0)


def key_pressed(event):
    # print(event)
    move_keys = (37, 38, 39, 40, 87, 65, 83, 68) # коды клавиш, отвечающие за wasd и стрелочки
    if event.keycode in move_keys:             
        move_player(event)           # вызываем функцию, отвечающую за движение объекта

def random_coords():
    N, M = h // cell_h, w // cell_w
    x, y = randint(0, M - 1), randint(0, N - 1)
    coords = (x * cell_w, y * cell_h)
    if coords in all_coords:
        return random_coords()
    else:
        all_coords.add(coords)
        return coords


def start_game():
    player_coords = random_coords()
    player = canvas.create_image(player_coords, image=pika_pic, anchor='nw')

    for i in range(20):
        coords = random_coords()
        carrot = canvas.create_image(coords, image=carrot_pic, anchor='nw')

    return player

master = tkinter.Tk()
w, h = 800, 600
cell_w, cell_h = 50, 50
step = 50
all_coords = set()
fone_pic = tkinter.PhotoImage(file="images/forest.png")
pika_pic = tkinter.PhotoImage(file="images/pika.png")
carrot_pic = tkinter.PhotoImage(file="images/carrot.png")
canvas = tkinter.Canvas(master, bg='white', height=h, width=w)
canvas.create_image((0, 0), image=fone_pic, anchor='nw')
player = start_game()
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
