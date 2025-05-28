# Declaration:

# I, [Nikita Mahendraprasad Maurya], declare that I have employed a Chat-GPT-4o,
# to check logic, redundancy, identify and handle potential
# exceptions and errors that may arise during execution.

import re

def search_motif(input_file, output_file): #accept protein fasta file
    pattern = r"A.[RK][SY]R.[RK]K" #the motif of our interest
    motif_pattern = re.compile(pattern) #looks for this motif
    protein = {} #to store protein id as key and protein as value
    current_header = None
    with open(input_file,"r") as f: #reads my input file of protein seq in fasta format
        for line in f: #read line by line
            line = line.strip() #to remove whitespaces from each line
            if line.startswith(">"): #to identify headers
                current_header = line #assign the entire line to current_header object
                protein[current_header] = "" #store header as key
            elif current_header: #if there is a header
                protein[current_header] += line #to store dna seq lines

    with open(output_file, "w") as f1: #to write protein seq along with headers and motif starting position in another fasta file
        for header, seq in protein.items():
            m = motif_pattern.search(seq)
            if m:
                f1.write(f"{header} motif_pos = {m.start()}\n{seq}\n")

    return protein

input_file = "outputfile_1b.fasta"
output_file = "outputfile_2.fasta"
protein_dictionary = search_motif(input_file,output_file)
