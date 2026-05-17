#settings for scr layer
#load and expose the config for scr layer
import os
from pdb import run
import yaml 
config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')

with open(config_path, 'r') as f:
    config =yaml.safe_load(f) 
#print(config)
if __name__ == "__main__": 
    print(config)
