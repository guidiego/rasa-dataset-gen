from src.config import Config

mock = {
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
}

def test_should_config_start_correctly():
    c = Config(mock)

    assert c._entities == mock['entities']
    assert c._synonimous == mock['synonimous']
    assert c.templates == mock['templates']

    assert c.get_value('synonimous', 'fizz') == mock['synonimous']['fizz']