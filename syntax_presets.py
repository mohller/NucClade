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
    },
    'HISTORY'                  : {
        'NUCID' : [ 1,  5],
    },
    'Q-VALUE'                  : {
        'NUCID' : [ 1,  5],
        'Q'     : [ 8,  8],
        'Q-'    : [10, 19],
        'DQ-'   : [20, 21],
        'SN'    : [22, 29],
        'DSN'   : [30, 31],
        'SP'    : [32, 39],
        'DSP'   : [40, 41],
        'QA'    : [42, 49],
        'DQA'   : [50, 55],
        'QREF'  : [56, 80],
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
        'MASS_NUMBER'  : [1, 3],
    },
    'END'                      : {},
}

# According to Chapter V in ENSDF manual these
# are the field formats defined as regular expressions
# since a field can have multiple formats which differ
# in character positioning (unlike records!).
digit = '[0-9]'
FIELDS = {
    'NUCID' : {
        'MASS_NUMBER' : [1, 3],
        'Z'           : [4, 5]
    },
    'DSID'  : {
        'REFERENCES'               : r'REFERENCES',
        'COMMENTS'                 : r'COMMENTS',
        'ADOPTED LEVELS'           : [
            r'ADOPTED LEVELS',
            r'ADOPTED LEVELS, GAMMAS'
        ],
        'DECAYS'                   : [
            r'(\d{1,3})(\w{1,2})(\[\+\d{1,}\]){0,1} ([\w,+,-]*) DECAY( \(.*\)){0,1}',
            r'MUONIC ATOM'
        ],
        'REACTIONS'                : [
            '(HI,XNG)', 
            'COULOMB EXCITATION'
        ]

    }
}

