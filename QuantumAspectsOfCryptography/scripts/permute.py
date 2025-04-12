import random

learners = ["Aryaman", "Moida", "Niranjan", "Sreyas" ]

def permute_natural_numbers(N):
    numbers = list(range(1, N + 1)) # I could just do range(N) here to simplify everything but ok...later
    random.shuffle(numbers)
    return numbers

def unique(permuted_list,N):
    for i in range(0, N):
        if (permuted_list[i] == i+1):
            return False
# Example usage
if __name__ == "__main__":
    
    N = int(input("Enter a value for N: "))
    
    permuted_list = permute_natural_numbers(N)
    
    while (unique(permuted_list,N) == False):
        permuted_list = permute_natural_numbers(N)
    
    print("Random permutation:", permuted_list)

    for i in range(0,N):
        print(f'{learners[i]} evaluates {learners[permuted_list[i]-1]}')
    

#Assignment 2

# Aryaman (1)
# Moida (2)
# Niranjan (3)
# Sreyas (4)

# [2, 3, 4, 1]

# Aryaman evaluates Moida
# Moida evaluates Niranjan
# Niranjan evaluates Sreyas
# Sreyas evaluates Aryaman 


#Assignment 3

# Aryaman (1)
# Moida (2)
# Niranjan (3)
# Sreyas (4)


# [4, 3, 2, 1]

# Aryaman evaluates Sreyas
# Moida evaluates Niranjan
# Niranjan evaluates Moida
# Sreyas evaluates Aryaman


#Assignment 4

# Aryaman (1)
# Moida (2)
# Niranjan (3)
# Sreyas (4)


# [3,1,4,2]

# Aryaman evaluates Niranjan
# Moida evaluates Ayraman
# Niranjan evaluates Sreyas
# Sreyas evaluates Moida



# Assignment 5

# Aryaman (1)
# Moida (2)
# Niranjan (3)
# Sreyas (4)

# Random permutation: [3, 4, 1, 2]

# Aryaman evaulates Niranjan
# Moida evaulates Sreyas
# Niranjan evaulates Aryaman
# Sreyas evaulates Moida


# Assignment 6

# Aryaman evaulates Moida
# Moida evaulates Sreyas
# Niranjan evaulates Aryaman
# Sreyas evaulates Niranjan

# Assignment 7

# Aryaman evaluates Moida
# Moida evaluates Niranjan
# Niranjan evaluates Sreyas
# Sreyas evaluates Aryaman