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

import numpy as np
from warnings import warn

def is_dataset(string):
    """Checks whether string complies with dataset structure expected
    according to ENSDF manual
    """
    return True

def classify_record(record_string):
    """Identifies the record type from one of the 15 different
    types defined in ENSDF manual
    """
    record_type = None
    if record_string[7] == 'H':
        record_type = 'HISTORY'
    elif record_string[7] == 'Q':
        record_type = 'Q-VALUE'
    elif record_string[7] == 'X':
        record_type = 'CROSS-REFERENCE'
    elif record_string[7] == 'P':
        record_type = 'PARENT'
    elif record_string[7] == 'N':
        record_type = 'NORMALIZATION'
        if record_string[5:7] == 'PN':
            record_type = 'PRODUCTION NORMALIZATION'
    elif record_string[7] == 'L':
        record_type = 'LEVEL'
    elif record_string[7] == 'B':
        record_type = 'BETA MINUS'
    elif record_string[7] == 'E':
        record_type = 'EC / BETA PLUS'
    elif record_string[7] == 'A':
        record_type = 'ALPHA'
    elif record_string[7] == 'D':
        record_type = 'DELAYED PARTICLE'
    elif record_string[7] == 'G':
        record_type = 'GAMMA'
    elif record_string[7] == 'R':
        record_type = 'REFERENCE'
    elif record_string[6] in ['c', 'd', 't', 'C', 'D', 'T']:
        record_type = 'COMMENT'
    elif record_string == END_RECORD:
        record_type = 'END'
    elif record_string[6:9] == 3 * r' ':
        record_type = 'IDENTIFICATION'
    else:
        warn('Record not within expected types!\n......{}\n'.format(record_string))

    return record_type

def classify_dataset(dataset_object):
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
    rtypes = []
    dataset_type = 'OTHER'
    for r in dataset_object.records[1:-1]:
        rtypes.append(r.type)
    
    if np.all(np.array(rtypes) == 'REFERENCE'):
        dataset_type = 'THE_REFERENCE'
    
    return dataset_type


class record_group(object):
    """A class to represent a group of records which
    are records as in ENSDF manual which belong to the
    the same type and are contiguous in the file.
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
        record_string = ''
        rs_lines_list = self.dataset_raw.split(u'\n')

        prev_type = 'IDENTIFICATION'  # all datasets start with this record type
        prev_record = rs_lines_list[0]
        for rec in rs_lines_list[1:]:
            if rec == '':
                # Residual from split
                rec = 80 * u' '

            new_record = rec + u'\n'
            new_type = classify_record(new_record)
            
            if (new_type == prev_type) and (new_record[5] > prev_record[5]):
                # If it is a continuation record, char in pos 5
                # should be any of (1..9, a..z)
                record_string += new_record
            else:
                self.records.append(record_group(prev_record, recordstype=prev_type))
                prev_type = new_type
                prev_record = new_record                
        self.type = classify_dataset(self)


class ensdf_file(object):
    """A class to represent and contain the information of
    a file in the format of ENSDF. 
    """
    def __init__(self, ensdfname):
            code_name = 'utf-8'  # closest to ASCII-7 used in ENSDF, python3

            # with open(ensdfname, 'rt', encoding=code_name) as f:  # for python3
            with open(ensdfname, 'rt') as f:
                s = f.read()

            self.datasets = []
            split_datasets = s.split(END_RECORD)
            for dataset_string in split_datasets:
                if dataset_string == u'':
                    # EOF reached
                    continue
                
                ds = dataset(dataset_string + END_RECORD, None)
                
                self.datasets.append(ds)


if __name__ == "__main__":    
    folder = '/home/visitante/decay_tools/ENSDF/'
    ef = ensdf_file('ensdf.039')
    import numpy as np
    for k in range(1, 299):
        filename = 'ensdf.{:0>3d}'.format(k)
        ef = ensdf_file(folder + filename)
    # for k, ds in enumerate(ef.datasets):
    #     for rec in ds.records:
    #         print(rec.A, rec.elem, rec.type)
        if len(ef.datasets) > 1:
            # rtypes = np.array([r.type for r in ef.datasets[1].records[1:-1]])
            print(ef.datasets[1].type)
        else:
            continue
        
        # if not np.all(rtypes == 'REFERENCE'):
        #     print(filename, np.all(rtypes == 'REFERENCE'))

