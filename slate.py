#!/usr/bin/env python

import argparse

OUT_FILE = 'seed.txt'
FILL_CHAR = '.'
ROWS = 20
COLS = 20


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--out', help='Name of output file.', dest='out',
                        default=OUT_FILE)
    parser.add_argument('-r', '--rows', help='Number of rows to fill.',
                        type=int, dest='rows', default=ROWS)
    parser.add_argument('-c', '--cols', help='Number of columns to fill.',
                        type=int, dest='cols', default=COLS)
    parser.add_argument('-f', '--fill', help='Character to fill with.',
                        dest='fill', default=FILL_CHAR)
    args = parser.parse_args()

    # Error checking on arguments.
    if len(args.fill) > 1:
        raise ValueError('--fill must only be a single character.')
    if args.rows < 0:
        raise ValueError('--rows must not be negative.')
    if args.cols < 0:
        raise ValueError('--cols must not be negative.')

    with open(args.out, 'w') as out_file:
        for row in range(args.rows):
            for col in range(args.cols):
                out_file.write(args.fill)
            out_file.write('\n')

if __name__ == '__main__':
    main()

