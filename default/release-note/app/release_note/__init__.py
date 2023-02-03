import os
import importlib
from release_note.utils.functions import to_camel_case


def get(name, min_version='', max_version=''):
    
    module = importlib.import_module(name=f"release_note.resources.{name}_release")
    release_class = getattr(module, f"{to_camel_case(name)}Release")()

    return release_class.get(min_version=min_version, max_version=max_version)

def list_resources():
    return [p.replace("_release.py", "") for p in os.listdir(f"{os.path.dirname(__file__)}/resources") if p.endswith("_release.py")]
