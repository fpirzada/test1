from .base import *  # noqa

DEBUG = False

try:
    from .local import *  # noqa
except ImportError:
    pass

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
