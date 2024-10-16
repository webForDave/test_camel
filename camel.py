def main():
    user_input = input('camelCase: ') # removes every whitespace in between string
    print(camel_to_snake_case(user_input)) # camel_to_snake_case function call


def camel_to_snake_case(camelCaseString):
    # removes any space(s) in between with leading/trailing space(s) & "_"
    camelCaseString = camelCaseString.replace('_', '').strip(' ').replace(' ', '')

    for char in camelCaseString:
        if camelCaseString.__contains__(char.upper()):
            camelCaseString = camelCaseString.replace(char.upper(), f'_{char.lower()}')
            camelCaseString = camelCaseString.lstrip('_')
        else:
            camelCaseString
    return camelCaseString


if __name__ == '__main__':
    main()