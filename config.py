from os.path import isfile

def isconfig(): # if there is no config, will return true
    config_path = './config.leaf'
    if not isfile(config_path):
        file = open('config.leaf', 'x')
        file.close()
        return True
    return False
