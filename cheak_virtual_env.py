import os

def get_virtual_environment_name():
    virtual_env_path = os.getenv("VIRTUAL_ENV")
    if virtual_env_path:
        return os.path.basename(virtual_env_path)
    return "No virtual environment"

virtual_env_name = get_virtual_environment_name()
print("Active virtual environment:", virtual_env_name)

import flask

flask_version = flask.__version__
print("Flask version:", flask_version)

