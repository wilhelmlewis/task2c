msg = "Social Situation Analysis Results\n"

# get user 1 input
print("Welcome to the Social Situation Analyzer System")
print("Person One")
user_one = input("\tEnter your name: ")
user_one_pos = eval(input("\tEnter your position (x, y): "))
user_one_space = eval(input("\tEnter your personal space radius: "))

# get user 2 input
print("\nPerson Two")
user_two = input("\tEnter your name: ")
user_two_pos = eval(input("\tEnter your position (x, y): "))
user_two_space = eval(input("\tEnter your personal space radius: "))

# person test
if user_one_pos < user_two_pos:
    msg += "\n\tPerson test: " + user_one + " is in " + user_two + "'s personal space"
elif user_two_pos < user_one_pos:
    msg += "\n\tPerson test: " + user_two + " is in " + user_one + "'s personal space"
elif user_one_pos < user_two_pos and user_two_pos < user_one_pos:
    msg += "\n\tPerson test: " + user_one + " and " + user_two + "are in each other's personal space"
else:
    msg += "\n\tPerson test: Neither " + user_one + " nor " + user_two + "is in the other's personal space"

# space test
if user_one_pos < user_two_pos or user_two_pos < user_one_pos:
    msg += "\n\tSpace test: " + user_one + " and " + user_two + "'s personal spaces overlap"
elif not user_one_pos < user_two_pos and not user_two_pos < user_one_pos:
    msg += "\n\Space test: " + user_one + " and " + user_two + "'s personal spaces do not overlap"
elif user_one_pos - user_two_pos >= user_one_space:
    msg += "\n\Space test: " + user_one + "'s personal space is entirely inside " + user_two + "'s personal space"
else:
    msg += "\n\Space test: " + user_two + "'s personal space is entirely inside " + user_one + "'s personal space"

print(msg)
