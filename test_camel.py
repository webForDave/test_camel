from camel import camel_to_snake_case

def test_camel_to_snake_case():
    assert camel_to_snake_case('helloWorld') == 'hello_world'
    assert camel_to_snake_case('DavidAkinola') == 'david_akinola'

def test_camel_to_snake_case_with_spaces():
    assert camel_to_snake_case('hello world') == 'helloworld'
    assert camel_to_snake_case('Hello World') == 'hello_world'

def test_camel_to_snake_case_without_spaces():
    assert camel_to_snake_case('helloworld') == 'helloworld'
    assert camel_to_snake_case('hello_world') == 'helloworld'
