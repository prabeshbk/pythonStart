import random
print(random.random())
print(random.randrange(1,10,2))   #randrange(start,stop,step)


#random from list
cities=['kathamandu','NY','London']
print("which city should i visit next? >>>>",random.choice(cities))
print("which city should i visit next? >>>>",random.sample(cities,3))  #sample use for unique elements from list
print("which city should i visit next? >>>>",random.choices(cities,k=3))  #sample use for any(can be repeat) elements from list

# The seed method is used to initialize the pseudorandom number generator in Python.
# The random module uses the seed value as a base to generate a random number. If seed value is not present, it takes a system current time.
random.seed(2)
print(random.random())
random.seed()
#shuffle the list
random.shuffle(cities)
print(cities)

#floating point numbers within a range
print(random.uniform(11.5,33.4))
#random.triangular(low, high, mode)  it randoms lower <= N <= upper and with the specified mode between those bounds.
print(random.triangular(10.5, 25.5, 5.5))

print(17.031749500267054/5.5)