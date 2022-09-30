#!/usr/bin/env python 

#add args
import argparse       #import argparse module into python - needed for reading one file and writing to another
import sys
import logging
import tqdm

parser = argparse.ArgumentParser() # Create a parser
                                                        #add as many parser arguements as needed for option
parser.add_argument('-a',                               # input
                    '--bed_a',                          # input in .sam format
                    default='None',
                    dest='bed_a',                     # Variable name to store option (optional)
                    help='Upload as bed file to check another file against',          # Help text (optional)
                    ) 
parser.add_argument('-b',                               # input
                    '--bed_b',                          # input in .sam format
                    default='None',
                    dest='bed_b',                     # Variable name to store option (optional)
                    help='A comparative bed file to check if files in bed_a match this file',          # Help text (optional)
                    ) 
parser.add_argument('-o',                               # output short form
                    '--output',                         # output long form
                    default='onscreen',           # standard out, normally - or stdout           
                    dest='overlap',                      # Variable name to store option (optional)
                    help='This is a list of sequence names in your bed_a that matches bed_b',        # Help text (optional)
                    )
args = parser.parse_args() # Parse arguments

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

#Run warnings
if args.bed_a == 'None' or args.bed_b == 'None':
    logging.warning('No -a or -b file specified. Terminating program!')
    sys.exit()
#overlapping intervals
else:
    print('Opening files...')
    instances = 0
    with open(args.overlap, mode='w') as overlap: #open output file to write
        with open(args.bed_a, mode="r") as bed_a: #open bed file to read which you want to check overlaps with
            with open(args.bed_b, mode="r") as bed_b: #open comparator bedfile
                logging.info(f'Beginning overlapping analysis comparing {args.bed_a} and {args.bed_b}')
                logging.info(f'Progress:')
                if args.overlap == 'onscreen':
                    logging.info(f'Running output as sequence name on screen...\n')
                line_total = sum(1 for line in bed_a)
                bed_a.seek(0)
                with tqdm.tqdm(total=line_total) as progress:
                    for index_a, line_a in enumerate(bed_a): #check each line of bed_a
                        a_columns = line_a.strip().split('\t') #split the line into strings, extr
                        chr_a = a_columns[0]
                        start_a = int(a_columns[1])
                        end_a = int(a_columns[2])
                        name_a = a_columns[3]
                        #breakpoint()
                        bed_b.seek(0)
                        progress.update(1)
                        for index_b, line_b in enumerate(bed_b):
                            b_columns = line_b.strip().split('\t')
                            chr_b = b_columns[0]
                            start_b = int(b_columns[1])
                            end_b = int(b_columns[2])
                            name_b = b_columns[3]                   
                            if chr_a == chr_b:                                  #if the chromosomes are the same then ...
                                if end_a >= start_b and end_b >= start_a:
                                    if args.overlap == 'onscreen':
                                        sys.stdout.write(f'{b_columns[3]}\t')
                                    else:
                                        overlap.write(f'{index_a}\t{name_a}\t{start_a}\n') #report overlapping interval as list with line break
                                    instances += 1                                      #counter 'instances' which increases in each loop

    if args.overlap != 'onscreen':
        sys.stdout.write(f'Output saved to your file in tab-delimited format of sequence line number, name, and start position\n')

    sys.stdout.write(f'The number of overlapping sequences is {instances}!\n')  #Final statement of number of instances


