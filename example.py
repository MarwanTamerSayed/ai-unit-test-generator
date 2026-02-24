def outer(a):
    def inner(b):
        return b * 2
    return inner(a)