import yaml
yamlFile = '8.DataHasToGoSomewhere/yaml_files/mcintyre.yaml'
with open(yamlFile, 'rt') as fin:
    text = fin.read()
    data = yaml.safe_load(text)
    print(data['details'])
    print(len(data['poems']))
    print(data['poems'][1]['title'])