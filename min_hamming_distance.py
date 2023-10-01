"""
the following function gives the minimum hamming distance between the pattern and any kmer in the text
"""
from hamming_distance import hamming_distance
def min_hamming_distance(pattern,text):
    min_hamming_distance = len(text)
    min_hamming_kmer = "" # this is the kmer where the minimum hamming distance occurs
    for i in range(len(pattern)-len(text)+1): 
        i_kmer = (pattern[i:i+len(text)])
        i_hamming_distance = hamming_distance(i_kmer,text)
        if i_hamming_distance<min_hamming_distance:
            min_hamming_distance = i_hamming_distance
            min_hamming_kmer = i_kmer
    return [min_hamming_distance,min_hamming_kmer]
