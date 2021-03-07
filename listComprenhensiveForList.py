fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = [x if x != 'apple' else 'apel' if x != 'banana' else 'botol' for x in fruits]
print(newList)