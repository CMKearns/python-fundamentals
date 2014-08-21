__author__ = 'oski'

#Loop over strings
for c in 'Alice', 'Bob', 'Carol':
    print c

#We want to replace this code

#alice_age = 20
#alice_is_drinking = True
#bob_age = 12
#bob_is_drinking = False
#charles_age = 22
#charles_is_drinking = True

Name = ['Alice','Bob','Charles']
Age = [20, 12, 22]
Drinking = [True, False, True]

for a,b,c in zip(Name, Age, Drinking):
    print '%s is %d years old' %(a,b)
    if c == True:
        if b<21:
            print "Not OK!"
        else:
            print "No problem"
    else:
        print "No need to check"
