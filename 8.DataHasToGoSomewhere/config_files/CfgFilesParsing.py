import configparser
settingsFile = '8.DataHasToGoSomewhere/config_files/settings.cfg'
cfg = configparser.ConfigParser()
cfg.read(settingsFile)
print(cfg['french'])
print(cfg['french']['greeting'])
print(cfg['files']['bin'])