"""
The following code calculates the hamming distance between two strings

Things to note: 

1. The length of the input strings must be the same 

"""
def hamming_distance(string1,string2):
    
    if len(string1)!=len(string2):
        raise Exception("the length is not the same") 
    
    hamming_distance = 0
    for i in range(len(string1)):
        if string1[i]!=string2[i]:
            hamming_distance = hamming_distance+1
    return hamming_distance