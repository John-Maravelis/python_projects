# Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει τις διαστάσεις ενός ορθογωνίου και θα φτιάχνει μέσα από λίστες τον αντίστοιχο πίνακα. 
# Στην συνέχεια θα βρίσκει το πλήθος των θέσεων και γεμίζει στην τύχη τις μισές με S και τις μισές με O. 
# Σκοπός είναι να μετρήσετε πόσες φορές εμφανίζεται το SOS οριζόντια, κάθετα, και διαγώνια. 
# Το πρόγραμμα επαναλλαμβάνεται 100 φορές (για τις ίδιες διαστάσεις) και επιστρέφει τον μέσο όρο των τριάδων SOS.
import random
try:
    rows = int(input("Δώσε το πλήθος των γραμμών: "))
    cols = int(input("Δώσε το πλήθος των στηλών: "))
except:
    raise TypeError("The rows and columns must be a positive integer")

matrix = [[None for i in range(cols)] for j in range(rows)] # create the requested matrix
cages = rows * cols
keyword = "SOS"
sumSOS = 0 # store the sum of the times the keyword was found

# create the 8 different directions to search in based on x,y values in a Cartesian system
xDir = [-1, -1, -1, 0, 0, 1, 1, 1]
yDir = [-1, 0, 1, -1, 1, -1, 0, 1]
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

    def searchMatrix(r, c, word):
        # if the first letter doesn't match return False
        if matrix[r][c] != word[0]:
            return False
        
        for j in range(8):
            # initialize the starting point for the current direction
            rowDir = r + xDir[j]
            colDir = c + yDir[j]

            # check for the remaining characters
            for k in range(1, len(word)):
                # break if position out of bounds
                if(rowDir >= rows or rowDir < 0 or colDir >= cols or colDir < 0):
                    break
                
                # break if characters don't match
                if(matrix[rowDir][colDir] != word[k]):
                    break

                # continue moving in the desired direction
                rowDir += xDir[j]
                colDir += yDir[j]

                # if all the characters have matched then it should be equal to k
                if k == len(word):
                    return True
        return False

    def findWord(word):
        global sumSOS
        for r in range(rows):
            for c in range(cols):
                if searchMatrix(r, c, word):
                    sumSOS += 1
    findWord(keyword)

avgSOS = int(sumSOS / 100) # calculate the average appeareances of "SOS" in a 100 randomly different matrices
print(sumSOS)
print(matrix)
print(avgSOS)