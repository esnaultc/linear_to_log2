#!/usr/bin/env python3
# -*- coding: utf-8 -*-

usage = """
Convert linear data to log2 data
Data to convert must be in the 3rd column of tab-separated file

 @author: Caroline Esnault
 Last update: 2018/09/23
"""


import os, sys
import argparse
import pandas as pd
import math

ap = argparse.ArgumentParser(usage=usage)
ap.add_argument('file_to_convert', help='File to convert')
ap.add_argument('--output', '-o', default='out', help='Output file, "out" by default')
args = ap.parse_args()

# input file format:
#chr1   1234    0.15
#chr1   1235    0.29

df = pd.read_table(args.file_to_convert, sep='\t')
values = df.iloc[:, 2]

def log2(df, values, outfile):
    """
    Writes output file after converting the 'column' in 'file_to_convert'

    Parameters
    ----------
    df : DataFrame
        Content of file to convert

    values : list
        list with the data to convert

    outfile : str
        path and name to the output file
    """

    with open(outfile, 'w') as outputfile:
        for i in range(len(values)):
            if values[i]== 0:
                logtwo = 0
            else:
                logtwo= math.log(values[i], 2)
                outputfile.write("%s\t%s\t%s\n" %
                    (df.iloc[i][0], df.iloc[i][1], logtwo)
                    )
                print(df.iloc[i][1])


log2(df, values, args.output)
