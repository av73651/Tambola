#This is a my learning app to build a tambola game
#This version will have row wins & full house
# user will enter 3 rows and 4 numbers in each row between 1-99. no duplicate numbers
# program will generate its only tambola winning numbers
# program will also gerate one lucky number
# Row wins 10,000
# 2 row wins 50000
# 3 row wins 100000
# lucky number gets 5000

#method to get userinput
import random

def getuserinputs():
    valid_input=False
    while(valid_input==False):
       user_row = input ("Enter 3 numbers separated by commas between 1-99: ")
       row = user_row.split(",")
       if (validate_user_input(row)==True and validate_distinct_numbers_in_row (row)==True):
            row_numbers=[int(number) for number in row]
            valid_input=True
       else:
            print("Invalid input")
            valid_input=False
      
    print(row_numbers)
    return row_numbers

#METHOD TO VALIDATE USER INPUTS
def validate_user_input(row):
     if len(row)==3:
        for i in row:
            if (i.isnumeric()==True) and int(i) in range(1,100):
                next
            else:
                return False
     else:
        return False
     return True

# new method to validate distinct inputs

def validate_distinct_numbers_in_row(row):
    valid_user_input=True   
    for i in range(0,len(row)-1):
       if row.count(row[i])>1:
            print("Error: Each number should be different")
            valid_user_input=False
            break
       else:
            next
    return valid_user_input

def validate_distinct_numbers_in_set(row1,row2):
   valid_user_input = "True"
   if row1.isdisjoint(row2)==True:
       valid_user_input = "True"
   else:
       print ("following numbers were repeated between your rows:", row1.intersection(row2))
       valid_user_input=False
   return valid_user_input
def startGame():

    print ("Game starts now.... we will generating 30 lucky #s and let see if you win")
    print ("--------------------------------------------------------------------------")
    gameset=set()
    winnings=0
    for start in range(0,30):
        newluckynumber=generateluckynumber(gameset)
        gameset.add(newluckynumber)
        if firstset.issubset(gameset):
            print ("first row full strike")
            winnings=winnings+1
        if secondset.issubset(gameset):
            print ("second row full strike")
            winnings=winnings+1
        if thirdset.issubset(gameset):
            print ("third row full strike")
            winnings=winnings+1
    
    newluckynumber=generateluckynumber(gameset)
    print ("finally the lucky number...",newluckynumber)
    if newluckynumber in firstset or newluckynumber in secondset or newluckynumber in thirdset:
            winnings=winnings+1
    print("firstset",firstset)
    print("secondset",secondset)
    print("thirdset",thirdset)
    print("drawedpool",gameset)
    if winnings>0:
        print("you win:",100**winnings)
    else:
        print("hard luck try again..")
## system generating numbers

def generateluckynumber(generatedset):
    successflag=False
    while(successflag==False):
        newluckynumber = int(random.randint(1,99))
        #print("lucky# generated....", newluckynumber)
        if newluckynumber in generatedset:
            successflag=False
        else:
            successflag=True
            break
    return newluckynumber


#main program
print("Welcome to Tambola")
print("-----------------------------------------------------------------------")
print("First Row")
print("-----------------------------------------------------------------------")
firstrow = getuserinputs()
firstset= {int(number) for number in firstrow}
print("Second Row")
print("-----------------------------------------------------------------------")
valid_input=False
while valid_input==False:
    secondrow = getuserinputs()
    secondset= {int(number) for number in secondrow}
    if validate_distinct_numbers_in_set(firstset,secondset) == 'True':
        valid_input=True
        break
    else:
        valid_input=False
print("third Row")
print("-----------------------------------------------------------------------")
valid_input=False
while valid_input==False:
    thirdrow = getuserinputs()
    thirdset= {int(number) for number in thirdrow}
    if validate_distinct_numbers_in_set(firstset,secondset)=='True' and validate_distinct_numbers_in_set(firstset,thirdset)=='True' and validate_distinct_numbers_in_set(secondset,thirdset)=='True':
        valid_input=True
        break
    else:
        valid_input=False

startGame()
