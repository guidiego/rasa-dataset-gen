import re

from .config import Config
from .template_path import locate_variables, split_path
from .iterate_helpers import aggregate_values

# loaded_data = '''
# {
#     "entities": {
#         "area": [
#             "cívil"
#         ],
#         "subarea": [
#             "divórcio"
#         ]
#     },
#     "synonimous": {
#         "want": [
#             "gostaria",
#             "necessito",
#             "necessitaria",
#             "preciso",
#             "precisava",
#             "queria"
#         ],
#         "indication": [
#             "orientação",
#             "ajuda"
#         ],
#         "professional": [
#             "júridica",
#             "profissional",
#             "de um advogado",
#             "de uma advogada",
#             "de um escritório"
#         ],
#         "greetings": [
#             "olá",
#             "oie",
#             "oi",
#             "ola"
#         ],
#         "byebye": [
#             "tchau",
#             "adeus",
#             "xau"
#         ],
#         "presentation": [
#             "sou o",
#             "sou a",
#             "meu nome é",
#             "me chamo"
#         ]
#     },
#     "templates": [
#         {
#             "text": "{synonimous.want} de {synonimous.indication} {entities.area||subarea}",
#             "intention": ""
#         },
#         {
#             "text": "{synonimous.want} de {synonimous.indication} {synonimous.professional} {entities.area||subarea}",
#             "intention": ""
#         },
#         {
#             "text": "{synonimous.greetings}",
#             "intention": ""
#         },
#         {
#             "text": "{synonimous.byebye}",
#             "intention": ""
#         },
#         {
#             "test": "{synonimous.presentation} {entities.name}",
#             "intention": ""
#         }
#     ]
# }'''

def create_rasa_dataset(value):
    c = Config(value)
    common_examples = []

    for template in c.templates:
        replace_values_group = {}
        entities_to_map = []

        for variable in locate_variables(template['text']):
            nspace, path = split_path(variable)
            variable_to_snake_case = re.sub(r'\.', '_', variable)

            template['text'] = re.sub(
                variable,
                variable_to_snake_case,
                template['text']
            )

            values = c.get_value(nspace, path)
            replace_values_group[
                variable_to_snake_case
            ] = values

            if nspace == 'entities':
                if path in entities_to_map:
                    entities_to_map[path].concat(values)
                else:
                    entities_to_map[path] = values


        for agg_val in aggregate_values(replace_values_group):
            common_examples.append({
                'text': template['text'].format(**agg_val),
                'intent': template['intention']
            })

    return {
        'rasa_nlu_data': {
            'common_examples': common_examples
        }
    }