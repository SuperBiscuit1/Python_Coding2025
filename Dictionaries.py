#creating a dictionary for the student
student = {
    "Name": "John Doe",
    "Age": "20",
    "Major": "Computer Science",
    "GPA": "3.8",

}


print(student)

#printing out for name and major
print(student["Name"])
print(student["Major"])

#now its time to add and update values
student.update({"graduation_date" : "2026", "email" : "johndoe@example.com", "GPA" : "3.9"})
print(student)

#Removing age from the dictionary
del student["Age"]
print(student)

#checking to see if email exists
print("email" in student.values())

#Iterating over keys and values then prints each item in the dictionary on every other line

for thing, show in student.items():
    print(f"{thing}:{show}" + "\n")

#storing the inputs of the user into a dictionary
taco = input("Please Write a sentence then hit Enter: ")

#next making them split into words
beef = taco.split()

#this then stores the result into dictionary
tomato = {}

#now creating the loop
for be in beef:
    if be in tomato:
       tomato[be] += 1
else:
    tomato[be] = 1


print("Words in your sentences: ", tomato)

#finding the maximum value within the dictionary
python_scores = {"Alice" : "85", "Bob" : "92", "Charlie" : "88", "David" : "75"}

topscore = max(python_scores, key=python_scores.get) #getting the max score from the python score dictionary
print(topscore)

#time to merge the dictionaries
dict1 = {"a": 100, 'b':200}
dict2 = {'c': 300, 'd': 400}

merged = {**dict1, **dict2}
print(merged)

#inverting a dictionary
python_ages = {"Alice: " : "25", "Bob: " : "30", "Charlie: " : "35"}
new_diction = {k: s for s, k in python_ages.items() }
print(new_diction)

#time to remove duplicate values
python_data = {'name1': 'apple', 'name2' : 'banana', 'name3': 'apple', 'name4': 'orange'}
work = set()
new_data = {}

for c, e in python_data.items():
    if e not in work:
        new_data[c] = e
        work.add(e)

print(new_data)


#Sorting the values in a dictionary
python_sales = {'John': 1500, 'Alice': 2200, 'Bob': 1800}
rangers =  dict(sorted(python_sales.items(), key=lambda x: x[1], reverse=True))
print(rangers)


#Nested Dictionary Access

python_employee = {
    'name': 'Alice',
    'position': 'Software Engineer',
    'salary': {
        'base': 70000,
        'bonus': 5000
    }
}


def print_employee_details(employee, indent=0):
    # Print name and position directly
    print(" " * indent + f"name: {employee['name']}")
    print(" " * indent + f"position: {employee['position']}")

    # Calculate and print salary details
    if 'salary' in employee and isinstance(employee['salary'], dict):
        base = employee['salary'].get('base', 0)
        bonus = employee['salary'].get('bonus', 0)
        total = base + bonus

        print(" " * indent + "salary:")
        print(" " * (indent + 2) + f"base: {base}")
        print(" " * (indent + 2) + f"bonus: {bonus}")
        print(" " * (indent + 2) + f"total: {total}")


print_employee_details(python_employee)

#frequency of characters in a string

python_text = "hello"
counting = {}

for stuff in python_text:
    counting[stuff] = counting.get(stuff, 0) + 1

print(counting)

#using a dictionary comprehension to make a dictionary
evil = {num: num**2 for num in range(1,6)}
print(evil)

