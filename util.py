# utility definition file

from configparser import ConfigParser

def get_token()->str:
    cfg = ConfigParser()
    cfg.read('config.ini')
    return cfg['DEFAULT']['token']
