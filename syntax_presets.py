"""Syntax and settings defined in ENSDF manual
"""

# According to Chapter III in ENSDF manual these
# are the standard one card record formats
RECORD_MEMBERS = {
    'IDENTIFICATION'           : {
        'NUCID'       : [ 1,  5],
        'Additional'  : [ 6,  6],
        'RID'         : [ 7,  8],
        'DSID'        : [10, 39],
        'DSREF'       : [40, 65],
        'PUB'         : [66, 74],
        'DATE'        : [75, 80],
    },
    'HISTORY'                  : {
        'NUCID'       : [ 1,  5],
        'Additional'  : [ 6,  6],
        'RID'         : [ 7,  8],
        'History'     : [10, 80],
    },
    'Q-VALUE'                  : {
        'NUCID'       : [ 1,  5],
        'Additional'  : [ 6,  6],
        'RID'         : [ 7,  8],
        'Q_'          : [10, 19],
        'DQ_'         : [20, 21],
        'SN'          : [22, 29],
        'DSN'         : [30, 31],
        'SP'          : [32, 39],
        'DSP'         : [40, 41],
        'QA'          : [42, 49],
        'DQA'         : [50, 55],
        'QREF'        : [56, 80],
    },
    'CROSS-REFERENCE'          : {
        'NUCID'       : [ 1,  5],
        'Additional'  : [ 6,  6],
        'RID'         : [ 7,  8],
        'DSSYM'       : [ 9,  9],
        'DSID'        : [10, 39],
    },
    'COMMENT'                  : {
        'NUCID'       : [ 1,  5],
        'Additional'  : [ 6,  6],
        'RID'         : [ 7,  8],
        'RTYPE'       : [ 8,  8],
        'PSYM'        : [ 9,  9],
        'CTEXT'       : [10, 80],
    },
    'PARENT'                   : {
        'NUCID'       : [ 1,  5],
        'Additional'  : [ 6,  6],
        'RID'         : [ 7,  8],
        'E'           : [10, 19],
        'DE'          : [20, 21],
        'J'           : [22, 39],
        'T'           : [40, 49],
        'DT'          : [50, 55],
        'QP'          : [65, 74],
        'DQP'         : [75, 76],
        'ION'         : [77, 80],
    },
    'NORMALIZATION'            : {
        'NUCID'       : [ 1,  5],
        'Additional'  : [ 6,  6],
        'RID'         : [ 7,  8],
        'NR'          : [10, 19],
        'DNR'         : [20, 21],
        'NT'          : [22, 29],
        'DNT'         : [30, 31],
        'BR'          : [32, 39],
        'DBR'         : [40, 41],
        'NB'          : [42, 49],
        'DNB'         : [50, 55],
        'NP'          : [56, 62],
        'DNP'         : [63, 64],
    },
    'PRODUCTION NORMALIZATION' : {
        'NUCID'       : [ 1,  5],
        'Additional'  : [ 6,  6],
        'RID'         : [ 7,  8],
        'NRxBR'       : [10, 19],
        'UNC1'        : [20, 21],
        'NTxBR'       : [22, 29],
        'UNC2'        : [30, 31],
        'NBxBR'       : [42, 49],
        'UNC3'        : [50, 55],
        'NP'          : [56, 62],
        'UNC4'        : [63, 64],
        'COM'         : [77, 77],
    },
    'LEVEL'                    : {
        'NUCID'       : [ 1,  5],
        'Additional'  : [ 6,  6],
        'RID'         : [ 7,  8],
        'E'           : [10, 19],
        'DE'          : [20, 21],
        'J'           : [22, 39],
        'T'           : [40, 49],
        'DT'          : [50, 55],
        'L'           : [56, 64],
        'S'           : [65, 74],
        'DS'          : [75, 76],
        'C'           : [77, 77],
        'MS'          : [78, 79],
    },
    'BETA MINUS'               : {
        'NUCID'       : [ 1,  5],
        'Additional'  : [ 6,  6],
        'RID'         : [ 7,  8],
        'E'           : [10, 19],
        'DE'          : [20, 21],
        'IB'          : [22, 29],
        'DIB'         : [30, 31],
        'LOGFT'       : [42, 49],
        'DFT'         : [50, 55],
        'C'           : [77, 77],
        'UN'          : [78, 79],
        'Q'           : [80, 80],
    },
    'EC / BETA PLUS'           : {
        'NUCID'       : [ 1,  5],
        'Additional'  : [ 6,  6],
        'RID'         : [ 7,  8],
        'E'           : [10, 19],
        'DE'          : [20, 21],
        'IB'          : [22, 29],
        'DIB'         : [30, 31],
        'IE'          : [32, 39],
        'DIE'         : [40, 41],
        'LOGFT'       : [42, 49],
        'DFT'         : [50, 55],
        'TI'          : [65, 74],
        'DTI'         : [75, 76],
        'C'           : [77, 77],
        'UN'          : [78, 79],
        'Q'           : [80, 80],
    },
    'ALPHA'                    : {
        'NUCID'       : [ 1,  5],
        'Additional'  : [ 6,  6],
        'RID'         : [ 7,  8],
        'E'           : [10, 19],
        'DE'          : [20, 21],
        'IA'          : [22, 29],
        'DIA'         : [30, 31],
        'HF'          : [32, 39],
        'DHF'         : [40, 41],
        'C'           : [77, 77],
        'Q'           : [80, 80],
    },
    'DELAYED PARTICLE'         : {
        'NUCID'       : [ 1,  5],
        'Additional'  : [ 6,  6],
        'RID'         : [ 7,  8],
        'E'           : [10, 19],
        'DE'          : [20, 21],
        'IP'          : [22, 29],
        'DIP'         : [30, 31],
        'EI'          : [32, 39],
        'T'           : [40, 49],
        'DT'          : [50, 55],
        'L'           : [56, 64],
        'C'           : [77, 77],
        'COIN'        : [78, 78],
        'Q'           : [80, 80],
    },
    'GAMMA'                    : {
        'NUCID'       : [ 1,  5],
        'Additional'  : [ 6,  6],
        'RID'         : [ 7,  8],
        'E'           : [10, 19],
        'DE'          : [20, 21],
        'RI'          : [22, 29],
        'DRI'         : [30, 31],
        'M'           : [32, 41],
        'MR'          : [42, 49],
        'DMR'         : [50, 55],
        'CC'          : [56, 62],
        'DCC'         : [63, 64],
        'TI'          : [65, 74],
        'DTI'         : [75, 76],
        'C'           : [77, 77],
        'COIN'        : [78, 78],
        'Q'           : [80, 80],
    },
    'REFERENCE'                : {
        'MASS_NUMBER' : [ 1,  3],
        'Additional'  : [ 6,  6],
        'RID'         : [ 7,  8],
    },
    'END'                      : {
        'BLANK'       : [ 1, 80]
    }
}

# According to Chapter V in ENSDF manual these below
# are the field formats. Here they are defined as 
# regular expressions since a field can have 
# multiple formats which differ in character 
# positioning (unlike records!).
NUM = r'\d*[\d,\.,E,+,-]*'  # defined as unsigned number e.g. 345, 345.34, 23.E+9, etc
# TODO: Check RTYPE field and similarity to RID
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
        r'\(?P<T>{}\){{0,1}}\s?\(?P<U>[Y,D,H,M,U,N,K,P,A,F,S,E,V]{{0,3}})\)?'.format(NUM),
        'STABLE'],
    'E'     : [
        r'\(?[A-Z]?\+?{}\+?[A-Z]?\)?'.format(NUM),
        r'{}\+{}'.format(r'[\d,\.,E,+,-]*', NUM)
        ],
}

# Adding other field formats by groups...
for key in ['BR','CC','HF','LOGFT','NB','NP','NR','NT','QP']:
    FIELDS[key] = [NUM,]

for key in ['DBR','DCC','DE','DHF','DIA','DIB','DIE','DIP','DNB','DNR','DNP','DNT','DQP','DQ_','DS','DSP','DTI']:
    # these are two-character fields
    FIELDS[key] = [r'([\h*,\d*]{2})', 'LT', 'GT', 'LE', 'GE', 'AP', 'CA', 'SY']

for key in ['MR','Q_','QA','SN','SP']:
    FIELDS[key] = [r'[\d,\.,E,+,-]*',]

for key in ['DFT','DMR','DT','DNB','DQA']:
    # uncertainties, either asymmetric or symmetric
    FIELDS[key] = [r'\+(\d+)\-(\d+)', r'([\h*,\d*]{2})', 'LT', 'GT', 'LE', 'GE', 'AP', 'CA', 'SY']

for key in ['IA','IB','IE','IP','RI','TI']:
    FIELDS[key] = [NUM, r'\(?{}\)?'.format(NUM)]