w, h = 800, 600
cell_w, cell_h = 50, 50
carrot_count = 20
box_count = 50
step = 50
move_keys = (37, 38, 39, 40, 87, 65, 83, 68)  # коды клавиш, отвечающие за wasd и стрелочки
images = {}


def load_images(tkinter):
    images["forest"] = tkinter.PhotoImage(file="images/forest.png")
    images["pika"] = tkinter.PhotoImage(file="images/pika.png")
    images["carrot"] = tkinter.PhotoImage(file="images/carrot.png")
    images["box"] = tkinter.PhotoImage(file="images/box.png")