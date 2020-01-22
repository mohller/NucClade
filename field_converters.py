"""Defining the functions to convert the fields defined in 
syntax_presets.py into their appropriate python values.
"""
from numpy import inf

def convert_time(stable, val, units):
    """Function to convert the values read from field T
    as defined in the ENSDF manual (section V.14).
    Returns the time in seconds.
    """
    h = 4.13566766e-15  # eV * s
    time_factors = {
        'Y'   : 365*24*3600,
        'D'   : 24*3600,
        'H'   : 3600,
        'M'   : 60,
        'S'   : 1,
        'MS'  : 1e-3,
        'US'  : 1e-6,
        'NS'  : 1e-9,
        'PS'  : 1e-12,
        'FS'  : 1e-15,
        'AS'  : 1e-18,
        'EV'  : h,
        'KEV' : h / 1e3,
        'MEV' : h / 1e6,
    }
    # print '-'.join([str(k) for k in [stable, val, units]])
    if stable == 'STABLE':
        return inf
    elif val == units == '':
        # handling empty field values
        return None
    elif units == '' != val:
        # these cases are not foreseen by the manual, but exist
        print('WARNING: Missing units in field of type T!')
        return None
    else:
        time = time_factors[units]
        if 'EV' in units: # val is energy
            result = time / float(val)
        else:
            result = time * float(val)
        return result


def convert_energy(e1, e2):
    """Function to convert the values read from field E
    as defined in the ENSDF manual (section V.18).
    Returns the time in seconds.
    """
    import re

    if e1 is None:
        val1 = 0
    elif not re.search('[A-DF-Z]', e1):
        val1 = float(e1)
    else:
        val1 = complex(0, sum(ord(l) for l in e1.lstrip() if l not in '+-'))
        if '-' in e1:
            val1 *= -1

    if e2 is None:
        val2 = 0
    elif not re.search('[A-DF-Z]', e2):
        val2 = float(e2)
    else:
        val2 = complex(0, sum(ord(l) for l in e2.lstrip() if l not in '+-'))
        if '-' in e2:
            val2 *= -1

    return val1 + val2


field_converters = {
    'E' : convert_energy,
    'T' : convert_time
    
}