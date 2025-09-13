# strings
# strings is a data type that store a sequence of character
# basic operation :
str1= 'string'
str2= "string"
str3= '''string'''
# scape siquence character : '\n'

str= "hello, \n my name is Akibul"
print(str)

# basic operation

# 1/ concatination
conString = str1 + str2
print(conString)
# 2/ leanth of str 
print(len(str1))
 
# 3/ indexing
# Indexing means accessing a character at a specific position in a string using its index.
indexOfI=str1[3] 
# 3/ Slicing
# Accessing parts of a string
# str[ starting_idx : ending_idx ] #ending idx is not included
# str = "ApnaCollege"
# str[ 1 :4 ] is "pna"
# str[ : 4 ] is same as str[ O : 4]
# str[ 1 : ] is same as str[ 1 : len(str) ]


# 4/ String Functions
# str = "I am a coder."
# str.endswith("er.") #returns true if string ends with substr
# str.capitalize() #capitalizes 1st char
# str.replace( old, new ) #replaces all occurrences of old with new
# str.find( word ) #returns 1st index of 1st occurrence
# str.count("am") #counts the occurrence of substr in string