#CurrencyConverter.py
#Author Henry Mbugua
#Description: Convert Euro to USD or vice versa
from __builtin__ import raw_input
from twisted.protocols.ftp import USR_LOGGED_IN_PROCEED

#1 USD = 0.7617
#1 Euro = 1.3218 
def currencyConvert():
    #Find out what the user want to convert: 1=Euro to USD or 2=USD to Euro
    #Store answer into a variable
    print "--------------------------------------------------------"
    userChoice = raw_input("What do you want to convert? \n1 USD > Euro \n2) Euro > USD\n")
    print userChoice
    
    #Check and see what the user typed
    #If the user typed 1
    
    if userChoice == "1":
    
    #Prompt the user the amount of USD they want to convert
    #Store what the user typed into a variable
       userUSD = input("Enter the amount in USD you wish convert\n")
    
       Euro = userUSD * 0.7617
    #output the amount to the user
       print "$ %0.2f" %userUSD, "= %0.2f" %Euro, "Euros"
       print "--------------------------------------------------------"
       doAgain()
    #if the user typed 2
    elif userChoice == "2":
    #Prompt the user the amount of USD they want to convert
    #Store what the user typed into a variable
       userEuro = input("Enter the amount in Euro you wish convert\n")
    
       USD = userEuro * 1.3218
    #output the amount to the user
       print " %0.2f" %userEuro, "Euro = $ %0.2f" %USD
       print "--------------------------------------------------------"
       doAgain() 
    #if the user typed anything else
    else:
    #Tell the user what they did wrong
        print "Error: You entered invalid information. Please try Again"
        print "--------------------------------------------------------"
    #Run the script again
        currencyConvert()
        
def doAgain():
    #Prompt the user if they would like to run the convert currency program again
    userDoAgain = raw_input("Would you like to convert again?\n1) Yes \n2) No\n ")
    #Checks what the user typed
    #if choice was 1
    if userDoAgain == "1":
        currencyConvert()
    #if choice was 2
    elif userDoAgain == "2":
        print "Thank you for using this program"
    
    #if choice was anything else
    else:
        print "Error: You entered invalid information. Please try again"
        doAgain()
currencyConvert()