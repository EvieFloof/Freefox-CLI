import json
import os
from pathlib import Path

from platformdirs import user_data_dir

import ffox.utils.logs as logger

data_dir = Path(user_data_dir("ffox"))
data_dir.mkdir(parents=True, exist_ok=True)

if not os.path.exists(f"{data_dir}/config.json"):
    open(f"{data_dir}/config.json", "w").write("{}")

config = json.load(open(f"{data_dir}/config.json"))


def Save():
    with open(f"{data_dir}/config.json", "w") as f:
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
