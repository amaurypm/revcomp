# revcomp
Convert lines of DNA sequences into their reverse-complement counterpart.

## Usage
`revcomp [-h] [-v] [inseqfile] [outseqfile]`

positional arguments:
  * `inseqfile`      Input sequence file [default: stdin].
  * `outseqfile`     Output sequence file [default: stdout].

options:
  * `-h`, `--help`     Show this help message and exit
  * `-v`, `--version`  Show program's version number and exit.

This script will process line per line of DNA sequences in no given format and will output the corresponding reverse-complement sequences.

Each line is considered a different sequence.

## Installation
This is a Python script, so, you can just run the revcomp.py file or put a symbolic link in any directory of your PATH.

## Dependencies
* Python3
* Biopython
* argparse

## OSs
Wherever Python runs.

## Examples
* `echo GATCG | revcomp`

  * output: `CGATC`
* `revcomp dna_seqs_per_line.txt rc_dna_seqs.txt`
