- For List comprehension, a new list is created

```
friends = ["Sam", "Samantha", "Saurabh"]

starts_s = [friend for friend in friends if friend.startswith("S")]
print(starts_s)

print(friends is starts_s) # False because the 2 lists are in different mem locations
```

- How to include a conditional statement in a list comprehension in Python
`[name for name in names_list if name.startswith("B)]`