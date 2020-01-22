"""Defining the functions to convert the fields defined in 
syntax_presets.py into their appropriate python values.
"""
from numpy import inf

def convert_time(stable, val, units):
    """Function to convert the values read into field T
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

    if stable == 'STABLE':
        return inf
    elif val == units == '':
        # handling empty field values
        return None
    else:
        time = time_factors[units]
        if 'EV' in units: # val is energy
            result = time / float(val)
        else:
            result = time * float(val)
        return result


field_converters = {
    'T' : convert_time
    
}