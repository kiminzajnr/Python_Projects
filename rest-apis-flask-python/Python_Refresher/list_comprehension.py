# numbers = [1, 3, 5]
# doubled = []

# # for num in numbers:
# #     doubled.append(num * 2)

# # print(doubled)



# doubled = [num * 2 for num in numbers]

# print(doubled)

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "jen"]

# starts_s = []

# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)

# print(starts_s)

starts_s = [friend for friend in friends if friend.startswith("S")]
print(starts_s)

print("friends: ", id(friends), "starts_s", id(starts_s))