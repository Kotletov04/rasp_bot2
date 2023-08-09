from configparser import ConfigParser



file = 'test.ini'
config = ConfigParser()



print(list(config.read('test.ini')))