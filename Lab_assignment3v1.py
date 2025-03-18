#creating a list called fruit and listing the variables in it.
fruit = ["apple","banana","cherry","date","elderberry"]
#creating a list of number
numbers = [3,1,4,5,9,2,6,5,3,5]



#now going to print the list from above
print(fruit)

#printing the first and last elements of fruit
print(fruit[0])
print(fruit[4])

#slicing the list to print the first three elements
print(fruit[0:2])

#printing every other fruit
print(fruit[::2])

#replacing banana with blueberry
fruit[1] = "blueberry"
print(fruit)

#inserting fig in the index 2
fruit.insert(2, "Fig")
print(fruit)

#adding grape to the end of the list using append
fruit.append("grape")
print(fruit)

#removing the date from the list
fruit.remove("date")
print(fruit)

#Finding the List and Learning the Length of the list called Numbers
print("Length in the Numbers List", len(numbers))

#Sorting the List in an ascending order
numbers.sort()
print(numbers)

#Removing the last element from the number
numbers.pop()
print(numbers)

#checking to see if 4 is in the list
print("Is 4 in the list?", 4 in numbers)

#printing each item in the numbers list
print(fruit)
for fruits in fruit:
    print(fruit)

#converting the fruit names to uppercase
print(fruit)
for i in fruit:
    print(i.upper())

#random number as well as maximum number
import random

randomnumbers = [random.randint(1,1000) for _ in range(10)]
print(randomnumbers)
print("Max: ", max(randomnumbers))

#Copying the Lists with original on it
original = [10,20,30]
badcopy = original
copylist = original[:]
original[1] = 90
print("Original: ", original)
print("Copy: ", copylist)

#Finding the median
group = [2,54,10,32,13]
group.sort()
med = sum(group)/len(group)
print("Median: ", med)
print("Sorted: ", group)

#Matrix lists that loop
import numpy as np

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(matrix)
matr = matrix[1][2]
print("Row 2, Column 3 value is: ", matr)

for ma in matrix:
    print(matrix)

#Doing list comprehensions
number = [1,2,3,4,5,6,7,8,9,10]

seq = [i * i for i in number]
print(seq)

ser = [i * i for i in number if i % 2 == 0]
print(ser)

#now removing duplicates from lists
duplicates = [1,2,3,4,2,3,5,6,3,7]

def remove_duplicates(lst): #function
    watch = set()
    sleep = [] #creates an empty list for the new set to be stored in
    for i in lst:
        if i not in watch: #if there isn't any duplicates...
                sleep.append(i) #then add the numbers to the brackets
                watch.add(i) #it will be added from the command called set.
    return sleep #will show the output back to the user.


slop = remove_duplicates(duplicates)  #testing out the function

print(duplicates) #print the original list
print(slop)  #prints the newly tested function


#Simulating a To-Do List
# Initialize an empty to-do list
todo_list = []

# Loop to ask for tasks
while True:
    rocks = input("Please type in your task, or type 'done' to escape: ")

    # Check if the user wants to exit
    if rocks.lower() == "done":
        break

    # Add the task to the to-do list
    todo_list.append(rocks)

# Print the tasks
print("\nYour tasks are: ")
for rocks in todo_list:
    print(f"> {rocks}")