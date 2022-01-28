members = ["Bob", "Tom", "Ken"]
print(members[0])
print(members[1])

# 課題解説　例
print(members[:2])

# 課題解説　例　
print('\n'.join(member for member in ["Bob", "Tom", "Ken"] if member == "Bob" or member == "Tom"))
print('\n'.join(member for member in members if member == "Bob" or member == "Tom"))

# 課題解説　例　
print(members[0], members[1])
