import pandas as pd
import numpy as np
import os
import PIL.Image as pilimg
from tqdm import tqdm
from config import *


class Dataset(object):

    def __init__(self,dir_path):
        self.train = self.load_train_image_file(os.path.join(dir_path,'train'))
        self.test = self.load_test_image_file(os.path.join(dir_path,'test'))
        # train_dir = os.path.join(data_dir, 'train')
        # test_dir = os.path.join(data_dir,'test')

    def load_train_image_file(self, train_dir):
        train = []
        for category_id, category in enumerate(CATEGORIES):
            for file in os.listdir(os.path.join(train_dir, category)):
                file_name = 'train/{}/{}'.format(category, file)
                file_location = os.path.join(data_dir, file_name)
                im = pilimg.open(file_location)
                pix = np.array(im)
                height, width = pix.shape[:2]

                train.append(['train/{}/{}'.format(category, file), category_id, category, height, width])
        train = pd.DataFrame(train, columns=['file','category_id', 'category', 'height', 'width'])

        return train

    def load_test_image_file(self, test_dir):
        test = []
        for file in os.listdir(test_dir):
            file_name = 'test/{}'.format(file)
            file_location = os.path.join(data_dir, file_name)
            im = pilimg.open(file_location)
            pix = np.array(im)
            height, width = pix.shape[:2]

            test.append(['test/{}'.format(file), file, height, width])
        test = pd.DataFrame(test, columns=['filepath', 'file', 'height', 'width'])

        return test
