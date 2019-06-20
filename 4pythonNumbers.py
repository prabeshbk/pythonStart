# int float complex

a,b,c=1,3.0,1j    # only j indicated complex number
print(type(a),type(b),type(c))

# we change the data type
a,b,c=complex(a),int(b),c
print(type(a),type(b),type(c))

# random numbers
# python doesnt have a random function  but has built in random module used to make random numbers

