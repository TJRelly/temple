# break stops a loop
# continue skips an item

# access the indexes using range

characters = ["Iron Man", "Scarlet Witch", "Black Panther", "Captain America"]

for character in characters: 
    if(character == "Black Panther"):
        print((character + " is the coolest!").upper())
        break
    elif(character == "Iron Man"):
        continue
    else: 
        print(character + " is cool.")

# access the indexes using range
# len function --- length of list

for x in range(0, 5):
    print(x) 

# type list
print(list(range(len(characters)))) 

for i in range(len(characters)):
    print(characters[i])

print(list(enumerate(characters))) # tuples

for i, character in enumerate(characters):
    print(i, character)

#RECAP
    
#break - stops loop
#continue - skips item in list
#len - length
#range - gives numbers
#enumerate - gives tuples  
#Tuples
    #iterable - can be looped over
    #imutable - can't be changed    

my_tup = (1, 2, 3)

for i,num in enumerate(my_tup):
    print(i, num) 

#Slicing
my_string = "Hello World!"
print(my_string[0:4])   
print(my_string[:5])
print(my_string[6:-1])
print(my_string[-1]) 
print(my_string[:])  #copy
print(my_string[::]) #copy
print(my_string[::2]) #skips every 2nd item
print(my_string[::-1]) #reverse
print(characters[::-3])