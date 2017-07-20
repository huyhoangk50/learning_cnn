import os
from PIL import Image
import sys
import scipy.io as sio
import numpy as np
import imp
# from file_processing import FileProcessing
FileProcessing = imp.load_source('FileProcessing', '/home/hoangnh/Document/TensorFlow/CNN/libs/file_processing.py').FileProcessing()
CNN = imp.load_source('CNN', '/home/hoangnh/Document/TensorFlow/CNN/libs/cnn_model.py').CNN

DATA_PATH = '/home/hoangnh/Document/TensorFlow/ImageClassificationExample/data/'
TRAIN_PATH = DATA_PATH + 'train/'
TEST_PATH = DATA_PATH + 'test/'

label_2_label_id_dict = FileProcessing.create_dict(DATA_PATH)
# testing_images_dirs, testing_images_label, error_testing_images_dir  = FileProcessing.get_images_dirs(TEST_PATH)
testing_images_dirs, error_testing_images_dir  = FileProcessing.get_unknown_images_dirs(TEST_PATH)
training_images_dirs, training_images_labels, error_training_images_dirs = FileProcessing.get_images_dirs(TRAIN_PATH)

print CNN.dense_to_one_hot(np.asarray([1, 2]), 5)
# print testing_images_dirs
# print error_training_images_dirs
# print label_2_label_id_dict
# print FileProcessing.create_dict(data_path)
