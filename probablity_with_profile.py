
profile = {
'A':[0.11,1.00,0.56,0.22],
'C':[0.11,0.11,0.22,0.33],
'G':[0.67,0.11,0.11,0.22],
'T':[0.11,0.67,0.11,0.22]
}





def calculate_probablity_of_kmer(kmer,profile):
    """
         The following function calculates the probablity of a kmer, given a profile.
        it calculates P(kmer|profile)
    """
    if(len(kmer)!=len(profile['A']) or len(kmer)!=len(profile['C']) or len(kmer)!=len(profile['G']) or len(kmer)!=len(profile['T'])):
        raise Exception('the profile length and kmer length do not match')
    output_string =''
    output_value = 1
    for i,nucleotide in enumerate(kmer):
        output_string += str(profile[nucleotide][i])+"*"
        output_value = output_value*profile[nucleotide][i]
    output_string = output_string[:-1] #this eliminates the last character *
    # print(kmer,end='\t')
    # print(output_string,end='\t')
    # print(round(output_value,5))
    return round(output_value,5)
        
"""
The following shows how the function above could be used.
seq = ['ACGTAACACCGT','TGGTACGTCCCA','CGTCGCTCGTGA','CCGAAGGGTACG','CGAACGTATACG']
for seq in seq:
    L = len(seq)
    k = 4; 
    kmers =[]
    prob_value_max = 0
    kmer_max = seq[0:0+k]
    for i in range(L-k+1):
        i_kmer = (seq[i:i+k])
        kmers.append(i_kmer)
        i_prob = calculate_probablity_of_kmer(i_kmer,profile)
        if(i_prob>prob_value_max):
            kmer_max = i_kmer
            prob_value_max = i_prob
    print(kmer_max,"has the maximum probablity of ",prob_value_max)

"""







