"""
Given a collection of strings Dna and an integer d, a k-mer is a (k,d)-motif if it appears in every string from Dna with at most d mismatches. The following algorithm finds (k,d)-motifs.

    MOTIFENUMERATION(Dna, k, d)
        Patterns ← an empty set
        for each k-mer Pattern in Dna
            for each k-mer Pattern’ differing from Pattern by at most d
              mismatches
                if Pattern' appears in each string from Dna with at most d
                mismatches
                    add Pattern' to Patterns
        remove duplicates from Patterns
        return Patterns
Implanted Motif Problem
Implement MotifEnumeration (shown above) to find all (k, d)-motifs in a collection of strings.

Given: Integers k and d, followed by a collection of strings Dna.

Return: All (k, d)-motifs in Dna.

Sample Dataset
3 1
ATTTGGC
TGCCTTA
CGGTATC
GAAAATT
Sample Output
ATA ATT GTT TTT
"""

from d_neighbords import d_neighbors

def check_if_kmer_exists_in_all_strings_with_d_mismatches(dna,kmer,d):
    number_of_strings = dna.count('\n')
    individual_strings = dna.split('\n')
    print(individual_strings[0]=='')
    individual_strings.remove('')
    individual_strings.remove('')
    print(individual_strings)

def motif_enumeration(dna,k,d):
    dna = dna.split('\n')
    for i_string in dna:
        for i in range(len(i_string)-k+1):
            d_neighbors_temp = d_neighbors(i_string[i:i+k],d)
            for i_candidate in d_neighbors_temp:
                None
    # return dna

dna = """
ATTTGGC
TGCCTTA
CGGTATC
GAAAATT
xyz
"""
k = 3
d = 1
# output_to_print = motif_enumeration(dna,k,d)
# print(output_to_print)
check_if_kmer_exists_in_all_strings_with_d_mismatches(dna,k,d)