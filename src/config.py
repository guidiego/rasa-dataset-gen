from copy import deepcopy


class Config():
    def __init__(self, raw_config):
        self._entities = raw_config['entities']
        self._synonimous = raw_config['synonimous']
        self._templates = raw_config['templates']

    @property
    def templates(self):
        return deepcopy(self._templates)

    def get_value(self, nspace, path):
        val = getattr(self, '_{}'.format(nspace))

        try:
            return val[path]
        except Exception:
            return None