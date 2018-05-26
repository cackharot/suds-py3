from __future__ import absolute_import, print_function, division, unicode_literals

def is_builtin(name):
    return name.startswith('__') and name.endswith('__')
