fileScanned = False


def newFileScan():
    global filename
    filename = input("Type in the name of the file you want to scan:")
    print("Scanning file: " + filename)
    
    global fileScanned
    fileScanned = True
    print("Successfully scanned file: " + filename + "!")
    
def printText():
    global file
    global fileLines
    file = open(filename)
    fileLines = open(filename)
    
    global fileList
    global fileLineList
    fileList = file.read().split()    # stores file into a list of many strings.
    fileLineList = fileLines.readlines()    # splits the entire text into lines and returns a list of it.
    print(fileList) # temp
    print(fileLineList) # temp
    

def findLine():
    if fileScanned == True:
        linecount = 0
        
        for i in range(len(fileLineList)):  # go throught the list using indecises
            linePosition = fileLineList[i].find(word)  # find the word within each item in the list
            if linePosition != -1:
                linecount += 1
                print(f"[{linecount}] -- Line: '{i+1}'")
                
        print(f"'{word}' was found in {linecount} lines " )
        
        if linecount <= 0:
            print(f"Null")
    else:
        print("No file detected. Please scan file before retrying.")
        menu()
        

def findWord():
    if fileScanned == True:
        global word
        word = input("Enter a word to search for in the file: ")
        count = 0

        for i in range(len(fileList)):  # go throught the list using indecises
            position = fileList[i].find(word)  # find the word within each item in the list
            if position != -1:
                count += 1

        if count > 1:
            print(f"The word '{word}' was found {count} times in the file.")
        elif count == 1:
            print(f"The word '{word}' was found {count} time in the file.")
        else:
            print(f"The word '{word}' was not found in the file.")
    else:
        print("No file detected. Please scan file before retrying.")
        menu()
    

def backtomenu():
    option = input("Back to the menu? (Y/N): ")
    if option == "Y" or option == "y":
        menu()
    else:
        exit()
    

def menu():
    print("\nSearch Engine Menu:")
    print("1. Scan a new file")
    print("2. Find an occurence in the file")
    print("3. Find lines containing an occurrence")
    print("4. Exit Program")
    choice = input("Enter your choice (1-4): ")
    
    while True:
        if choice == "1":
            newFileScan()
            printText()
            input("Scan complete. Press Enter to continue...")
            menu()
        elif choice == "2":
            findWord()
            backtomenu()
        elif choice == "3":
            findWord()
            findLine()
            backtomenu()
        elif choice == "4":
            print("Exiting...")
            exit()
        else:
            print("Invalid choice! Please try again.")
            menu()
    
menu()