# Γράψτε ένα κώδικα σε Python ο οποίος να παίρνει σαν είσοδο ένα αρχείο ASCII κειμένου και μετατρέπει τον κάθε χαρακτήρα του 
# στον “κατοπτρικό” του χαρακτήρα ASCII. Κατοπτρικοί χαρακτήρες είναι αυτοί των οποίων το άθροισμα είναι 255. 
# Εμφανίστε το κατοπτρικό κείμενο στο χρήστη με ανάποδη σειρά χαρακτήρων.

def textToASCII(f):
    file = open(f, "r")
    words = file.read().split(" ")
    reflectedWords = []

    for i in range(len(words)): # iteration for every word in the list
        temp = ""
        for char in words[i]: # iteration for every character in the words
            temp += chr(255 - ord(char)) # convert the each character to its reflective one in ASCII
       
        temp += " "
        reflectedWords.append(temp[::-1]) # reverse and append the new word to a new list

    result = " ".join(reflectedWords) # join the final reversed list in a string
    file.close()
    return result

# start of the program
filePath = "dummyTextForReflectiveASCII.txt"
print(textToASCII(filePath))