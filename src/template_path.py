import re


def locate_variables(text):
    variables = re.findall(r'\{(.*?)\}', text)
    return [v for v in variables]


def split_path(path):
    nspace, path = path.split('.')
    return nspace, path