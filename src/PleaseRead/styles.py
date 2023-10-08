"""styles"""

import importlib.resources
import json


def get_default_rules() -> dict:
    data_path_resource = importlib.resources.files(__package__) / 'rules.json'
    with open(data_path_resource, 'r') as f:
        return json.load(f)


def get_styles(style_file: str = None) -> str:
    """Get string of css file.

    Parameters
    ----------
    style_file : str, optional
        A css file name or path, by default None and uses default.css in the module.

    Returns
    -------
    str
        The CSS as a string.
    """
    if not style_file:
        data_path_resource = importlib.resources.files(
            __package__) / 'default.css'
    with open(data_path_resource, 'r') as f:
        return f.read()


def make_header(styles=None):  #TODO delete? add other things here?
    return """
    <head>
  <title></title> </head>"""
