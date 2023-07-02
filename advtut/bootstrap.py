import yaml
from kink import di
from orator import DatabaseManager


def bootstrap():

    with open("etc/config.yaml", 'r') as F:
        config = yaml.safe_load(F)
        # print("config: ", config)
        di["config"] = config

        db = DatabaseManager(di["config"]["databases"])
        di["db"] = db
