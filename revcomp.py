#!/usr/bin/env python3
## Convert lines of DNA sequences into their reverse-complement counterpart.
##
## This script will process line per line of DNA sequences in no given format and will output
## the corresponding reverse-complement sequences.
## Each line is considered a different sequence.
##
## Amaury Pupo Merino
## amaury.pupo@gmail.com
##
## This script is released under GPL v3.
##

## Importing modules
import argparse
import sys
from Bio.Seq import Seq

## Functions

## Main
def main():
    """Main function.
    """
    parser=argparse.ArgumentParser(description="Convert lines of DNA sequences into their reverse-complement counterpart.")
    parser.add_argument('inseqfile', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='Input sequence file [default: stdin].')
    parser.add_argument('outseqfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout, help='Output sequence file [default: stdout].')
    parser.add_argument('-v', '--version', action='version', version='1.0.0', help="Show program's version number and exit.")

    args=parser.parse_args()

    for line in args.inseqfile:
        line=line.strip()
        seq = Seq(line)
        rc_seq = seq.reverse_complement()
        args.outseqfile.write("{}\n".format(rc_seq))                
                  

## Running the script
if __name__ == "__main__":
        main()
