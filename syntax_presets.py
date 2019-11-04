"""Syntax and settings defined in ENSDF manual
"""

# According to Chapter III in ENSDF manual these
# are the standard one card record formats
RECORD_MEMBERS = {
    'IDENTIFICATION'           : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 6,  8],
        'DSID'  : [10, 39],
        'DSREF' : [40, 65],
        'PUB'   : [66, 74],
        'DATE'  : [75, 80],
    },
    'HISTORY'                  : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 6,  8],
    },
    'Q-VALUE'                  : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 6,  8],
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
        'RID'   : [ 6,  8],
    },
    'COMMENT'                  : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 6,  8],
    },
    'PARENT'                   : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 6,  8],
    },
    'NORMALIZATION'            : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 6,  8],
    },
    'PRODUCTION NORMALIZATION' : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 6,  8],
    },
    'LEVEL'                    : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 6,  8],
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
        'RID'   : [ 6,  8],
    },
    'EC / BETA PLUS'           : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 6,  8],
    },
    'ALPHA'                    : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 6,  8],
    },
    'DELAYED PARTICLE'         : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 6,  8],
    },
    'GAMMA'                    : {
        'NUCID' : [ 1,  5],
        'RID'   : [ 6,  8],
    },
    'REFERENCE'                : {
        'MASS_NUMBER'  : [ 1,  3],
        'RID'          : [ 6,  8],
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
        'HISTORY'                  : r'  H', 
        'Q-VALUE'                  : r'  Q', 
        'CROSS-REFERENCE'          : r'  X', 
        'PARENT'                   : r'  P', 
        'NORMALIZATION'            : r'  N', 
        'PRODUCTION NORMALIZATION' : r' PN',
        'LEVEL'                    : r'  L', 
        'BETA MINUS'               : r'  B', 
        'EC / BETA PLUS'           : r'  E', 
        'ALPHA'                    : r'  A', 
        'DELAYED PARTICLE'         : r'  D', 
        'GAMMA'                    : r'  G', 
        'REFERENCE'                : r'  R',   
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
            r'(?P<A>\d{1,3})(?P<Sym>\w{1,2})(\[\+\d{1,}\]){0,1} (?P<mode>[\w,+,-]*) DECAY( \()?(?P<T>[\d,\.,E,+,-]*){0,1}\s?(?P<U>[Y,D,H,M,U,N,K,P,A,F,S,E,V]{0,3})\)?',
            r'MUONIC ATOM'
        ],
        'REACTIONS'                : [
            '(HI,XNG)', 
            'COULOMB EXCITATION'
        ]
    },
    'T'     : [
        r'(?P<T>[\d,\.,E,+,-]*){0,1}\s?(?P<U>[Y,D,H,M,U,N,K,P,A,F,S,E,V]{0,3})\)?',
        'STABLE']
}

