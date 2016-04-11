def print_only(x):
   y = x * 2
   print y

def return_only(x):
   y = x * 2
   return y

print "running print_only ..."
print_only(7)
#Prints out running print_only 14.

print "running return_only ..."
return_only(7)
#only prints out running return_only

print "printing print_only ..."
print print_only(7)
#prints print_only

print "printing return_only ..."
return_only(7)
#prints 14

print "using print_only ..."
print_only(7) + 6
#prints out using print_only then an error

print "using return_only ..."
return_only(7) + 6
#prints out error and 14.
