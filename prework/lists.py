my_list = []
my_list = list()
print(type(my_list))

numbers = [2, 6, 10.6, 4]
print(numbers)
print(type(numbers))

print(numbers[1]) # 6

## All of these methods work in place # returns None
# .append()
# .insert(index, item)
# .remove() #only removes first index
# del list[index]
# .pop() removes last item
# .pop(index) removes item at index


numbers.append("TJ")
numbers.remove(6)
numbers.insert(2, "Jackson")
del numbers[0]
numbers.pop(0)

print(numbers)

## Sorting functions
# works OUT of place:
    # sorted() takes iterables
    # sorted(iterable, reverse=True)
# works in place:
    # .sort() ONLY works on lists # returns None
    #can take arguments such as .sort(reverse=True)
    # .reverse()

animals = ["frog", "lion", "bear", "monkey"]
# animals.sort()
# # print(animals)
# animals.sort(reverse=True)
# # print(animals)

print(sorted(animals))
print(animals)
animals.reverse()
print(animals)

