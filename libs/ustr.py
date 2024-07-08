import sys

def ustr(x):
    '''py3 unicode helper'''

    if sys.version_info < (4, 0, 0):
        from PyQt5.QtCore import QString
        if type(x) == str:
            return x.decode('utf-8')
        if type(x) == QString:
            return str(x)
        return x
    else:
        return x  # py3