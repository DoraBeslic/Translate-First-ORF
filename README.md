# translate_first_orf.py
## Overview: Gets fasta file from user, reads file, if fasta record id matches inputted id or default id, find first orf and translate it. Communicate id and translated sequence back to user. 
## Author: Isidora Beslic
## Date created: February 23, 2023
## Date started: February 20, 2023
## Running identify_sequence_refactored.py:
### Calling on the command line: python translate_first_orf.py [path to fasta file]
## Tests: 
test_translate_first_orf.py (run with pytest)
- test_short_orf: pass
- test_orf_in_orf: pass
- test_missing_stop_codon: pass
- test_out_of_frame_stop: pass
- test_dna_sequence: pass
