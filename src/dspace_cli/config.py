import os
import yaml

dir_path = os.path.dirname(os.path.realpath(__file__))
conf_path = os.path.join(dir_path, '../../config.yml')
config = yaml.safe_load(open(conf_path))