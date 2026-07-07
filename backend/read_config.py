import configparser

def import_config(sections):
    #print(sections)
    config = configparser.ConfigParser()
    config.read('settings.ini')
    find_section = config[sections]
    response = {}
    for key in find_section:
        value = find_section[key]
        response.update({key: value})
    return response

def create_settings():
    config = configparser.ConfigParser()
    config['Paths'] = {'ScanPath': '',
        'LibraryPath': '/home/shaggy/Documents/RPGShelf'}
    config['Library settings'] = {'PreserveMissing': 'false'}

    with open('settings.ini', 'w') as configfile:
        config.write(configfile)