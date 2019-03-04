import os
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
    #print(max_x2, max_y2)
    return((x1,y1),(x2,y2))


def get_bbox_random_square(image_size):
    x1=randrange(image_size[0]-100)
    x2 = x1 + 40 + randrange(image_size[0] - (x1 + 50))
    y1=20+randrange(image_size[1]-(x2-x1))
    y2 = y1 + (x2-x1)
    return((x1,y1),(x2,y2))


def generate_blank_image(image_size):
    img = Image.new('RGB', image_size, get_random_color())
    draw = ImageDraw.Draw(img)
    return img, draw


def generate_rectangle(image_size):
    img, draw = generate_blank_image(image_size)
    draw.rectangle(get_bbox_random_rectangle(image_size),
                   fill=get_random_color(), outline=get_random_color())
    return img


def generate_circle(image_size):
    img, draw = generate_blank_image(image_size)
    draw.ellipse(list(get_bbox_random_square(image_size)),
                 fill = get_random_color(), outline =get_random_color())
    return img


def generate_line(image_size):
    img, draw = generate_blank_image(image_size)
    draw.line(get_bbox_random_rectangle(image_size), fill=get_random_color())
    return img


def generate_triangle(image_size):
    img, draw = generate_blank_image(image_size)
    draw.polygon(list(np.random.choice(range(image_size[0]), size=6)),
                 fill=get_random_color(), outline=get_random_color())
    return img


def get_dir_for_class(image_class):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    class_dir = os.path.join(script_dir,'data','images',image_class)
    return os.path.normpath(class_dir)



generators = {
    'line' : generate_line,
    'triangle' : generate_triangle,
    'rectangle' : generate_rectangle,
    'circle' : generate_circle
}


image_size = (500,500)
num_images = 10000

for image_class in generators:
    print('Generating for '+image_class)
    image_gen_function=generators[image_class]
    image_dir=get_dir_for_class(image_class)
    print('\tSaving at ' + image_dir)
    os.makedirs(image_dir, exist_ok=True)
    for image_num in range(1,num_images+1):
        img=image_gen_function(image_size)
        image_filename=str(image_class) + '_' + str(image_num) + '.png'
        image_path=os.path.join(image_dir,image_filename)
        img.save(image_path)

