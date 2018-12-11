import time
from datetime import datetime
import os
from os import listdir
from os.path import isfile, join
import pickle


def visualise_images(title, image_name_list):
    # original_dir = os.path.dirname(os.path.realpath(__file__))
    images = ""
    for image in image_name_list:
        img_div = open('visualization/templates/image-div.html', 'r').read()
        path = get_image_path(image)
        img_div = img_div.replace("<PATH>", path)
        img_div = img_div.replace("<image-title>", str(image))
        images += img_div
    html_file = open('visualization/templates/webpage.html', 'r').read()
    html_file = html_file.replace("<mwd-image-content>", images)
    html_file = html_file.replace("<task-title>", title)
    time_str = str(time.strftime("%Y%m%d-%H%M%S")) + str(datetime.now().strftime(".%f"))[
                                                     1:]  # to ensure that the file is not overwritten
    op_file = 'wp-' + time_str + '.html'
    with open('visualization/webpages/' + op_file, 'w') as f:
        f.write(html_file)
    return op_file


def get_image_path(image):
    try:
        with open('visualization/pickles/file_to_path_dict.pkl', 'rb') as pkl_file:
            file_to_path_dict = pickle.load(pkl_file)
    except FileNotFoundError:
        file_to_dict_prepare = dict_devset("devset/img/")
    return file_to_path_dict[image]


def prepare_dict(path):
    sub_dirs = [x[0] for x in os.walk(path)]
    file_to_path_dict = {}
    for d in sub_dirs:
        for f in listdir(d):
            if isfile(join(d, f)) and len(f) > 3:
                try:
                    file_to_path_dict[int((f[:f.index('.')]))] = d + "/" + f
                except:
                    pass
    with open('visualization/pickles/file_to_path_dict.pkl', 'wb') as pkl_file:
        pickle.dump(file_to_path_dict, pkl_file)
    return file_to_path_dict


# print(get_image_path(10719836514))
# images_list = ["135114844","288051306","457718082","512080165","12044649575","10045759763","330074636"]
# visualise_images("Demo Task", images_list)
# os.chdir(os.getcwd() + "/webpages")
# op = prepare_dict("../../devset/img/")
# op = prepare_dict("../../devset/img/")
