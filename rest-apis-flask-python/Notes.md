- For List comprehension, a new list is created

```
friends = ["Sam", "Samantha", "Saurabh"]

starts_s = [friend for friend in friends if friend.startswith("S")]
print(starts_s)

print(friends is starts_s) # False because the 2 lists are in different mem locations
```

- How to include a conditional statement in a list comprehension in Python
```
[name for name in names_list if name.startswith("B")]
```

- Lambda function -  a function without a name, used to return a value


```# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {
    'name': 'Jose',
    'school': 'Computing',
    'grades': (66, 77, 88)
}

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades =   data['grades']
    return sum(grades) / len(grades)


# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student['grades'])
        count += len(student['grades'])

    return total / count```