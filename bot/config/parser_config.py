from configparser import ConfigParser

# нужно будет указать путь к файлу а то он не читается через эту хуйню

def read_config(name):
    config = ConfigParser()
    config.read('config_settings.ini', encoding="utf-8")
    return config[name][name]

def write_config():
    pass


