from PIL import Image
from PIL import ImageDraw
import numpy as np
from random import randrange

def get_random_color():
    color = list(np.random.choice(range(256), size=3))
    return tuple(color)
    return color


def get_bbox_random_rectangle(image_size):
    x1=randrange(image_size[0]-100)
    y1=randrange(image_size[1]-100)
    max_x2=image_size[0]-(x1+50)
    x2=x1+40+randrange(max_x2)
    max_y2=image_size[1] - (y1 + 50)
    y2 = y1 + 40+ randrange(max_y2)
    print(max_x2, max_y2)
    return((x1,y1),(x2,y2))


def get_bbox_random_square(image_size):
    x1=randrange(image_size[0]-100)
    x2 = x1 + 40 + randrange(image_size[0] - (x1 + 50))
    y1=20+randrange(image_size[1]-(x2-x1))
    y2 = y1 + (x2-x1)
    return((x1,y1),(x2,y2))



image_size=(500,500)

img = Image.new('RGB',image_size,get_random_color())

draw = ImageDraw.Draw(img)

draw.line(get_bbox_random_rectangle(image_size), fill=get_random_color())

draw.rectangle(get_bbox_random_rectangle(image_size), fill=get_random_color(), outline=get_random_color())

draw.ellipse(list(get_bbox_random_square(image_size)), fill = get_random_color(), outline =get_random_color())

draw.polygon(list(np.random.choice(range(image_size[0]), size=6)),
             fill = get_random_color(), outline =get_random_color())

#draw.ellipse([(20,50),(40,70)], fill = get_random_color(), outline =get_random_color())

img.show()