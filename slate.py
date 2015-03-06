#!/usr/bin/env python
#
# Copyright (c) 2015 Adam Heins
#
# This file is part of the Multicell project, which is distributed under the MIT
# license. For the full terms, see the included LICENSE file.
#

import argparse
import os.path
import re

# Defaults.
OUT_FILE = 'seed.txt'
FILL_CHAR = '.'
ROWS = 35
COLS = 100


def clean(out_file, rows, cols):
    """ Rewrites the file as a clean slate. """
    with open(out_file, 'w') as out_file:
        for row in range(rows):
            for col in range(cols):
                out_file.write(FILL_CHAR)
            out_file.write('\n')

def main():
    """ Setup. """
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--out', help='Name of output file.', dest='out',
                        default=OUT_FILE, metavar='out_file')
    parser.add_argument('-r', '--rows', help='Number of rows to fill.',
                        type=int, dest='rows', default=ROWS, metavar='rows')
    parser.add_argument('-c', '--cols', help='Number of columns to fill.',
                        type=int, dest='cols', default=COLS, metavar='cols')
    parser.add_argument('-f', '--force', help="Don't ask before overwriting a "
                        "file.", dest='force', action='store_true')
    args = parser.parse_args()

    # Error checking on arguments.
    if args.rows < 0:
        raise ValueError('--rows must not be negative.')
    if args.cols < 0:
        raise ValueError('--cols must not be negative.')

    # Prompt user to confirm file overwrite, if force flag is not present.
    edit = True
    if not args.force and os.path.exists(args.out):
        input_ = raw_input('The file {} already exists. Do you want to '
                           'overwrite it? [Y/n] '.format(args.out))
        edit = input_ == '' or re.match('[Yy](es)?', input_)

    if edit:
        clean(args.out, args.rows, args.cols)

if __name__ == '__main__':
    main()

