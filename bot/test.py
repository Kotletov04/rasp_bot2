import configparser
import os

config = configparser.ConfigParser()



config = config.read('config.ini')


print(config)