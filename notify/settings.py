import pathlib
import yaml
from dotmap import DotMap


BASE_DIR = pathlib.Path(__file__).parent.parent
STATIC_DIR = BASE_DIR/'static'
TEMPLATES_DIR = STATIC_DIR/'templates'
config_path = BASE_DIR/'config.yaml'


def get_config(path):
    with open(path) as file:
        config = yaml.safe_load(file)
    return config


config = DotMap(get_config(config_path))
