import cv2
import numpy as np
from PIL import Image
from tensorflow.keras import models
import os
# from django.contrib.staticfiles.templatetags.staticfiles import static


class predict:
    IMG_SIZE = 172
    MODEL_DIR = "network.h5"
    MEDIA_PATH = "C:\Important\Projects\media"
    predictions = []
    dataset = []
    model = None

    def __init__(self, IMG_SIZE=172, MEDIA_PATH='C:\Important\Projects\media', model=None):
        self.IMG_SIZE = IMG_SIZE
        self.MEDIA_PATH = MEDIA_PATH
        self.model = model
        self.load_dataset()

    def load_dataset(self):
        self.dataset = np.array(self.Dataset_loader(
            self.MEDIA_PATH, self.IMG_SIZE))
        print(len(self.dataset))

    def predict_value(self):
        val = self.model.predict(self.dataset)[:1]
        return [val[0][0], val[0][1]]

    def Dataset_loader(self, DIR, RESIZE):
        IMG = []
        def read(imname): return np.asarray(Image.open(imname).convert("RGB"))
        for IMAGE_NAME in os.listdir(DIR):
            PATH = os.path.join(DIR, IMAGE_NAME)
            _, ftype = os.path.splitext(PATH)
            if ftype == ".jpg" or ftype == ".png" or ftype == ".jpeg":
                img = read(PATH)
                img = cv2.resize(img, (RESIZE, RESIZE))
                IMG.append(np.array(img) / 255.)
        return IMG


def debug():
    p = predict()
    print(p.predict_value())
