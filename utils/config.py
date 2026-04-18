import json
import os

import utils.logs as logger

if not os.path.exists("./config.json"):
    open("config.json", "w").write("{}")

config = json.load(open("config.json"))


def Save():
    with open("config.json", "w") as f:
        json.dump(config, f)


def Read(key: str):
    return config[key]


def Contains(key):
    return key in config


def Edit(elements):
    for element in elements:
        config[element] = elements[element]
    Save()


def Remove(*args):
    for key in args:
        if key in config:
            del config[key]
        else:
            logger.warn(f"Key {key} not in config file")
    Save()
