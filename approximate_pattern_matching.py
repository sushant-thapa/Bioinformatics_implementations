"""
Find all approximate occurrences of a pattern in a string.

Given: Strings Pattern and Text along with an integer d.

Return: All starting positions where Pattern appears as a substring of Text with at most d mismatches.

Sample Dataset
ATTCTGGA
CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC
3
Sample Output
6 7 26 27 78
"""
from hamming_distance import hamming_distance
def approximate_pattern_matching(pattern,text,d):
    d = int(d)
    k = len(pattern) # this gives the length of the pattern
    L = len(text) # this gives the length of the entire string 'text'
    print(pattern)
    print(text)
    print(d)
    

    output = ""
    for i in range(L-k+1):
        if hamming_distance(pattern,text[i:i+k])<=d: output = output+str(i)+" "
    return output
#checking the file pattern, we are using split function to take the input. 
output_to_print = ""
with open("./input.txt","r") as file:
    input_string = file.read()
    [pattern,text,d] = input_string.split('\n')
    # print(pattern)
    # print(text)
    # print(d)
    output_to_print = (approximate_pattern_matching(pattern,text,d))

open('./Output.txt', 'w').close() # the code to delete the contents of a file
with open("./Output.txt", "a") as text_file:    
        # text_file.write(output)
        text_file.write(output_to_print)