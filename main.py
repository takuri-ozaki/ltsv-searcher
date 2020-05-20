#!/usr/bin/env python
import sys
import os
import traceback
from collections import OrderedDict
from io import StringIO
import pandas as pd

FILE_SIZE_LIMIT = 1024 * 1024
pd.set_option('display.max_rows', None)


def main():
    args = sys.argv
    if len(args) != 2 and len(args) != 3:
        print("usage main.py [filepath] [query(optional)]\n"
              "if you specify \"-\" in the filepath, load from stdin instead of file\n"
              "buffering is not supported")
        exit(1)

    filepath = args[1]

    try:
        if filepath != "-" and os.path.getsize(filepath) > FILE_SIZE_LIMIT:
            print("too large file, file size limit is %d bytes (file size: %d bytes)"
                  % (FILE_SIZE_LIMIT, os.path.getsize(filepath)))
            exit(1)
    except FileNotFoundError:
        print("file not found")
        exit(1)

    df = load_ltsv_and_return_df(filepath)

    if len(args) == 2:
        print(df)
        exit(0)

    pd_query = args[2]
    print(df.query(pd_query))


def load_ltsv_and_return_df(filepath):
    try:
        if filepath == "-":
            df = ltsv_to_df(sys.stdin)
        else:
            with open(filepath) as f:
                df = ltsv_to_df(f)
        return df
    except Exception as e:
        print("exception occurred!\n", traceback.format_exc())
        exit(1)


def ltsv_to_df(file):
    return pd.read_table(StringIO(pd.DataFrame([OrderedDict(cell.split(':', 1)
                                                            for cell in line.rstrip('\n').split('\t'))
                                                for line in file]).to_csv(sep='\t', index=False)))


if __name__ == '__main__':
    main()
