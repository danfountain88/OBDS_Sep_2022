from pickle import TRUE
from re import T


i = 1 

running = True

while running:
    if i < 11:
        print(i)
        i+=1
    else:
        running = False


for i in range(-1,-11,-1):
    print(i)

#calculate sum of defined number
number = 5
total = 0

for i in range(1,number,1):
    total+= i

print(total)

number = 6
total = 0
i = 1

while i < number+1:
    total+=i 
    i+=1
    print(total)


#print prime numbers betwen 1 and 50
prime_list = []
for i in range(1,51):
    if i == 1:
        print('')
    else:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_list.append(i)

for i in range(1,50):
    is_prime = True
    for j in range (2,i):
        if (i%j == 0):
            is_prime = False
    if is_prime == True:
        print(i)


#Functions exercise 1
def complement(sequence):
    complement_sequence = ''
    for base in sequence:
        if base == 'A':
            complement_sequence += 'T'
        elif base == 'T':
            complement_sequence += 'A'
        elif base == 'G':
            complement_sequence += 'C'
        elif base == 'C':
            complement_sequence += 'G'
        else:
            complement_sequence = ''
            print('ERROR')
    print(complement_sequence)    


#Functions exercise 1
def complement(sequence):
    complement_sequence = ''
    for base in sequence:
        if base == 'A':
            complement_sequence += 'T'
        elif base == 'T':
            complement_sequence += 'A'
        elif base == 'G':
            complement_sequence += 'C'
        elif base == 'C':
            complement_sequence += 'G'
        else:
            print('ERROR')
            break
    print(complement_sequence)  

complement('ATGC')

#Function exercises 2
def reverse(string):
    string2 = ''
    for i in range (len(string)-1,-1,-1):
        string2+=string[i]
    return string2

reverse('hello')

#Function exercises 3

def rev_complement(sequence):
    rev_complement_sequence = ''
    sequence2 = reverse(sequence)
    for base in sequence2:
        if base == 'A':
            rev_complement_sequence += 'T'
        elif base == 'T':
            rev_complement_sequence += 'A'
        elif base == 'G':
            rev_complement_sequence += 'C'
        elif base == 'C':
            rev_complement_sequence += 'G'
        else:
            rev_complement_sequence = ''
            print('ERROR')
            break
    print(rev_complement_sequence)  

rev_complement('ATGC')

complement(reverse())