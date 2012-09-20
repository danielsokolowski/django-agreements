"""
Arbitrary agreement/lease/terms-and-conditions signing app
"""
VERSION = (0, 5, 0)

__version__ = '.'.join((str(each) for each in VERSION[:4]))

def get_version():
    """
    Returns shorter version (digit parts only) as string.
    """
    return '.'.join((str(each) for each in VERSION[:4]))