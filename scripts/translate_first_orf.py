#!/usr/bin/env python
"""Translates first orf of inputted fasta files 

Gets fasta file from user, reads file, if fasta record id matches inputted id or defualt id, find first orf and translate it.
Communicate id and translated sequence back to user. 
"""

import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import re

def get_args():
    """Return parsed command-line arguments."""

    parser = argparse.ArgumentParser(
        description="parses fasta file",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # get the FASTA file of sequences
    parser.add_argument('filename',  # variable to access this data later: args.filename
                        metavar='FASTA', # shorthand to represent the input value
                        help='Provide name and path to FASTA file to process.', # message to the user, it goes into the help menu
                        type=str)
    parser.add_argument('-p', '--pattern',  # access with args.pattern
                        help='Provide a regex pattern for filtering FASTA entries',
                        default='^\\d{1}\\D*$')  # default works for Drosophila chromosomes

    return(parser.parse_args())


def find_first_orf(rna):
    """Return first open-reading frame of RNA sequence as a Bio.Seq object.

    Must start with AUG
    Must end with UAA, UAG, or UGA
    Must have even multiple of 3 RNA bases between
    """
    try:
        # update regex to find the ORF
        orf = re.search('AUG([AUGC]{3})+?(UAA|UAG|UGA)', str(rna)).group()

    except AttributeError:  # if no match found, orf should be empty
        orf = ""
    return(Seq(orf))


def translate_first_orf(dna):
    """Return translated first orf 

    Assumes input sequences is a Bio.Seq object.
    """

    # transcribe the DNA, find the first ORF, translate said ORF
    rna = dna.transcribe()
    rna_orf = find_first_orf(rna)
    translated_orf = rna_orf.translate()
    return(translated_orf)


if __name__ == "__main__":

    # get command-line arguments
    args = get_args()

    #use SeqIO to get the records in the fasta file provided by the command-line input
    with open(args.filename) as file:
        for record in SeqIO.parse(file, "fasta"):

            # if the FASTA record's ID matches the regex pattern print out its record ID and translated first ORF
            if re.match(args.pattern, record.id):
                dna = record.seq
                first_orf = translate_first_orf(dna)
                print(f'{record.id}\t{first_orf}')
  
   