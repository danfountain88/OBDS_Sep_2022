'''
Start with sam file
skip the header
   Headers start with @, if starts with @ skip
   Copy the required column info into the output bed file

   
SAM file



BED format                              SAM col in python (0-based)
    chr                                 [2] 
    start                               [3] 
    end                                 [3]+[8]-1
    name                                [0]
    score                               [4] MAPQ
    strand  "+" "-" "."                 use [1] and check bit info                  



'''

### Script to convert Sam to Bed file ###
#! /usr/bin/env python

# Need to use the command line to go to the path of the folder where script and file are saved
#Read SAM file input - COMPLETE
# with open("test.sam", mode="r") as sam_file:
#     print("This is the output of the first 5 lines of the file:\n")

#     for i, line in enumerate(sam_file):
#         if i < 25:
#             line_with_no_return_character = line.strip()
#             print(line_with_no_return_character)
#         else:
#             break

import argparse
import gzip

parser = argparse.ArgumentParser() # Create a parser
parser.add_argument('-o', # output 
                    dest='bedfile', # Variable name to store option (optional)
                    help='This is your bedfile', # Help text (optional)
                    )
parser.add_argument('-i', # input
                    '--input', # input in .sam format
                    dest='samfile', # Variable name to store option (optional)
                    help='Upload as SAM file', # Help text (optional)
                    ) 
parser.add_argument('-z', # compress file
                    '--compress', #compress the file in .bed.gz format
                    dest='compress', #variable 
                    default=False, #Default option is not to compress
                    action='store_true', #Flag to specify compressing file
                    )
parser.add_argument('-p',
                    '--padding',
                    default=0,
                    dest='pad',
                    help='specify padding',
                    )
args = parser.parse_args() # Parse arguments

#Define a function to determine if compressed or not
if args.compress == False:
    bed_file = open(args.bedfile, mode="w")
else:
    if not args.bedfile.endswith('.gz'):
        args.bedfile += '.gz' #change ending to .gz
    bed_file = gzip.open(args.bedfile, mode="wt")

#Write BED file output
with open(args.samfile, mode="r") as sam_file:
    for i, line in enumerate(sam_file):
        if not line.startswith('@'):
            #Extract required information from line
            column = line.split('\t')
            chr = column[2]
            if chr != '*':
                start = int(column[3]) - int(args.pad)
                end = int(column[3]) + int(column[8]) - 1 + int(args.pad) #might be wrong
                name = column[0]
                score = column[4]
                bed_file.write(f'{chr}\t{start}\t{end}\t{name}\t{score}\t.\n')
                
#Close the file          
bed_file.close()               
                
                
                
# if i < 5:
#     line_with_no_return_character = line.strip()
#     print(line_with_no_return_character)
# else:
#     break

#Convert to gz

#Supply input file names using command line parameters
#Supply the SAM file name on the command line using –i or —input


#Supply the BED file name on the command line using –o or —output

#Write out a gzip compressed file (.bed.gz)

#Make the script run on the command line


#Output what you are going to do
#Output what you have done
#Output anything that is unexpected
#Output anything that is of interest


##Extra task - use logging

