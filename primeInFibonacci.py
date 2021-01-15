# Γράψτε ένα κώδικα σε Python ο οποίος ελέγχει αν ο ν όρος της ακολουθίας Fibonacci είναι πρώτος ή όχι. 
# Για να απαντήσετε αν ένας αριθμός p είναι πρώτος θα πρέπει για 20 τυχαίες επιλογές του a να ισχύει ότι a^p=a mod p. 
# Ο κώδικάς σας παίρνει τον όρο της ακολουθίας Fibonacci από το χρήστη.

from functools import lru_cache
# import random

try:
    n_term = int(input("Παρακαλώ δώστε τον ν-οστό όρο που επιθυμείτε: "))
except:
    raise TypeError("n must be a positive integer")


@lru_cache(maxsize=1000) # create a cache for numbers that the function has already calculated to speed up the process
def fibonacci(n): 
    # validate input
    if n <= 0: 
        raise TypeError("n must be a positive integer")

    # find the Nth number
    if n == 1: 
        # first number is 1
        return 1
    elif n == 2:
        # second number is 1
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2) 

# the implimantion of the prime rule given above genarates a bug
# def isPrime(p):
#     # create and fill list to hold the 20 different numbers to check against p in order to find if it's prime or not
#     a = []
#     for i in range(1,21):
#         a.append(random.randint(1, n_term-1))
#         print(a[i-1])

#     # check if p is prime 
#     temp = 0
#     for i in a:
#         if a[i] ** p == a[i] % p: #! the bug is in the condition
#             print("hi2")
#             temp += 1
#     print(temp)
#     if temp == 20:
#         return "is prime" 
#     else:
#         return "is composite (not a prime)"

def isPrime(p):
    #corner cases
    if (p <= 1):
        return "is composite (not a prime)"
    elif(p == 2):
        return "is prime"
    elif(p % 2 == 0):# eliminating the multiples of 2
        return "is composite (not a prime)"

    #checking for numbers >=3 (the odds)
    for i in range(3, p, 2):
        if (p % i == 0):
            return "is composite (not a prime)"
 
    return "is prime"
 
 
# Driver Code
if isPrime(11):
    print("true")
else:
    print("false")

# program start
fib = fibonacci(n_term)
print(fib,isPrime(fib))

