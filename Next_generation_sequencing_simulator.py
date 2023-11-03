import random
from reverse_compliment import reverse_compliment
# input_genome_sequence = "ABCDEFGHIJKLMNOP" # This is the sample input to the program
# input_genome_sequence = """AGAAGACGAAGGGGGCGTCTCCCC""" # This is the sample input to the program
coverage = 10 #Number of copies of the genome sequence to create before fragmentation.
insert_size = 4 # This is the length of each fragment
read_length = 3 # length of each sequencing read
seq_error = 0.02 # This is the sequencing error rate
fragments_list = [] # This is where the fragments will be stored
read_list =[] # This is the list where all the reads will be stored
missing_fragment_rate = 0.1 # This is the probability of not sequencing a fragment
input_file_name = "input.txt"
output_file_name = 'read_output.fa'
"""
1> This step we will generate multiple copies of the input_genome_sequence, based on coverage
"""
input_genome_sequence = ''
with open(input_file_name,'r') as file:
     input_genome_sequence = file.read()
input_genome_sequence = input_genome_sequence.replace("\n","") #removing \n chars
input_genome_sequence = input_genome_sequence.replace(" ","") #removing blanks 
genome_sequence_copies = []
for i in range(coverage):
    genome_sequence_copies.append(input_genome_sequence)
# print(*genome_sequence_copies,sep="\n")/

"""
2> We will make the fragments at random intervals.

Initial position is chosen at random, and then we will fragment according to insert_size
"""
counter = 0
for i_genome in genome_sequence_copies:
    temp_frag_list = []
    random_starting_position = random.randrange(0,insert_size) #Generating a random starting position
    first_fragment = ''
    if random_starting_position!=0:
        first_fragment = i_genome[0:random_starting_position]
    remaining = i_genome[random_starting_position::] #generating the fragments for the remainder of the sequence
    
    #
    ## We use a list comprehension below to only make a list from the remaining string. 
    # We also introduce a condition that only inserts the fragment according to a probablility determinded by missing_fragment_rate
    #
    temp_frag_list = [remaining[i:i+insert_size] for i in range(0,len(remaining),insert_size) if random.randint(1,100)>missing_fragment_rate*100 ]
    temp_frag_list.append(first_fragment)
    if '' in temp_frag_list:
        temp_frag_list.remove('')
    fragments_list.extend(temp_frag_list)

"""
3> This is the step where we generate reads from the sequence fragments_list
"""    

# ii. check every element of fragments_list whether a random integer between 1 and 100 is less than the missing_fragment_rate times 100.
    # This step essentially guarantees that there's a missing_fragment_rate percent chance that it is not sequenced
for i_fragment in fragments_list:
    if (random.randint(1,100)<=seq_error*100):
            temp_list = list(i_fragment)
            random.shuffle(temp_list)
            i_fragment = "".join(temp_list)
    read_list.append(reverse_compliment(i_fragment[0:read_length]))
    
    
# print(len(read_list)/len(fragments_list)) # this can be used to validate whether we've achieved the desired missing_fragment_rate

print(*read_list,sep = '\n')

"""
Section where we write the output to a file in FASTA format
"""
with open(output_file_name, 'w') as file:
    for i,i_read in enumerate(read_list):
        file.write(">read "+str(i+1)+"\n")
        file.write(i_read+"\n")


