from hamming_distance import hamming_distance
def substring(pattern):
    return pattern[1:]
alphabets = ['A','C','G','T']
def d_neighbors(pattern,d):
    # print(pattern,d)
    if d == 0:
        return pattern;
    if len(pattern) == 1:
        return alphabets
    one_less_substring = substring(pattern)
    # print(one_less_substring)
    all_d_neighbors_from_one_less_substring = d_neighbors(one_less_substring,d)
    # print("the d neighbors are",all_d_neighbors_from_one_less_substring)
    temp1 = []
    # print("the temp1 is ",temp1)
    for each_d_neighbors_from_one_less_substring in all_d_neighbors_from_one_less_substring:
        # print("each d neighbor is",each_d_neighbors_from_one_less_substring)
        # print("the hamming distance with one_less_substring is",hamming_distance(each_d_neighbors_from_one_less_substring,one_less_substring))
        # print("one less substring is",one_less_substring)
        if hamming_distance(each_d_neighbors_from_one_less_substring,one_less_substring) < d: #this means that i can still afford to fluctuate
            temp1.append('A'+each_d_neighbors_from_one_less_substring)
            temp1.append('C'+each_d_neighbors_from_one_less_substring)
            temp1.append('G'+each_d_neighbors_from_one_less_substring)
            temp1.append('T'+each_d_neighbors_from_one_less_substring)
            # print("temp1 now is ",temp1)
        else: # this just means that I cannot cause variations, which means I literally just have the choice of pattern['0']
            temp1.append(pattern[0]+each_d_neighbors_from_one_less_substring)    
    return temp1
# pattern = "AAC"
# d = 1
# print(d_neighbors(pattern,d))