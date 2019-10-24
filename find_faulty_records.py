# Parse ENSDF files and report on faulty records
import numpy as np
from my_ensdf_parser import classify_record

folder = '/home/visitante/decay_tools/ENSDF/'

report = {}
for k in range(1, 299):
    filename = 'ensdf.{:0>3d}'.format(k)
    with open(folder + filename, 'r') as f:
        lines = f.readlines()

    for k, r in enumerate(lines):
        if classify_record(r) is None:
            if filename in report:
                report[filename].append((k, r))
            else:
                report[filename] = [(k, r)]

with open('Report_faulty_records.txt', 'w') as f:
    for filename, instances in report.items():
        f.write(filename + '\n')
        f.write('\t      - ....5...10....5...20....5...30....5...40....5...50....5...70....5...80' + '\n')
        for line_number, record in instances:
            f.write('\t{:>5d} - {}'.format(line_number,record))
        f.write('\n')
