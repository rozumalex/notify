import pathlib
import yaml


SECRET_KEY = b'8gmb092bYf0ybnvBTgtkrVDtqTiaXQxRGKcx060W2bg='
BASE_DIR = pathlib.Path(__file__).parent.parent
STATIC_DIR = BASE_DIR/'static'
TEMPLATES_DIR = STATIC_DIR/'templates'
config_path = BASE_DIR/'config'/'notify.yaml'

def get_config(path):
    with open(path) as file:
        config = yaml.safe_load(file)
    return config


config = get_config(config_path)