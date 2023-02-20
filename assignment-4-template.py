#!/usr/bin/env python
"""TODO: Say what the code does

TODO: Elaborate on what the code does
"""

import argparse
#TODO import other libraries needed


def get_args():
    """Return parsed command-line arguments."""

    parser = argparse.ArgumentParser(
        description="TODO: say what the script does.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # get the FASTA file of sequences
    parser.add_argument('filename',  # variable to access this data later: args.filename
                        metavar='FASTA', # shorthand to represent the input value
                        help='Provide name and path to FASTA file to process.', # message to the user, it goes into the help menu
                        type=str)
    parser.add_argument('-p', '--pattern',  # access with args.pattern
                        help='Provide a regex pattern for filtering FASTA entries',
                        default='^\d{1}\D*$')  # default works for Drosophila chromosomes

    return(parser.parse_args())


def find_first_orf(rna):
    """Return first open-reading frame of RNA sequence as a Bio.Seq object.

    Must start with AUG
    Must end with UAA, UAG, or UGA
    Must have even multiple of 3 RNA bases between
    """
    try:
        #TODO update regex to find the ORF
        orf = re.search('TODO: your regex', str(rna)).group()
    except AttributeError:  # if no match found, orf should be empty
        orf = ""
    return(Seq(orf))


def translate_first_orf(dna):
    """TODO: what it does

    Assumes input sequences is a Bio.Seq object.
    """

    # TODO: transcribe the DNA, find the first ORF, translate said ORF

    return(translated_orf)


if __name__ == "__main__":
    #TODO: get command-line arguments

    #TODO: use SeqIO to get the records in the fasta file provided by the command-line input
    #TODO: if the FASTA record's ID matches the regex pattern,
    #      then print out its record ID then a tab space then the translated first ORF
   