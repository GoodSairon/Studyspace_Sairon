class AnythingError(Exception):
    """Anything error"""
    pass

a = int(input("Enter number (if you'll enter '0' - it'll be error): "))

if a == 0:
    raise AnythingError("Hello, it's error guy =)")
