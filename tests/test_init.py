from src import create_rasa_dataset

def test_render_correct_data():
    dataset = create_rasa_dataset({
        "entities": {
            "foo": [ "bar", "foobar" ]
        },
        "synonimous": {
            "fizz": [ "fizzfuzz", "fuzz"]
        },
        "templates": [
            {
                "text": "{synonimous.fizz} and {entities.foo}",
                "intention": "fizzfoo"
            }
        ]
    })

    assert dataset == {
        'rasa_nlu_data': {
            'common_examples': [
                {'text': 'fizzfuzz and bar', 'intent': 'fizzfoo'},
                {'text': 'fizzfuzz and foobar', 'intent': 'fizzfoo'},
                {'text': 'fuzz and bar', 'intent': 'fizzfoo'},
                {'text': 'fuzz and foobar', 'intent': 'fizzfoo'}
            ]
        }
    }