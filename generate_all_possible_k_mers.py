alphabets = ['A','C','G','T']

def cartesian_product_string(listA,listB):
    output = []
    for i in listA:
        for j in listB:
            output.append(i+j)
    return output

def generate_all_possible_k_mers(k):
    if(k ==1):
        return alphabets
    output = alphabets
    for i in range(k-1):
        output = cartesian_product_string(output,alphabets)
    return output


