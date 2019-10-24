"""Syntax and settings defined in ENSDF manual
"""

# According to Chapter III in ENSDF manual these
# are the standard one card record formats
RECORD_MEMBERS = {
    'IDENTIFICATION'           : {
        'NUCID' : [ 1,  5],
        'DSID'  : [10, 39],
        'DSREF' : [40, 65],
        'PUB'   : [66, 74],
        'DATE'  : [75, 80],
    }
    'HISTORY'                  : {
        'NUCID' : [1, 5],
    },
    'Q-VALUE'                  : {
        'NUCID' : [1, 5],
    },
    'CROSS-REFERENCE'          : {
        'NUCID' : [1, 5],
    },
    'COMMENT'                  : {
        'NUCID' : [1, 5],
    },
    'PARENT'                   : {
        'NUCID' : [1, 5],
    },
    'NORMALIZATION'            : {
        'NUCID' : [1, 5],
    },
    'PRODUCTION NORMALIZATION' : {
        'NUCID' : [1, 5],
    },
    'LEVEL'                    : {
        'NUCID' : [1, 5],
    },
    'BETA MINUS'               : {
        'NUCID' : [1, 5],
    },
    'EC / BETA PLUS'           : {
        'NUCID' : [1, 5],
    },
    'ALPHA'                    : {
        'NUCID' : [1, 5],
    },
    'DELAYED PARTICLE'         : {
        'NUCID' : [1, 5],
    },
    'GAMMA'                    : {
        'NUCID' : [1, 5],
    },
    'REFERENCE'                : {
        'MASS'  : [1, 3],
    },
    'END'                      : {},
}

