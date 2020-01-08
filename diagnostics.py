"""Checks to test the ENSDF database or the code
correctly.
"""

folder = '/home/visitante/decay_tools/ENSDF/'
import numpy as np
import re

from my_ensdf_parser import DECAY_MODES, ensdf_file
from nuclei_data import nuclide_data

DSID_decay_template_str = r'(\d{1,3})(\w{1,2})(\[\+\d{1,}\]){0,1} ([\w,+,-]*) DECAY( \(.*\)){0,1}'
DSID_decay_template_rex = re.compile(DSID_decay_template_str)

def check_decay_types():
    """Checks that all decays are known and recorded in the 
    DECAY_MODES list
    """
    mas = []
    modes = []
    unmatched_DSIDs = []
    for k in range(1, 299):
        filename = 'ensdf.{:0>3d}'.format(k)
        ef = ensdf_file(folder + filename)

        for ds in ef.datasets:
            if ds.type == "DECAY":
                output = DSID_decay_template_rex.match(ds.records[0].DSID)
                if output:
                    mode = output.group(4)
                else:
                    unmatched_DSIDs.append(ds.records[0].DSID)
                if mode not in DECAY_MODES:
                    modes.append(mode)
            if 'MUONIC ATOM' in ds.records[0].DSID:
                mas.append(ds.records[0].DSID)

    report = ''
    if modes:
        report += 'The following decay modes were not present in DECAY_MODES:\n{}\n'.format('\n'.join(modes))
    else:
        report += 'No decay modes were found outside of DECAY_MODES.\n\n'

    if unmatched_DSIDs:
        report += 'The following DSIDs were not captures by the regular expresion:\n{}'.format('\n'.join(unmatched_DSIDs))
    else:
        report += 'All DSIDs were captures by the regular expresion.\n'

    if mas:
        report += 'Some muonic atom DSIDs:\n{}\n'.format('\n'.join(mas))

    return report
    

def extract_decays():
    """Checks that all decays are known and recorded in the 
    DECAY_MODES list
    """
    nuc_by_decays = {}
    for k in range(1, 29):
        filename = 'ensdf.{:0>3d}'.format(k)
        ef = ensdf_file(folder + filename)

        for ds in ef.datasets:
            if ds.type == "DECAY":
                output = DSID_decay_template_rex.match(ds.records[0].DSID)

                if output:
                    A = output.group(1)
                    elem = output.group(2)
                    if len(elem) == 2:
                        elem = elem[0] + elem[1:].lower()
                    if elem in nuclide_data['symbols']:
                        Z = nuclide_data['symbols'].index(elem)
                        ncosid = int(A)*100+Z
                    else:
                        ncosid = str(A) + elem
                                            
                    # Eexc = output.group(3)
                    mode = output.group(4)
                    
                    if ncosid in nuc_by_decays:
                        nuc_by_decays[ncosid].append(mode)
                    else:
                        nuc_by_decays[ncosid] = [mode]

    return nuc_by_decays


def extract_adoptedlevels(maxA = 30):
    """Checks that all decays are known and recorded in the 
    DECAY_MODES list
    """
    nuc_with_adlev = []
    for k in range(1, maxA):
        filename = 'ensdf.{:0>3d}'.format(k)
        ef = ensdf_file(folder + filename)

        for ds in ef.datasets:
            # if "ADOPTED LEVELS" in ds.records[0].record_raw:
            if ds.type == "ADOPTED LEVELS":
                A = int(ds.records[0].record_raw[:3].strip())
                elem = ds.records[0].record_raw[3:5].strip()
                if len(elem) == 2:
                    elem = elem[0] + elem[1:].lower()
                if elem in nuclide_data['symbols']:
                    Z = nuclide_data['symbols'].index(elem)
                    ncosid = int(A)*100+Z
                else:
                    ncosid = str(A) + elem
                nuc_with_adlev.append(ncosid)

    return nuc_with_adlev


def extract_dataset_by_type(dataset_type='REFERENCES', maxA = 30):
    """Checks that all decays are known and recorded in the 
    DECAY_MODES list
    """
    nuc_with_adlev = []
    for k in range(1, maxA):
        filename = 'ensdf.{:0>3d}'.format(k)
        ef = ensdf_file(folder + filename)

        for ds in ef.datasets:
            if ds.Z > 0:
                ncosid = int(ds.A) * 100 + ds.Z
                nuc_with_adlev.append(ncosid)
            else:
                pass
                # print 'unequal types.....: ds-{} and arg-{}'.format(ds.type, dataset_type)

    return nuc_with_adlev


def extract_datasets(maxA = 30):
    """Checks that all decays are known and recorded in the 
    DECAY_MODES list
    """
    nuc_with_adlev = []
    for k in range(1, maxA):
        filename = 'ensdf.{:0>3d}'.format(k)
        ef = ensdf_file(folder + filename)

        for ds in ef.datasets:
            if "ADOPTED LEVELS" in ds.records[0].record_raw:
                A = int(ds.records[0].record_raw[:3].strip())
                elem = ds.records[0].record_raw[3:5].strip()
                if len(elem) == 2:
                    elem = elem[0] + elem[1:].lower()
                if elem in nuclide_data['symbols']:
                    Z = nuclide_data['symbols'].index(elem)
                    ncosid = int(A)*100+Z
                else:
                    ncosid = str(A) + elem
                nuc_with_adlev.append(ncosid)
                # if (A == 18) and (Z == 2):
                #     print ds.records[0].record_raw[:25]
            # else:
            #     print ds.records[0].record_raw[:5]
    return nuc_with_adlev


if __name__ == "__main__":

    # print check_decay_types()
    extract_decays()