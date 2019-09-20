from src.template_path import locate_variables, split_path

def test_correct_one_var():
    variables = locate_variables('{synonimous.foo} bar fizz')
    assert variables == ['synonimous.foo']

def test_correct_multiple_vars():
    variables = locate_variables('{synonimous.foo} bar fizz {entities.fuzz}')
    assert variables == ['synonimous.foo', 'entities.fuzz']

def test_split_path_without_or():
    nspace, paths = split_path('synonimous.foo')

    assert nspace == 'synonimous'
    assert paths == 'foo'

