from datetime import date

def percentOfBrumAndMan(string):
    string = string.upper()  #converts to upper
    percentage = (string.count("B") + string.count("M")) / int(len(string))*100 # counting for, B stands for birmingham and M stands for Manchester tickets
    # calculates the percentage with /int(len(string) on the count
    return round(percentage, 2)

ticketTableDict = {
        'B': {'City': 'Birmingham', 'Ticket Price': 29.2}, # the table containing the cities their keys and their prices
        'C': {'City': 'Cardiff', 'Ticket Price': 16.6},
        'H': {'City': 'Hereford', 'Ticket Price': 34.7},
        'L': {'City': 'Liverpool', 'Ticket Price': 31.7},
        'M': {'City': 'Manchester', 'Ticket Price': 38.0},
        'N': {'City': 'Newport', 'Ticket Price': 19.8},
        'S': {'City': 'Shrewsbury', 'Ticket Price': 15.2}
    }

def ticketTablePrice(string, ticketTableDict):
    string = string.upper()  # converts to upper
    price = 0.0
    for i in string:
        if i in ticketTableDict:
            price += ticketTableDict[i]['Ticket Price']
        elif i == ' ':
            pass
        elif not i in ticketTableDict:
            print("Unrecognised city symbol detected " + str(i))
    return round(price, 2)

def numberOfTicketsSold(string):
    string = string.upper() # converts the string to all uppercase to avoid case sensitive error
    outputDict = { # dictionary of the city's and their counts
        'B': 0,
        'C': 0,
        'H': 0,
        'L': 0,
        'M': 0,
        'N': 0,
        'S': 0,
    }
    for i in string:
        if i in outputDict:
            outputDict[i] += 1 # increments the count in teh dict if the key exists
    return outputDict

def SetOfTicketsSold(string):
    ticketset = set() # initialises a set
    for i in string:
        ticketset.add(i) # adds all elements in the string to the set
    return ticketset

def quitFunction(filename):
    totalsetdict = { # dictionary of the city's and their counts
        'B': 0,
        'C': 0,
        'H': 0,
        'L': 0,
        'M': 0,
        'N': 0,
        'S': 0,
    }
    try:
        with open(filename, "r+") as file: # this opens and reads the file as read and write
            print("This is file: " + filename)
            totalLetters = file.read().split() # makes the txt file into a list
            totalLettersStr = ' '.join(totalLetters) # makes the list into a string
            for i in totalLetters:
                ticketset = set(SetOfTicketsSold(i)) # loops through the list and adds the strings to a set making function
                for j in ticketset:
                    if j in totalsetdict:
                        totalsetdict[j] += 1 # counts up the values from the single set of ticket characters then adds them to the dict
            print(str(totalLetters)) # below prints the calculated info to the screen calling previous functions
            print("Number of tickets sold: "+str(numberOfTicketsSold(totalLettersStr)))
            print("Number of hours in hours of each city: "+str(totalsetdict))
            print("The total price of sold tickets is: £" + str(ticketTablePrice(totalLettersStr, ticketTableDict)))
            file.close() # closes the file
    except:
        print("file cannot open")

#this is the actual task 4 function
def task4loopFinal(ticketTableDict):
    totalLetters = "" # initialises a string to increament the city key characters

    filename = str(date.today()) # creates the filename from the current date using import date
    filename += ".txt"
    try:
        file = open(filename, "w")

        quit = False # creates a boolean quit, so it can be used to exit out of the while loop once its changed to true
        while quit == False: # while loop that keeps going while quit = false
            string = input("Enter cities string Task 4\n") # asks the users to input the cities ticket string (for task4)
            if string == "quit": # runs once the user inputs quit
                file.write(totalLetters) #writes the cities ticket string to the file
                file.close()# closes the file
                quit = True # ends the loop
                quitFunction(filename)# calls the quit function to calculate the values and print to the screen

            else:
                Currentletters = "" # initialises a string to increament the city key characters for this loop
                for i in string:
                    if i in ticketTableDict:
                        Currentletters += i #for each element in the current cities input string if it is in the dict then add it to the current

                    elif not i in ticketTableDict: # if not output this text and continue
                        print("Error. Unrecognized city symbol is detected. Please enter the cities string again. Acceptable list of cities symbols are B, C, H, L, M, N and S")
                        continue
                totalLetters = totalLetters + " " + Currentletters #adds the currentletters to the total once the input string as been iterated through
    except:
        print("file cannot open")

# This function doesn't meet all the requirements of the task however i believe that it logically works better so i included it in the final code file just to inspect
# def task4loop(ticketTableDict):
#     totalLetters = "" # creates a string to increament the city key characters
#     totalsetdict = { # dictionary of the city's and their counts
#         'B': 0,
#         'C': 0,
#         'H': 0,
#         'L': 0,
#         'M': 0,
#         'N': 0,
#         'S': 0,
#     }
#
#     filename = str(date.today()) # creates the filename from the current date using import date
#     filename += ".txt"
#     file = open(filename, "w")
#
#     quit = False # creates a boolean quit, so it can be used to exit out of the while loop once its changed to true
#     while quit == False: # while loop that keeps going while quit = false
#         string = input("Enter cities string Task 4\n") # asks the users to input the cities ticket string (for task4)
#         if string == "quit": # runs once the user inputs quit
#             quit = True # ends the loop
#             print(str(totalLetters))  # below prints the calculated info to the screen calling previous functions
#             print("Number of tickets sold: " + str(numberOfTicketsSold(totalLetters)))
#             print("Number of hours in hours of each city: " + str(totalsetdict))
#             print("The total price of sold tickets is: " + str(ticketTablePrice(totalLetters, ticketTableDict)))
#
#             file.write(str(totalLetters)+"\n")# writes the info to the file on new lines
#             file.write("Number of tickets sold: " + str(numberOfTicketsSold(totalLetters))+"\n")
#             file.write("Number of hours in hours of each city: " + str(totalsetdict)+"\n")
#             file.write("The total price of sold tickets is: " + str(ticketTablePrice(totalLetters, ticketTableDict))+"\n")
#             file.close() # closes the file
#         else:
#             Currentletters = "" # initialises a string to increament the city key characters for this loop
#             for i in string:
#                 if i in ticketTableDict:
#                     Currentletters += i #for each element in the current cities input string if it is in the dict then add it to the current
#
#                 elif not i in ticketTableDict: # if not output this text and continue
#                     print("Error. Unrecognized city symbol is detected. Please enter the cities string again. Acceptable list of cities symbols are B, C, H, L, M, N and S")
#                     continue
#             totalLetters += Currentletters #adds the currentletters to the total once the input string as been iterated through
#             ticketset = set(SetOfTicketsSold(Currentletters)) # adds the strings to a set making function
#             for i in ticketset:
#                 if i in totalsetdict:
#                     totalsetdict[i] += 1 #iterates through from the single set of ticket characters then adds them to the dict if its key exists in the dict


if __name__ == '__main__':
    # uncomment/comment out the code below to run the code for the specific tasks

    # Task 1
    #CitiesString = "BMMNSB" #Test Example
    print(percentOfBrumAndMan(input("Enter cities string Task 1\n")))

    #Task 2
    # CitiesString = "BMMNSBK" #Test Example containing a wrong character k
    print("£"+str(ticketTablePrice(input("Enter cities string Task 2\n"), ticketTableDict)))

    # Task 3
    CitiesString = "BCCBBLNNLLBBMMMBCBCLLMSMBMBMBMNMNSSLSCS" #Test Example
    print(numberOfTicketsSold(CitiesString))

    # Task 4
    # BBMNH MMMBB #Test Example
    ##task4loop(ticketTableDict) # this function is the old task 4 function which does not meet all the requirements but is better in some ways
    task4loopFinal(ticketTableDict)# this is the main task 4 function to be run which meets all the tasks requirements

