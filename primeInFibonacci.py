# Γράψτε ένα κώδικα σε Python ο οποίος ελέγχει αν ο ν όρος της ακολουθίας Fibonacci είναι πρώτος ή όχι. 
# Για να απαντήσετε αν ένας αριθμός p είναι πρώτος θα πρέπει για 20 τυχαίες επιλογές του a να ισχύει ότι a^p=a mod p. 
# Ο κώδικάς σας παίρνει τον όρο της ακολουθίας Fibonacci από το χρήστη.
import random
# issue #2, given the Nth nubmer of the Fibonacci sequence calculate if it's a prime
try:
    n_term = int(input("Παρακαλώ δώστε τον ν-οστό όρο που επιθυμείτε: "))
except:
    raise TypeError("n must be a positive integer")


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

def isPrime(p):
    # create and fill list to hold the 20 random numbers 
    # to check against p in order to find if it's prime or not
    testCases = []
    for i in range(1,21):
        testCases.append(random.randint(1, n_term-1))
            
    # check if p is prime 
    flag = False
    for i in testCases:
        if testCases[i] ** p == testCases[i] % p: 
            flag = True
    return ("is prime" if flag == False else "is composite (not a prime)")
    
# program start
fib = fibonacci(n_term)
print(fib,isPrime(fib))

