#Name; Dictionary Assignment
#purpose: To showcase list and dictionary manipulation.
#date: April 1st 2025
#By Isaiah Mims

#making the list of fruits
fruits = ['apple', 'banana', 'cherry']
print(fruits)
#accessing the first and last element in the list
print(fruits[0])
print(fruits[2])
#adding grape to the list and printing the updated list
fruits.append('grape')
print(fruits)

#List slicing and indexing
numbers = [10,20,30,40,50]
#slicing the first three elements
print(numbers[:3])
#printing the last two numbers using an negative index
print(numbers[-2:])
#replacing the 20 with 25
numbers[1] = 25
print(numbers)

#Listing the Methods
colors = ['red','green','blue']
#appending yellow to the back of the list
colors.append('yellow')
#inserting black to the beginning of the list
colors.insert(0,'black')
#removing blue from the list
colors.remove('blue')
#sorting the list in alphabetical order
colors.sort()
print(colors)

#searching a list
def NameSearch(nameset, name):
    if name in nameset:
        print(nameset.index(name))
    else:
        print("Not found, please try again.")


#making the list of median
    def numberset(numbers):
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)

        if n == 0:
            return None  # Handling the cases of no numvers

        if n % 2 == 1:  # Odd number of elements
            median = sorted_numbers[n // 2]
        else:  # Even number of elements
            middle1 = sorted_numbers[(n // 2) - 1]
            middle2 = sorted_numbers[n // 2]
            median = (middle1 + middle2) / 2

        return median

#creating the dictionary for student
student = {
    "Name": "John Doe",
    "Age": "21",
    "Major": "Computer Science"

}
#printing the student name
print(student["Name"])
#updating the age
student.update({"Age": "22"})
#adding a new key value pair of GPA
student["GPA"] = "3.8"
#removing a key from the dictionary
student.pop("Major")
print(student)

#Using Dictionary Methods
grades = {
    'John': 85,
    'Alice': 92,
    "Bob": 78

}
#adding a new student to the dictionary
grades["David"] = 88
#checking to see if Alice exists in the dictionary
if grades.get("Alice"):
    print("Alice is on the list.")
else:
    print("Alice is not on the list.")

#printing all the names of the students using a list
for name in grades:
    print(f"{name} has a grade of {grades[name]}")

#Word Frequency counter
def count_words(sentence):
    # Convert to lowercase and split into words
    words = sentence.lower().split()

    # Initialize an empty dictionary
    word_count = {}

    # Count occurrences of each word
    for word in words:

        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


# Get input from user
user_input = input("Enter a sentence: ")

# Count the words
result = count_words(user_input)

# Print the result
print("\nWord counts:")
print(result)

sales = {
    'John': 1500,
    'Alice': 2200,
    'Bob': 1800
}

sorted_sales = dict(sorted(sales.items(), key=lambda item: item[1], reverse=True))
#the loop statement for each
print("Sales, in order, are as follows: (descending):")
for name, amount in sorted_sales.items():
    print(f"{name}: ${amount}")



#Finding the frequenetly used words
def find_most_frequent_word(words):
    word_count = {}

    # Count occurrences of each word
    for word in words:
        word = word.lower()  # Make case-insensitive
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Find the word with maximum count
    max_count = 0
    most_frequent = []

    for word, count in word_count.items():
        if count > max_count:
            max_count = count
            most_frequent = [word]
        elif count == max_count:
            most_frequent.append(word)

    return most_frequent, max_count



