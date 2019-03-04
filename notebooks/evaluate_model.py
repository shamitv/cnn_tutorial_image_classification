import os
from os.path import dirname
from keras.models import load_model
from pathlib import Path
from PIL import Image
import numpy as np

def get_script_dir():
    if '_dh' in globals():
        current_folder = globals()['_dh'][0]
    else:
        script_path=__file__
        current_folder=dirname(script_path)
    return current_folder

def get_model_dir():
    script_dir = get_script_dir()
    model_dir = os.path.join(script_dir,'..','data','model')
    return os.path.normpath(model_dir)


def get_image_dir(image_type):
    script_dir = get_script_dir()
    image_dir = os.path.join(script_dir,'..','data','images',image_type)
    return os.path.normpath(image_dir)


def load_trained_model():
    model_file=os.path.join(get_model_dir(),'trained_model_v2.h5')
    return load_model(model_file)

model = load_trained_model()

model.summary()

image_dim=100

def get_text_X_for_class(img_class):
    image_dir = get_image_dir('validate')
    image_dir = os.path.join(image_dir, img_class)
    print('Scanning :: '+image_dir)
    pathlist = Path(image_dir).glob('*.png')
    img_arr_list = []
    for path in pathlist:
        #filepath_str=str(path)
        img = Image.open(path)
        img = img.resize((image_dim,image_dim), Image.LANCZOS)
        arr = np.array(img)
        img_arr_list.append(arr)
    return np.array(img_arr_list)


test_X=get_text_X_for_class('triangle')

print(test_X.shape)
print('Got text x')

