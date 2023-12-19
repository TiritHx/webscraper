from os.path import isfile

def isconfig(): # if there is no config, will return true
    config_path = './config.cv' # cv stands for config vault
    if not isfile(config_path):
        file = open('config.cv', 'x')
        file.close()
        return True
    return False
