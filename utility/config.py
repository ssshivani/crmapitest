import importlib
import os


def get_config():
    env_to_file_dict = {
        "prod": "production",
        "test": "crmtest",
        "testt": "crmtestt"
    }
    env = os.environ.get("ENV")
    path = ".".join(["environment", env_to_file_dict.get(env, "development")])
    config = importlib.import_module(path)
    return config.Config
