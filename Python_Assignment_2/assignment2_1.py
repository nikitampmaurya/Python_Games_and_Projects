# Declaration:

# I, [Nikita Mahendraprasad Maurya], declare that I have employed a Chat-GPT-4o,
# to check logic, redundancy, identify and handle potential
# exceptions and errors. 

import re #regular expression library

def read_fasta_file(filename): #accept dna sequence file in fasta format as input parameter
    # there is only one entry in the file 
    with open(filename, "r") as f: #to read the file
        counter = 0 #to skip the header
        name = "" #to store record description of the dna seq
        dna = "" #to store the dna sequence
        for line in f: #to read line by line
            line = line.strip() #to remove whitespaces from each line
            if counter == 0: #to refer header
                name = line #to store record description of the dna seq to the name object
            else:
                dna += line #to join and store each line of the dna seq

            counter += 1

    name = re.sub('>','',name) #to remove '>' from the record description
    return [name, dna] #to get record_description and dna seq

# to check the output

# input_fasta_file = "Oryza_sativa.IRGSP-1.0.dna.toplevel.fa1.fasta"
# result = read_fasta_file(input_fasta_file)
# print(result[0])  #get only name/record_description
# print(result[1][:2000]) #get only first 1000 dna sequence

# column -t -s $'\t' O_sativa_chr1.gff | less -S to view the .gff file in ubuntu instead of excel

#explanation for RE
# grep ">" filename } wc -l to count no of dna seq and protein seq

"""
filter_cds function filters only cds rows from the .gff file and return a dictionary with unique locus id as key
and starting and ending position of cds along with +/- strand infomation
"""

def filter_cds(filename): #to accept .gff file as input parameter
    cds_dict = {} #to store ids/headers as keys and start,end and forward/reverse strand as values
    with open(filename,"r") as f: #to read the .gff file
        counter = 0 #to skip header
        for line in f:
            line = line.strip()
            if counter != 0:
                cells = line.split("\t") #to separate each column by tab
                type_seq = cells[2]
                start = int(cells[3]) - 1 #because python starts counting from 0 instead of 1
                end = int(cells[4])  #but genomic coordinates start counting from 1 instead of zero.
                strand = cells[6]
                locus = cells[8]

                if type_seq == "CDS": #to retrieve only CDS lines
                    match = re.search(r'(?<=\=)[^:]+(?=\:)', locus) #to get only id from last column
                    if match:  # if a match exist
                        locus_id = match.group(0)  # to return entire match
                        if locus_id not in cds_dict:
                            cds_dict[locus_id] = [] #add locus id as key
                        cds_dict[locus_id].append([start, end, strand]) # add starting, ending position along with type of strand as value

            counter +=1
    return cds_dict


#gff_file = "O_sativa_chr1.gff"
#cds_data = filter_cds(gff_file)
#print(cds_data)

"""
reverse_fragment will convert all - strands into reverse complement 
"""

def reverse_fragment(seq): #to translate and reverse the cdna seq
    trans_table = str.maketrans("ATCG","TAGC") #this table replaces A with T, T with A, C with G, and G with C
    complement_seq = seq.translate(trans_table) #this function carries out the replacement
    reversed_complement_seq = complement_seq[::-1] #this is to reverse the seq after replacing the nucleotides

    return reversed_complement_seq

#dna_seq = "ATGC"
#print(reverse_fragment(dna_seq))

"""
this function will return a dictionary where locus ids are keys and fragments are the list of values
"""

def retrieve_fragment(cds_dict,dna_seq): #accpet a dictionary where id as keys and coordinates are value and also dna seq
    fragment_dict = {}

    for locus_ids,data in cds_dict.items():
        fragment_list = [] #to store all the fragments associated with each id

        for ind in data: #refering to the values of each key
            fragment = dna_seq[ind[0]:ind[1]+1] #since python slicing excludes last postion so to include it we use +1

            if ind[2] == "-": #if the third entry of each value is a reverse strand
                fragment = reverse_fragment(fragment) #then we convert it to template strand

            fragment_list.append(fragment) #then add it to our fragment list

        fragment_dict[locus_ids] = fragment_list #then we add list of fragments for each lcous id to the final list

    return fragment_dict #then we return the list

#input_fasta_file = "Oryza_sativa.IRGSP-1.0.dna.toplevel.fa1.fasta"
#gff_file = "O_sativa_chr1.gff"
#result = read_fasta_file(input_fasta_file)
#cds_data = filter_cds(gff_file)

#retrieved_fragments = retrieve_fragment(cds_data, result[1])

#print(retrieved_fragments)

#index = 0  # to show the no of cds fragments for first lcous id of the cds_dict dictionary
#key_at_index = list(retrieved_fragments.keys())[0] #convert all keys into a list

#length_of_value_list = len(retrieved_fragments[key_at_index]) #to get length of the value list

#print(f"The length of the value list for the key at index {index} ({key_at_index}) is: {length_of_value_list}")

"""
join_fragments will join the fragments of each key
"""

def join_fragments(fragment_dict): #accepts a dictionary where locus is key and value is list of fragments
    dna_seq_dict = {} #dictionary to store locus id as key and long dna seq
    for id, fragments in fragment_dict.items(): #reading locus id as key and list of fragments as values
        joined_fragments = ''.join(fragments) #join all the fragments
        dna_seq_dict[id] = joined_fragments #append them to the dictionary
    return dna_seq_dict #return the dictionary

input_fasta_file = "Oryza_sativa.IRGSP-1.0.dna.toplevel.fa1.fasta"
gff_file = "O_sativa_chr1.gff"

result = read_fasta_file(input_fasta_file)
cds_data = filter_cds(gff_file)
retrieved_fragments = retrieve_fragment(cds_data, result[1])
final_dict = join_fragments(retrieved_fragments)

def write_fastafile(fasta_dict,outputfile): #accepts dictionary where locus id is key and dna seq is value and write them in a outputfile
    with open(outputfile, "w") as f:
        for header,seq in fasta_dict.items():
            f.write(f">{header}\n")
            f.write(f"{seq}\n")

output_fasta_file = "outputfile_1a.fasta"

write_fastafile(final_dict, output_fasta_file)

def translate_dna(dna_dict, codon_table): #accepts list of codon and dictionary where locus id is key and dna seq is value
    protein_dict = {} #to store protein id as key and protein as value

    for locus_id,dna_seq in dna_dict.items():
        protein = "" #to make protein

        rna_seq = dna_seq.replace("T","U")

        for i in range(0,len(rna_seq),3): #to read only three nucleotides at a time and not overlap
            codon = rna_seq[i: i + 3]
            if len(codon) != 3:
                continue
            if codon in codon_table:
                if codon_table[codon] == "*": #to add * for stop codon
                    protein += codon_table[codon] #to add amino acid
                    continue
                else:
                    protein += codon_table[codon] #to add amino acid
            else:
                print(f"Error: This Codon {codon} is not present codon table and locus id is {locus_id}")
                protein += "N" #for unknown codon
        protein_dict[locus_id] = protein #to store protein id as locus id and protein as value

    return protein_dict

codon_menu =  {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "UGA": "*", "UGU": "C", "UGC": "C", "UGG": "W",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

translated_proteins = translate_dna(final_dict, codon_menu)

#for locus_id, protein in translated_proteins.items():
    #print(f"{locus_id}: {protein}")

def write_proteinfile(protein_dict,outputfile): #uses protein dictionary where lcous id are key and protein are value
    with open(outputfile, "w") as f:
        for header,seq in protein_dict.items():
            f.write(f">{header}\n")
            f.write(f"{seq}\n")

outputfile = "outputfile_1b.fasta"

write_proteinfile(translated_proteins, outputfile)
