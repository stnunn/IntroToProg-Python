# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,01.01.2020,Created started script
# SNunn,05.15.2020,Added initial code to complete assignment 5
# SNunn,05.16.2020,Reworked logic for removing items (Choice 3)
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strPath = 'C:\\_PythonClass\\Assignment05\\ToDoList.txt'
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = "" # Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

objFile = open(strPath, "r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Task":lstRow[0],"Priority":lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()
# print(lstTable)

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Choice 1 - Show the current items in the table
    if strChoice.strip() == '1':
        for dict in lstTable:
            strTask, strPrty = dict.values()
            print(strTask,"|",strPrty)
    # Choice 2 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        strNewTask = input("What is the task name you would like to add? ")
        strNewPrty = input("What is the task priority you would like to add? ")
        lstTable.append({"Task":strNewTask,"Priority":strNewPrty})
    # Choice 3 - Remove an item from the list/Table
    elif strChoice.strip() == '3':
        strRmvTask = input("What is the task name you would like to remove? ")
        numRemoved = 0 # counter for how many Tasks with that name were removed
        for dict in lstTable:
            if dict["Task"].lower() == strRmvTask.lower():
                lstTable.remove(dict)
                # print("'" + strRmvTask + "'","removed successfully.")
                numRemoved = numRemoved + 1
        if numRemoved == 1:
            print(str(numRemoved) + " instance of '" + strRmvTask + "' was removed.")
        else:
            print(str(numRemoved) + " instances of '" + strRmvTask + "' were removed.")
    # Choice 4 - Save tasks to the ToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open(strPath, "w")
        for dict in lstTable:
            strTask, strPrty = dict.values()
            objFile.write(strTask + "," + strPrty + "\n")
        objFile.close()
        print("Data was successfully save to file.")
    # Choice 5 - Exit program
    elif strChoice.strip() == '5':
        break  # and Exit the program

input("Press Enter key to exit the program.")
