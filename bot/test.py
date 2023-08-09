import configparser
import os

config = configparser.ConfigParser()
config.sections()


config = config.read('config\\config.ini')

TOKEN = configparser.ConfigParser().read('TOKEN')
HELP_COMMANDS = configparser.ConfigParser().read('COMMANDS')

print(config)