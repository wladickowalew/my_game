import tkinter
from random import randint
from consts import *


def object_collision(obj1, obj2):
    return canvas.coords(obj1) == canvas.coords(obj2)


def carrot_collision():
    global points
    for carrot in carrots:
        if object_collision(player, carrot):
            carrots.remove(carrot)
            canvas.delete(carrot)
            points += 1
            return


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
    if event.keycode in move_keys:
        move_player(event)  # вызываем функцию, отвечающую за движение объекта
        carrot_collision()


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
    for i in range(carrot_count):
        coords = random_coords()
        carrot = canvas.create_image(coords, image=images["carrot"], anchor='nw')
        carrots.append(carrot)

    for i in range(box_count):
        coords = random_coords()
        box = canvas.create_image(coords, image=images["box"], anchor='nw')
        boxes.append(box)

    player_coords = random_coords()
    player = canvas.create_image(player_coords, image=images["pika"], anchor='nw')
    return player


master = tkinter.Tk()
all_coords = set()
carrots, boxes = [], []
points = 0
load_images(tkinter)
canvas = tkinter.Canvas(master, bg='white', height=h, width=w)
canvas.create_image((0, 0), image=images["forest"], anchor='nw')
player = start_game()
canvas.pack()
master.bind("<KeyPress>", key_pressed)
master.mainloop()
