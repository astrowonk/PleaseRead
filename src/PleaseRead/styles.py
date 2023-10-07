"""styles"""

import importlib.resources


def get_styles(style_file=None):
    if not style_file:
        data_path_resource = importlib.resources.files(
            __package__) / 'default.css'
    with open(data_path_resource, 'r') as f:
        return f.read()


def make_header(styles=None):
    return """
    <head>
  <title></title> </head>"""
