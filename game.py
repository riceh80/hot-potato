import random

list = []
player = 0
seconds = random.randint(1, 180)

for i in range (0, 11):
    user = input("Enter your name: ")
    list.append(user)

for i in len(list):
    list.pop(seconds / len(list))
    print(user + "has been removed")
