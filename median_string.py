"""
Given a k-mer Pattern and a longer string Text, we use d(Pattern, Text) to denote the minimum Hamming distance between Pattern and any k-mer in Text,
d(Pattern,Text)=minall k-mers Pattern' in TextHammingDistance(Pattern,Pattern′).

Given a k-mer Pattern and a set of strings Dna = {Dna1, … , Dnat}, we define d(Pattern, Dna) as the sum of distances between Pattern and all strings in Dna,

d(Pattern,Dna)=∑i=1td(Pattern,Dnai).

Our goal is to find a k-mer Pattern that minimizes d(Pattern, Dna) over all k-mers Pattern, the same task that the Equivalent Motif Finding Problem is trying to achieve. We call such a k-mer a median string for Dna.
"""

"""
Find a median string.
Given: An integer k and a collection of strings Dna.
Return: A k-mer Pattern that minimizes d(Pattern, Dna) over all k-mers Pattern. (If multiple answers exist, you may return any one.)
"""
from generate_all_possible_k_mers import generate_all_possible_k_mers
from min_hamming_distance import min_hamming_distance

def median_string(dna,k):
    output_dict = {}
    candidate_k_mers = generate_all_possible_k_mers(k)
    for i_kmer in candidate_k_mers:
        hamming_distance_sum = 0
        for j_dna in dna:
            hamming_distance_sum = hamming_distance_sum+ min_hamming_distance(j_dna,i_kmer)[0]
        output_dict[i_kmer] = hamming_distance_sum
    return output_dict

#input section 
k = 6
# Dna = """AAATTGACGCAT
# GACGACCACGTT
# CGTCAGCGCCTG
# GCTGAGCACCGG
# AGTACGGGACAG"""

Dna = """TATAGAGAGCCTCCATTACAATTCCTCCCTCGATGACACTGC
ATTTCATAATATCGTCTCCTCCCTCAAAGCTGGAAGATATTC
TAGCGGTCTTGCGGCAGATCGGTCCGAAAACTATTCCTCTCT
AACCGGCTCCCTTGCAACCTGATGTTACTTATTTGACCAGAC
ACTATTATTCAGGCATAAAGCGCACTCTCTACTCTAGCAGGT
ACCTCGGTCCTCGCAATGCCCGTTCAGCGTTCCGTACTCCCT
GCTCCAAAGAAACCCGGCCTCACTGCATCGACCAACCAGTTC
TAAGGTGTAAGTACTCAACTCTCTATTACTTGTTCGACGGAG
CGGGCGAAAAGAATCACGTACATACGCTCGAGAGTGCTCGCT
AAATGTACGAAGTACGCCGCGCAGGAAGCTCTCACTGACTGG"""
dna_in_list = Dna.split('\n')
output_dict = median_string(dna_in_list,k)

min_value = min(output_dict.values())
output_string = ""
for i_key in output_dict.keys():
    print(output_dict[i_key],min_value)
    if output_dict[i_key] == min_value:
        output_string = output_string+i_key+" "
        

print(output_string)










