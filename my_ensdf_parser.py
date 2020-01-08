# Code to parse ENSDF format following the manual instructions
# https://www.nndc.bnl.gov/nndcscr/documents/ensdf/ensdf-manual.pdf
# Here the structure of the file should be replicated by a class that 
# contains analogous substructure to that of the file


# Files general info:
#  - An ENSDF is a collection of 'datasets' (blocks separated by a blank line)
#  - A 'dataset' can be 1 of 5 different types
#  - A 'dataset' is made of lines (record) with 80 characters fixed length
#  - A file contains 'datasets' referring to nuclei of a specific mass A
#    - Within the file the 'datasets' can refer to the whole mass group (type 1 or 2) or... 
#    - ... to a specific nuclide, where 'datasets' are either: comments, adopted data, or (type 4 or 5)

END_RECORD = 80 * u' ' + u'\n'
DECAY_MODES = ['A', 'B+', '2B+', 'B+A', 'B+P', 'B+2P', 'B+3P',
               'B-', '2B-', 'B-A', 'B-N', 'B-2N', 'B-P', 
               'EC', '2EC', 'ECP', 'EC2P', 'ECA', 'EC3P', 'IT', 
               'N', '2N', 'P', '2P', 'SF', '14C']

import re
import numpy as np
from warnings import warn
from syntax_presets import RECORD_MEMBERS, FIELDS
from nuclei_data import nuclide_data

def get_atomic_number(symbol):
    """Returns the atomic number of an atomic element
    with symbol given by the parameter symbol of type string.
    """
    Z = 0
    for k, s in enumerate(nuclide_data['symbols']):
        if s.lower() == symbol.lower():
            Z = k
            break
    return Z

def dismember(string, markers, names=None):
    """Decompose string into size-limited fragments
    and returns them separately

    string: string to separate into substrings
    """

    if markers is None:
        return string
    else:
        pass
        
def is_dataset(string):
    """Checks whether string complies with dataset structure expected
    according to ENSDF manual
    """
    return True

def classify_record(record_string):
    """Identifies the record type from one of the 15 different
    types defined in ENSDF manual
    TODO: change into form of classify_dataset based
    on syntax_presets
    """
    record_type = None
    for key, val in FIELDS['RID'].iteritems():
        if record_string[5:8] == val:
            record_type = key

    if record_type is None:
        if record_string[6] in ['c', 'd', 't', 'C', 'D', 'T']:
            record_type = 'COMMENT'
        elif record_string == END_RECORD:
            record_type = 'END'
        elif record_string[6:9] == 3 * r' ':
            record_type = 'IDENTIFICATION'
        else:
            # warn('Record not within expected types!\n......{}\n'.format(record_string))
            pass

    return record_type

def classify_dataset(dsid_string):
    """Datasets can be classified into 5 types according to the 
       information they present (see ENSDF manual page 3). Here
       those types are tagged as:
       [
           'SUMMARY_INFOS',
           'THE_REFERENCE',
           'ADOPTED_LINES',
           'EVALUATED_DAT',
           'COMBINED_VALS'
        ]
    """
    dataset_type = 'UNKNOWN'
    for k, v in FIELDS['DSID'].iteritems():
        if isinstance(v, list):
            field_re = re.compile(r'|'.join(v))
        else:
            field_re = re.compile(v)

        match = field_re.match(dsid_string)
        if match:
            dataset_type = k
            break

    return dataset_type, match


class record_group(object):
    """A class to represent a group of records which
    are records as in ENSDF manual which belong to the
    the same type and are contiguous in the file.
    TODO: make compatible with two records of different types
    like LEVEL+B- records which always come toghether
    """
    def __init__(self, record_string, recordstype=None):
        """Receives the record in string format (80 character string)
        and determines its type and info based on its content
        """
        self.record_raw = record_string
        self.type = recordstype
        self.A = record_string[:3].strip()
        self.elem = record_string[3:5]

        # might be a continuation record, check char in pos 5
        # which should be any of (1..9, a..z)

        if self.type != 'END':
            self.A = int(self.A)
        
        self._populate_data()

    def _populate_data(self):
        if self.type:
            rtype = self.type
            for field, lim_idcs in RECORD_MEMBERS[rtype].iteritems():
                i1, i2 = lim_idcs[0] - 1, lim_idcs[1]
                self.__setattr__(field, self.record_raw[i1:i2])

    def __iter__(self):
        rtype = self.type
        for attr, value in self.__dict__.iteritems():
            if attr in RECORD_MEMBERS[rtype]:
                yield attr, value


class dataset(object):
    """A class that represents the datasets contained in ENSDF
    """

    def __init__(self, dataset_string, loc):
        """Receives the string representing the dataset, which
        should be composed of 2 or more lines (referred to as 
        `records` in the ENSDF manual. Populates the class members
        according to the information in dataset_string

        Datasets can be classified into 5 types according to the 
        information they present (see ENSDF manual page 3). Here
        those types are tagged as:
        [
            'SUMMARY_INFOS',
            'THE_REFERENCE',
            'ADOPTED_LINES',
            'EVALUATED_DAT',
            'COMBINED_VALS'
        ]

        Arguments:
        ---------
        dataset_string: {str} the dataset, a collection of 80char lines
        """
        if not is_dataset(dataset_string):
            warn('The argument dataset_string does not have a `dataset` structure!')

        self.location = loc
        self.dataset_raw = dataset_string
        self.records = []
        self.type = ''  # the type of dataset (1 of 5)

        # parse string and build list of records, group records 
        rs_lines_list = self.dataset_raw.split(u'\n')

        prev_type = 'IDENTIFICATION'  # all datasets start with this record type
        prev_record = rs_lines_list[0]
        record_string = prev_record + u'\n'
        for rec in rs_lines_list[1:]:
            if rec == '':
                # Residual from split, eliminate in future
                rec = 80 * u' '

            new_record = rec + u'\n'
            new_type = classify_record(new_record)
            
            if (new_type == prev_type) and (new_record[5] > prev_record[5]):
                # If it is a continuation record, char in pos 5
                # should be any of (1..9, a..z)
                # TODO: a group can be interjected by a comment, and this is not taken into account atm.... fix it
                record_string += new_record
            else:
                self.records.append(record_group(record_string, recordstype=prev_type))
                prev_type = new_type
                prev_record = new_record
                record_string = prev_record + u'\n'             
        
        self.A = int(self.records[0].record_raw[:3].strip())
        self.elem = self.records[0].record_raw[3:5].strip()
        self.Z = get_atomic_number(self.elem)
        
        self.type, _ = classify_dataset(self.records[0].DSID)


class ensdf_file(object):
    """A class to represent and contain the information of
    a file in the format of ENSDF. 
    """
    def __init__(self, ensdfname):
            # code_name = 'utf-8'  # closest to ASCII-7 used in ENSDF, python3

            # with open(ensdfname, 'rt', encoding=code_name) as f:  # for python3
            with open(ensdfname, 'rt') as f:
                s = f.read()

            self.datasets = []
            split_datasets = s.split(END_RECORD)
            for dataset_string in split_datasets:
                if dataset_string == u'':
                    # EOF reached
                    continue
                
                # ds = dataset(dataset_string + END_RECORD, None)
                ds = dataset(dataset_string, None)
                
                self.datasets.append(ds)


if __name__ == "__main__":    
    folder = '/home/visitante/decay_tools/ENSDF/'
    ef = ensdf_file('ensdf.039')
    import numpy as np
    import diagnostics

    print diagnostics.check_decay_types()