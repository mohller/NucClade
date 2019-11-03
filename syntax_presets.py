"""Syntax and settings defined in ENSDF manual
"""

# According to Chapter III in ENSDF manual these
# are the standard one card record formats
RECORD_MEMBERS = {
    'IDENTIFICATION'           : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 8,  8],
        'DSID'  : [10, 39],
        'DSREF' : [40, 65],
        'PUB'   : [66, 74],
        'DATE'  : [75, 80],
    },
    'HISTORY'                  : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 8,  8],
    },
    'Q-VALUE'                  : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 8,  8],
        'Q_'    : [10, 19],
        'DQ_'   : [20, 21],
        'SN'    : [22, 29],
        'DSN'   : [30, 31],
        'SP'    : [32, 39],
        'DSP'   : [40, 41],
        'QA'    : [42, 49],
        'DQA'   : [50, 55],
        'QREF'  : [56, 80],
    },
    'CROSS-REFERENCE'          : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 8,  8],
    },
    'COMMENT'                  : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 8,  8],
    },
    'PARENT'                   : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 8,  8],
    },
    'NORMALIZATION'            : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 8,  8],
    },
    'PRODUCTION NORMALIZATION' : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 8,  8],
    },
    'LEVEL'                    : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 8,  8],
        'E'     : [10, 19],
        'DE'    : [20, 21],
        'J'     : [22, 39],
        'T'     : [40, 49],
        'DT'    : [50, 55],
        'L'     : [56, 64],
        'S'     : [65, 74],
        'DS'    : [75, 76],
        'C'     : [77, 77],
        'MS'    : [78, 79],
    },
    'BETA MINUS'               : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 8,  8],
    },
    'EC / BETA PLUS'           : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 8,  8],
    },
    'ALPHA'                    : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 8,  8],
    },
    'DELAYED PARTICLE'         : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 8,  8],
    },
    'GAMMA'                    : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 8,  8],
    },
    'REFERENCE'                : {
        'MASS_NUMBER'  : [ 1,  3],
        'RID'          : [ 8,  8],
    },
    'END'                      : {},
}

# According to Chapter V in ENSDF manual these
# are the field formats defined as regular expressions
# since a field can have multiple formats which differ
# in character positioning (unlike records!).
digit = '[0-9]'
FIELDS = {
    'RID'   : {
        'HISTORY'                  : 'H', 
        'Q-VALUE'                  : 'Q', 
        'CROSS-REFERENCE'          : 'X', 
        'PARENT'                   : 'P', 
        'NORMALIZATION'            : 'N', 
        'PRODUCTION NORMALIZATION' : 'PN',
        'LEVEL'                    : 'L', 
        'BETA MINUS'               : 'B', 
        'EC / BETA PLUS'           : 'E', 
        'ALPHA'                    : 'A', 
        'DELAYED PARTICLE'         : 'D', 
        'GAMMA'                    : 'G', 
        'REFERENCE'                : 'R',   
    },
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

