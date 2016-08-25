x = "There are %d types of people."%10 #decalare variable with string value remember not to place , before argumnet
binary = "binary" #declare string
do_not = "don't" #declare String
y = "Those who know %s and those who %s."%(binary,do_not) #declare String with argument

print x #printing string with argument
print y #printing string with multiple argument

print "I said: %r."%x  #passing string with argument to print string
print "I also said: '%s'."%y #same as above

hilarious = False #declare boolean
joke_evalution = "Isn't that joke so funny? ! %r" #accepting value in advance

print joke_evalution %hilarious #passing argument dynamically

w = "This is the left side of ..."
e = "a string with a right side."

print w + e #concating string
