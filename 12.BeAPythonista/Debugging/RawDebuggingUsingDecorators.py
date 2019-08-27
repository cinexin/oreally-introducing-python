def dump(func):

    def wrapped(*args, ** kwargs):
        "Print input argument(s) and output value(s)"
        print('Function name: %s' % func.__name__)
        print("Input arguments: %s" % ','.join(map(str, args)))
        print("Input keyword arguments: %s" % kwargs.items())
        output = func(*args, **kwargs)
        print("Output:", output)
        return output

    return wrapped
