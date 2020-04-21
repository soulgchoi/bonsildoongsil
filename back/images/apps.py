from django.apps import AppConfig
import pandas as pd
from joblib import load
import os


class ImagesConfig(AppConfig):
    name = 'images'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CLASSIFIER_FOLDER = os.path.join(BASE_DIR, 'found\models')
    CLASSIFIER_FILE = os.path.join(CLASSIFIER_FOLDER, "model.h5")
    classifier = load(CLASSIFIER_FILE)
