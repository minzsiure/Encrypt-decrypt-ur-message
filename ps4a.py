# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    if len(sequence) <= 1:
        return [sequence]
   
    #input 'ab'
    else: #if there's more than 1 char
        permutation = [] #a temp list
        first_char = sequence [0] 
        #first_char = a
        
        rest_char = sequence [1:] #from index 1 to the rest
        #rest_char = b
        
        perm_of_seq = get_permutations(rest_char) 
        #keep getting permutations of the rest characters until the length = 1
        #in this case, it stopped when perm_of_seq = b
        
        
        for seq in perm_of_seq: #iterate over character
        #for b in b
            
            for index in range(len(seq) + 1):
            #iterate over every index 012345
            #for 0 in range 2
            #for 1 in range 2 
                
                new_seq = seq [0:index] + first_char + seq[index:len(seq)+1]
                #new_seq = char from start to index + first char + char from index to end
                #new_seq = nothing + a + b = ab
                #new_seq = b + a + nothing = ba
                
                permutation.append(new_seq) #add to the output list
                #add ab
                #add ba
                
        return permutation #output ab, ba
        
            
    
    
sequence = 'abcde'
print(get_permutations(sequence))

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

