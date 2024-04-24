### EXCEPTIONS ###

#1. 
#UNPACKING A TUPLE
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia', 'Russia']

reversed_names = names[::-1]

Est, Rus, *rest = reversed_names
print(Est, Rus, rest)

nordic_names = rest
print(nordic_names)


