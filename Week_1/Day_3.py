#Task 1
from platform import java_ver


participants = ['Li-Hsin','Nicole','Susann','Matt','Christina','Emily','Kinam','Yu','Judy','Felix','Dan']

#Task 2
participants_2 = participants
participants_3 = participants.copy()

#Task 3
participants.append('Andrea')
participants.append('David')

#Task 4
print(participants_2)
print(participants_3)

#Task 5
participants[2]
participants[4]
participants[2:5:2]

#Task 6
participants.sort()
participants[2:5]

#Task 7
participants[2][:2]

#Task 8
ab = {}
for name in participants:
    if name == 'David' or name == 'Andrea':
        ab[name] = 'Trainer'
    else:
        ab[name] = 'Trainee'

ab = {}
for name in participants:
    if name in ('David', 'Andrea'):
        ab[name] = 'Trainer'
    else:
        ab[name] = 'Trainee'


#Task 9
for name, role in ab.items():
    if role == 'Trainee':
        print(name)

#Task 10
participants_tuple = ('Li-Hsin','Nicole','Susann','Matt','Christina','Emily','Kinam','Yu','Judy','Felix','Dan')
participants_tuple_2 = participants_tuple
participants_tuple_3 = participants_tuple.copy() #can't copy
participants_tuple.append('Andrea') #can't append
participants_tuple.append('David') #can't append
print(participants_tuple_2)
print(participants_tuple_3) #not defined as unable to copy
participants_tuple[2]
participants_tuple[4]
participants_tuple[2:5:2]
participants_tuple.sort() #can't sort
participants_tuple[2:5]
participants_tuple[2][:2]

#Task 11
#see separate .py


#Algorithms

sequence = 'TATAATGCTGACTTATAGCGCTATATATATATA'
promoter = sequence

#Exercise 1

def make_ordinal(n):
    '''
    Convert an integer into its ordinal representation::

        make_ordinal(0)   => '0th'
        make_ordinal(3)   => '3rd'
        make_ordinal(122) => '122nd'
        make_ordinal(213) => '213th'
    '''
    n = int(n)
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix


def motif_finder(motif,promoter):
    motif_start = []
    motif_end = []
    motif_count = 0
    motif_position = []
    for i in range(0,len(promoter)-4,1):
        if promoter[i:i+4] == motif:
            motif_start.append(i+1)
            motif_end.append(i+4)
            motif_count += 1
            motif_position.append(motif_count)
    for position, start, end in zip(motif_position, motif_start, motif_end):
        print ('Your', make_ordinal(position), 'motif starts at position',start,'and ends at position',end)
    print('The total occurences of',motif,'in your promoter sequence is:',motif_count)


#Exercise 2

def GC_content(sequence):
    GC = 0
    for base in sequence:
        if base == 'G' or base == 'C':
            GC += 1
    GCcontent = GC/len(sequence)*100
    print('Your GC content is',round(GCcontent, 2),'%')


#Exercise 3

def hamming_distance(sequence1,sequence2):
    hammer = 0
    if len(sequence1) != len(sequence2):
        print('ERROR - sequences of unequal length')
    else:
        for i, j in zip(sequence1,sequence2):
            if i != j:
                hammer += 1
        print('The hamming distance is', hammer)


#Exercise 4

def consensus_motif(motif_list):
    from tabulate import tabulate
    
    #if lists not equal, break
    if len(set(map(len,motif_list)))!=1:
        print('ERROR - motifs not of equal length')
    else:    
        #create necessary variable
        table = [['Sequence number / Base number',list(range(1,len(motif_list[1])+1))]]
        Acount = [0] * len(motif_list[1])
        Tcount = [0] * len(motif_list[1])
        Ccount = [0] * len(motif_list[1])
        Gcount = [0] * len(motif_list[1])
        Consensus = []
        
        #Present bases
        for i in range(0,len(motif_list),1):
            table += [[i+1,list(motif_list[i])]]
        
        #Compile base counts
        for j in range(0,len(motif_list),1):
            for k in range(0,len(motif_list[j]),1):
                Acount[k] += motif_list[j][k].count('A')
                Ccount[k] += motif_list[j][k].count('C')
                Gcount[k] += motif_list[j][k].count('G')
                Tcount[k] += motif_list[j][k].count('T')
    
        #Make consensus
        for i in range(0,len(motif_list[0]),1):
            if Acount[i] > Tcount[i] and Acount[i] > Gcount[i] and Acount[i] > Ccount[i]:
                Consensus += 'A'
            elif Tcount[i] > Acount[i] and Tcount[i] > Gcount[i] and Tcount[i] > Ccount[i]:
                Consensus += 'T'
            elif Gcount[i] > Tcount[i] and Gcount[i] > Acount[i] and Gcount[i] > Ccount[i]:
                Consensus += 'G'
            elif Ccount[i] > Tcount[i] and Ccount[i] > Gcount[i] and Ccount[i] > Acount[i]:
                Consensus += 'C'
            else:
                Consensus += 'X'
        
        #Compile table
        table += [['A count',Acount],['C count',Ccount],['G count',Gcount],['T count',Tcount],['Consensus',Consensus]]
        print(tabulate(table,headers='firstrow',tablefmt='fancy_grid'))


motif_list1 = ['ATCCAGCT', 'GGGCAACT', 'ATGGATCT', 'AAGCAACC', 'TTGGAACT', 'ATGCCATT', 'ATGGCACT']
motif_list2 = ['ATCCAGCT', 'GGGCT', 'ATGGATCT', 'AAGCAACC', 'TTGGAACT']
motif_list3 = ['ATCCAGCT', 'GGGCAACT', 'ATGGATCT', 'AAGCAACC']
motif_list4 = ['ATCCAGCATGTC', 'GGGCAACTAATT', 'ATGGATCTCTGT', 'AAGCAACCATGT']


consensus_motif(motif_list2)

