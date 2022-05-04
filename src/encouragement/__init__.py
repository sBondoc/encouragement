from pathlib import Path
from configparser import ConfigParser

DIR_DATA = Path.home() / Path('.encouragement')
CONFIG = ConfigParser()
CONFIG.read(DIR_DATA / Path('config.cfg'))
