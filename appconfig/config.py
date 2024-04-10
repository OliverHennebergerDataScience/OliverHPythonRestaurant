#from logging.config import fileConfig
import logging.config


import json
from ruamel.yaml import YAML

import os 
from pathlib import Path

os.chdir(Path(__file__).parent) 

APP_FOLDER = Path(__file__).parent.parent
# DATASET_PATH = 'dataset/dataxy'

#fileConfig('logging.ini')
#logger = logging.getLogger()
# Run once at startup:

from appconfig.logging_dict import LOGGING_CONFIG
logging.config.dictConfig(LOGGING_CONFIG)

# Include in each module:
logger = logging.getLogger(__name__)
logger.debug("Logging is configured.")


# Read config.json
# File Structure: In ein String mit single hoch komma setzen. BEACHTEN: Innere Strings mit doppel Hoch Komma !
with open('config.json', mode='r', encoding = 'UTF-8') as file:
    json_string = file.read()

config_dict = json.loads(json_string)
print(config_dict['appname'])
print(config_dict['author'])


# Read config.yaml
# Das YAML Format wird wie json nur ohne geschweifte Klammern geschrieben
with open('config.yaml', mode='r', encoding = 'UTF-8') as file:
    yaml_string = file.read()

yaml = YAML() # Wird erstellt weil die YAML instance erst erstellt werden muss.
config_dict = yaml.load(yaml_string)
print(config_dict['appname'])
print(config_dict['author'])

logger.info('Config is closed')
