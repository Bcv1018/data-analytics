# Lab 1
CustomerId = '12345' # I thought this variable would be to hold a customerID number but I am thinking it would better to put it as an integer?
CustomerName = 'Buster Posey' # This variable was used to hold the customers name but it could be separted into two variables named first and last name
CustomerGender = 'Male' # I thought this would be to hold the customers gender.
CustomerDOB = '04-27-87' # I thought this would be the customers date of birth and maybe it should be a int? instead of a str or if there is a date syntax for data type it would be that? Maybe also make another variable for their age?
DriversLicenseNum = 'f123456' # I thought this was customers driver license and maybe just include the digits instead of f or maybe not idk how DL are formatted and if they are different for each state.
AutoPolicyNum = '56656' # This I really don't know but I am guessing its like a case number or a ticket number for an accident?
# I am assuming that these varaibles are to hold car insurance customer's information

# Lab 2
# a) What is the full list of reserved words that can’t be used for variable names?
# Full list of reserved words that can't be used for variable names is the following:
# False Def If Raise None Del Import Return True Elif In Try And Else is While As
# Except Lambda With Assert Finally Nonlocal Yield Break For Not Class Form Or
# Continue Global Pass
import keyword
print (keyword.kwlist)
print ('The amount of keywords is:',len(keyword.kwlist))

# b) Pick 5 of these words and review the explanation for how it is used as a keyword in
#    Python. Add these 5 definitions as # comments to your exercise document. Put ^^
#    around any terms that you are not familiar with.
# 1. ^Lambda^ - A lambda function is an anonymous function it can take any number of arguments but only have a single expression
# 2. ^Nonlocal^ - This keyword is used in functions inside function to create anonymous functions
# 3. ^Global^ - Accessing a global variable is simple as any other variable but to modify a global variable, you need to use the global keyword
# 4.  Continue - It is a control flow statement used to continue to the next  iteration of a loop. Unlike break, the continure statement does not exit the loop.
# 5.  Elif - Shorthand for else if, checks if some other condition holds when the condition in the if statement is false.
