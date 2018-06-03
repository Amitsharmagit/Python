## A string is a sequence of characters. Strings are basically just a bunch of words.

## A Strings are immutable this means that once defined that can not be changed.


#Accessing Values in Strings
var1 = "amit"
var2 = "Software Testing"
print "var1[0]=",var1[0]
print "var2[1:5]=",var2[1:5]

#Some more examples
x = "Hello World!"
print x[:6] 
print x[0:6] + "Amit"

#Python String replace() Method
oldstring = 'I am Amit' 
newstring = oldstring.replace('am', 'are')
print newstring

#Changing upper and lower case strings
string="python at amit"
print string.upper()
string="python at amit"		
print string.capitalize()
string="PYTHON AT AMIT"
print string.lower()

#Using "join" function for the string
print"A".join("Python")	
	
#Reversing String
string="12345"		
print''.join(reversed(string))

#Split Strings
word="amitcareer "		
print word.split(' ')
word="amit career"		
print word.split('r')
x = "amit"

#Replace Function
x.replace("amit","Python")
print x
x = "amit"
x = x.replace("amit","Python")
print x
