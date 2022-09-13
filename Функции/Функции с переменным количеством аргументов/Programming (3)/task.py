def greet(name, *args):
    if not args:
        return f'Hello, {name}!'
    else:
        result = ' '.join(['and ' + arg for arg in args])
        return f'Hello, {name} {result}!'
