import yaml


def yamltodic():
    return yaml.load(open("../config.yaml", "r"), Loader=yaml.FullLoader)
