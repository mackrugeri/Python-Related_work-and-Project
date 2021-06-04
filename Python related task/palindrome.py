def reverse_complement(dna):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([complement[base] for base in dna[::-1]]) 
def rev_palindrome(string_of_dna):
    list_of_dna = list(string_of_dna)
    listing = []
    second_list=[]
    concatnation = ""
    counter =4
    while(counter !=13):
        for i in range(0,len(list_of_dna)-counter):
            for j in range(0,counter):
                concatnation = concatnation + list_of_dna[i+j]
            if (str(concatnation) == reverse_complement(str(concatnation))):
                listing.append(i)
                listing.append(len(concatnation))
                second_list.append(listing)
                listing=[]
            concatnation = ""
        counter = counter +1 
    for i in range(0,len(second_list)):
        second_list[i] = tuple(second_list[i])
    return second_list

print(rev_palindrome("CAA"))

            