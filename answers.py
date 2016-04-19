#! /usr/bin/env python

from collections import Counter
import pybedtools

#Question 1: Write a Python program to read the lamina.bed file and report
#the following: 
#   1. On what chromosome is the region with the largest start position
#   (2nd column) in lamina.bed?

filename = '/Users/gregkirkpatrick/devel/data-sets/bed/lamina.bed'

lamina_bed = pybedtools.BedTool(filename)

largest_chrom = ''
largest_start = 0

for record in lamina_bed:

    if int(record.start) > largest_start:
        largest_start = record.start
        largest_chrom = record.chrom

answer_1_1 = largest_chrom
print "answer-1.1: %s" % answer_1_1

#   2. What is the region with the largest end position on chrY in
#   lamina.bed? Report as chromA: 1-1000

largest_end = 0

for record in lamina_bed:

    if record.chrom != 'chrY': continue
    if int(record.end) > largest_end:
        largest_end = record.end
        largest_end_chrom = record.chrom
        largest_end_start = record.start

print 'answer-1.2: %s:%s-%s' % (largest_end_chrom, largest_end_start, largest_end) 

#Use Python to read the SP1.fq file in the data-sets repository. 
#   1. Which of the first 10 sequence records has the largest number of
#   'C' residues in the sequence? Report its record name.

        #Answer 2.1 C count is 17

filename2 = '/Users/gregkirkpatrick/devel/data-sets/fastq/SP1.fq'

line_num = 0
max_Cs = 0
seq_num = 0
big_seq = ''
largest_tot_qual = 0
rev_comp_list = []

def reverse_complement(seq):
    comps = []
    for char in seq:
        if char == 'A':
            comps.append('T')
        elif char == 'T':
            comps.append('A')
        elif char == 'G':
            comps.append('C')
        elif char == 'C':
            comps.append('G')
        elif char == 'U':
            comps.append('A')
    return ''.join(reversed(comps))


for line in open(filename2):
    line_type = line_num % 4

    if line_type == 0:
        name = line.strip()
    elif line_type == 1:
        seq = line.strip()
        seq_num += 1
    elif line_type == 3:
        quals = line.strip()

        counts = Counter(seq)
        if counts['C'] > max_Cs and seq_num <= 10:
            max_Cs = counts['C']
            big_seq = name

        sum_qual = sum([ord(i) for i in quals])
        if sum_qual > largest_tot_qual:
            largest_tot_qual = sum_qual

        if seq_num <= 10:
            rev_comp_list.append(reverse_complement(seq))

    line_num += 1

answer_2_1 = max_Cs

print 'answer-2.1: %s' % (answer_2_1)

#   2. For each record, convert each character in the quality score to a
#   number, and sum the numbers.  Use the python function ord to convert
#   characters to numbers. Report the largest total quality score.

print 'answer-2.2: %s'  % (largest_tot_qual)

print 'answer-2.3:'
for item in rev_comp_list:
    print item
