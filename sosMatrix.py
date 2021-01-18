# Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει τις διαστάσεις ενός ορθογωνίου και θα φτιάχνει μέσα από λίστες τον αντίστοιχο πίνακα. 
# Στην συνέχεια θα βρίσκει το πλήθος των θέσεων και γεμίζει στην τύχη τις μισές με S και τις μισές με O. 
# Σκοπός είναι να μετρήσετε πόσες φορές εμφανίζεται το SOS οριζόντια, κάθετα, και διαγώνια. 
# Το πρόγραμμα επαναλλαμβάνεται 100 φορές (για τις ίδιες διαστάσεις) και επιστρέφει τον μέσο όρο των τριάδων SOS.

# issue #5, get the dimensions of matrix, randomly fill with: S, O, S and the find how many "SOS" occur horizontally, vertically and diagonally
import random
try:
    rows = int(input("Δώσε το πλήθος των γραμμών: "))
    cols = int(input("Δώσε το πλήθος των στηλών: "))
except:
    raise TypeError("The rows and columns must be a positive integer")

matrix = [[None for i in range(cols)] for j in range(rows)] # create the requested matrix
cages = rows * cols
sumSOS = 0 # store the sum of the matrices
word = "SOS"

for i in range (100): # loop 100 times and find the mean value that "SOS" appears in the matrix
    posCache = [] # a list to cache the used indexes
   
    for c in range(1, cages + 1): # loop through all the cages
        
        def createRandPos():
            while True: 
                randRow = random.randint(0, rows - 1) # random row index
                randCol = random.randint(0, cols - 1) # random column index
                tempPos = randRow, randCol # temporary pair of (row, col) index
            
                # checking if the pair has already been generated and if not
                # append it to the cache and break out of the loop
                if tempPos not in posCache: 
                    posCache.append(tempPos) 
                    break
            return randRow, randCol

        def fillMatrix():
            rowIndex, colIndex = createRandPos()

            if c <= int(cages / 2): # filling half of the cages with "S" and half with "O"
                matrix[rowIndex][colIndex] = "S"
            else:
                matrix[rowIndex][colIndex] = "O"
        
        fillMatrix()

# i have to implement a function where it searches through the matrix and finds "SOS"

avgSOS = int(sumSOS / 100) # calculate the average appeareances of "SOS" in a 100 randomly different matrices
print(matrix)
print(avgSOS)