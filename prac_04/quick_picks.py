import random
CONSTANTS = []
pick = int(input("How many quick picks? "))
for i in range(1, 7):
    CONSTANTS.append(random.randint(1, 45))
print(repr(CONSTANTS))

print(CONSTANTS)