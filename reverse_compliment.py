"""
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'. Given a nucleotide p, we denote its complementary nucleotide as p. The reverse complement of a DNA string Pattern = p1…pn is the string Pattern = pn … p1 formed by taking the complement of each nucleotide in Pattern, then reversing the resulting string.

For example, the reverse complement of Pattern = "GTCA" is Pattern = "TGAC".

Reverse Complement Problem
Find the reverse complement of a DNA string.

Given: A DNA string Pattern.

Return: Pattern, the reverse complement of Pattern.
"""

def single_base_compliment(base):
    if base == "A":
        return "T"
    elif base == "T":
        return "A"
    elif base == "G":
        return "C"
    elif base =="C":
        return "G"
    else:
        raise Exception("The base you gave is ```", base, "```This base not recognized. base should be A, C, G, or T")

def reverse_string(sequence):
    return sequence[-1::-1] # here we follow the syntax of "start:stop:step". Thus we are starting at the last element.

input_string = "GTCA"
input_string = input_string.upper()

"""
This is function that performs the reverse compliment. 
The input is the string for which you want to do the operation
"""
def reverse_compliment(input_string):
    output_string = ""
    for i in input_string:
        output_string = output_string + single_base_compliment(i) # step of calculating compliment for each step

    output_string = reverse_string(output_string) #step of doing the reverse of the string
    return output_string


 


