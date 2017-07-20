
'''
this class allow us to do some method working with file
'''
import os
from PIL import Image

class FileProcessing(object):

# def __init__(self):

#create a dictionary in the path between directories and ids in the range (0, N) where N is the number of directories in the path
    @staticmethod
    def create_dict(path):
        id = 0
        dictionary = dict()
        for file_name in os.listdir(path):
            dictionary[file_name] = id
            id = id + 1
        return dictionary

#get list images andtheir folders (error images' dirs if existed)in a directory, which is organized as directory/species/images
    @staticmethod
    def get_images_dirs(directory):
        images_dirs = list()
        error_images_dirs = list()
        species_tmp_ids = list()
        id = 0
        for species_id in os.listdir(directory):
            # print species_id
            species_dir = os.path.join(directory, species_id)
            for image_name in os.listdir(species_dir):
                image_dir = os.path.join(species_dir, image_name)
                try: 
                    image = Image.open(image_dir)
                except IOError:
                    error_images_dirs.append(image_dir)
                    continue
                if image.format != 'JPEG':
                    error_images_dirs.append(image_dir)
                    continue
                images_dirs.append(image_dir)
                species_tmp_ids.append(id)
            id = id + 1
        return images_dirs, species_tmp_ids, error_images_dirs
    @staticmethod


#get list images (error images' dirs if existed) in a directory, which is organized as directory/images
    def get_unknown_images_dirs(directory):
        images_dirs = list()
        error_images_dirs = list()
        for image_name in os.listdir(directory):
            image_dir = os.path.join(directory, image_name)
            try: 
                image = Image.open(image_dir)
            except IOError:
                error_images_dirs.append(image_dir)
                continue
            if image.format != 'JPEG':
                error_images_dirs.append(image_dir)
                continue
            images_dirs.append(image_dir)
        return images_dirs, error_images_dirs
