import os
import textwrap

refFile = input('Enter name of reference file: ')
newRef = "mmbir_" + refFile
tempRef = "tempRef.txt"
insertions = "insertions" + refFile + ".txt"
newRef_temp = "tempNewRef.txt"
ins_len = int(input('Enter desired length of MMBIR insertion (nt): '))      #Length of mmbir insertion desired.
temp_finder = int(input('Enter desired distance to insertion (nt): '))   #Distance that template finder is expected to look.
regions = int(input('Approximately how many MMBIR insertions should be added? '))    #number of MMBIR insertions to add to the dna

def make_files():
    f1 = open(refFile, "r")
    f2 = open(newRef, "w+")
    f3 = open(tempRef, "w+")
    for l1 in f1:
        if l1.startswith(">"):
            f2.write(l1)
        else:
            f3.write(l1.rstrip('\n'))
    f1.close()
    f2.close()

    f3.read()
    k = 0
    with open(tempRef, "r") as dna:
        bases = str(dna.read())
        for b in bases:
            if b != "N":
                k += 1
        region_len = k / regions
        if region_len <= 2*(temp_finder + ins_len):
            print('too many insertions for size of chromosome!')
            exit()
        regions_list = insert_newlines(bases, int(region_len))
        #f4.write('\n'.join(chunks_list))

    frags = regions_list
    templates_list = []
    insertions_list= []
    for b2 in frags:
        templates_list.append(b2[0:ins_len])
    for e in templates_list:
        if 'N' in e:
            insertions_list.append(e)
        else:
            insertions_list.append(reverse_complement(e))
    f4 = open(insertions, "w+")
    mmbir_regions = [m for m in regions_list if 'N' not in m]
    mmbir_events = [o for (o,q) in zip(insertions_list, regions_list) if 'N' not in q]
    f4.write('MMBIR insertion length: ' + str(ins_len) + '\nDistance to template: ' + str(temp_finder) + '\nRegions requested: ' + str(regions) + '\n')
    f4.write(str(len(mmbir_regions)) + ' MMBIR insertions were added to the reference: \n')
    f4.write('\n'.join(mmbir_events))
    f4.close()

    #The following list comprehension is where all the magic happens. It is basically the model for mmbir repair events.
    f5 = open(newRef_temp, "w+")
    mmbir_list = [j if 'N' in j else make_insertion(j, h, temp_finder) for (j, h) in zip(regions_list, insertions_list)]
    #first, if there's an N in the string, don't add an insertion.
    #second, make_insertion function below splits the string at the distance specified by temp_finder and adds the string from insertions list.
    #NO SEQUENCE WILL BE REPLACED IN THIS VERSION (CREATES INSERTION WITHOUT DELETION)!
    #f2.write('\n'.join(mmbir_list))
    f5.write('\n'.join(mmbir_list))

    wrapped_f5 = rewrap_file(newRef_temp)
    f6 = open(wrapped_f5, 'r')

    f2_append = open(newRef, "a+")
    for l3 in f6:
        f2_append.write(l3)

    f2_append.close()
    f3.close()
    f5.close()
    os.remove(tempRef)
    os.remove(newRef_temp)
    f6.close()
    os.remove('tempFile2.txt')


def insert_newlines(dna, every):
    lines = []
    for i in range(0, len(dna), every):
        lines.append(dna[i:i + every])
    return lines


def reverse_complement(ins):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'a': 't', 'c': 'g', 'g': 'c', 't': 'a'}
    return ''.join([complement[base] for base in ins[::-1]])


def make_insertion(source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]


def rewrap_file(miswrapped_file):
    f1 = 'tempFile.txt'
    f3 = 'tempFile2.txt'
    text = open(miswrapped_file, 'r')
    text_0 = open(f1, 'w+')
    text_1 = text.read()
    text_0.write(textwrap.fill(text_1, 50))
    text_0.close()
    text.close()
    text_0 = open(f1, 'r')
    text_2 = open(f3, 'w+')
    text_1 = text_0.read()
    for line in text_1:
        text_2.write(line.replace(' ', ''))
    text_0.close()
    text_2.close()
    os.remove(f1)
    return 'tempFile2.txt'

def rewrap_file2(miswrapped_file):
    from Bio import SeqIO
    refin = miswrapped_file
    refout = 'tempFile2.txt'
    SeqIO.convert(refin, "fasta", refout, "fasta")
    return 'tempFile2.txt'


make_files()