#declaring variables

first=4
second="This is string"
third="23"
fourth=float(input("Enter a float number"))
fifth=first+fourth

#multi line declaration

a,b,c="a","b",input("can i enter input prompt?")
if(c):
    print("yes you can input prompt on multi line declaration")

#printing int and str
print("here first int is changed to str :",str(first) +third)              #we cannot print int and string so chane int to str
print("here third str is changed to int :",first +int(third))              #we cannot print int and string so chane int to str

#introduction of Replacement fields
print ("Sum of first and fourth {0} and {1}=".format(first,fourth),fifth)

